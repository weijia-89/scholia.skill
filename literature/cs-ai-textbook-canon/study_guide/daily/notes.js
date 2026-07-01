/* cc-prep notes feature — hybrid localStorage + backend.
 *
 * Modes:
 *   be     — backend reachable; notes save via POST/PUT/DELETE to /api/note
 *            and are written into CC_Study_Guide.md or daily_notes.md.
 *   ls     — localhost or file://, backend NOT reachable; notes save to
 *            localStorage only. Export to markdown for sync.
 *   pages  — GitHub Pages or other static deployment; same as ls, plus a
 *            view-only banner.
 *
 * Notes rendering:
 *   Baked-in notes (from daily_notes.md at render time) appear as <aside
 *   class="user-note" data-source="baked"> from the server. This script
 *   appends LS-stored notes for anchors present on the page, then wires
 *   add/edit/delete UI on every <aside class="user-note"> and every
 *   [data-notable-anchor] element.
 */
(function () {
  'use strict';

  const API_BASE = location.origin + '/api/note';
  const LS_KEY = 'cs-ai-foundation-notes-v1';
  const MAX_TEXT_LEN = 2000;
  const PROBE_TIMEOUT_MS = 800;

  let backendAvailable = false;
  let mode = 'pages';

  // ---------- localStorage helpers ----------

  function lsLoad() {
    try {
      const raw = localStorage.getItem(LS_KEY);
      if (!raw) return {};
      const obj = JSON.parse(raw);
      return obj && typeof obj === 'object' ? obj : {};
    } catch { return {}; }
  }

  function lsSave(state) {
    try { localStorage.setItem(LS_KEY, JSON.stringify(state)); }
    catch (e) { console.warn('LS save failed', e); }
  }

  function lsAdd(anchor, text) {
    const state = lsLoad();
    state[anchor] = state[anchor] || [];
    const noteId = 'note-ls-' + anchor + '-' + Date.now().toString(36);
    state[anchor].push({ note_id: noteId, text: text, ts: Date.now() });
    lsSave(state);
    return noteId;
  }

  function lsUpdate(noteId, text) {
    const state = lsLoad();
    for (const anchor of Object.keys(state)) {
      const arr = state[anchor];
      for (let i = 0; i < arr.length; i++) {
        if (arr[i].note_id === noteId) {
          arr[i].text = text;
          arr[i].ts = Date.now();
          lsSave(state);
          return true;
        }
      }
    }
    return false;
  }

  function lsDelete(noteId) {
    const state = lsLoad();
    for (const anchor of Object.keys(state)) {
      const arr = state[anchor];
      const idx = arr.findIndex(n => n.note_id === noteId);
      if (idx !== -1) {
        arr.splice(idx, 1);
        if (arr.length === 0) delete state[anchor];
        lsSave(state);
        return true;
      }
    }
    return false;
  }

  function lsCount() {
    return Object.values(lsLoad()).reduce((sum, arr) => sum + arr.length, 0);
  }

  // ---------- Backend probe ----------

  async function probeBackend() {
    if (location.protocol === 'file:') return false;
    const isLocal = ['localhost', '127.0.0.1'].includes(location.hostname);
    if (!isLocal) return false;
    try {
      const ctrl = new AbortController();
      const t = setTimeout(() => ctrl.abort(), PROBE_TIMEOUT_MS);
      const r = await fetch(API_BASE, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: '{}',
        signal: ctrl.signal,
      });
      clearTimeout(t);
      // BE responds 400 "anchor and text required" to an empty body. Any
      // structured response means BE is reachable.
      return r.status === 400 || r.status === 200;
    } catch { return false; }
  }

  // ---------- API calls ----------

  async function apiAdd(anchor, text) {
    const r = await fetch(API_BASE, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ anchor, text }),
    });
    const data = await r.json();
    if (!data.ok) throw new Error(data.error || 'add failed');
    return data.note_id;
  }

  async function apiUpdate(noteId, text) {
    const r = await fetch(API_BASE + '/' + encodeURIComponent(noteId), {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text }),
    });
    const data = await r.json();
    if (!data.ok) throw new Error(data.error || 'update failed');
  }

  async function apiDelete(noteId) {
    const r = await fetch(API_BASE + '/' + encodeURIComponent(noteId), { method: 'DELETE' });
    const data = await r.json();
    if (!data.ok) throw new Error(data.error || 'delete failed');
  }

  // ---------- DOM helpers ----------

  function cssEscape(s) {
    if (window.CSS && CSS.escape) return CSS.escape(s);
    return String(s).replace(/[^a-zA-Z0-9_-]/g, c => '\\' + c);
  }

  function makeAside(noteId, anchor, text, source) {
    const aside = document.createElement('aside');
    aside.className = 'user-note';
    aside.dataset.noteId = noteId;
    aside.dataset.anchor = anchor;
    aside.dataset.source = source;
    aside.textContent = text;
    return aside;
  }

  function findInsertionPoint(anchor) {
    return document.querySelector('[data-notable-anchor="' + cssEscape(anchor) + '"]');
  }

  function lastNoteOrAnchor(anchor) {
    const all = document.querySelectorAll('aside.user-note[data-anchor="' + cssEscape(anchor) + '"]');
    if (all.length > 0) return all[all.length - 1];
    return findInsertionPoint(anchor);
  }

  // ---------- Render LS notes on page ----------

  function renderLsNotes() {
    const state = lsLoad();
    const onPage = new Set();
    document.querySelectorAll('[data-notable-anchor]').forEach(el => {
      onPage.add(el.dataset.notableAnchor);
    });
    for (const anchor of Object.keys(state)) {
      if (!onPage.has(anchor)) continue;
      for (const note of state[anchor]) {
        // Skip if a baked-in or BE-rendered note with this id already exists
        // (defensive against duplicate-render after import-then-reload).
        if (document.querySelector(
          'aside.user-note[data-note-id="' + cssEscape(note.note_id) + '"]'
        )) continue;
        const aside = makeAside(note.note_id, anchor, note.text, 'ls');
        const after = lastNoteOrAnchor(anchor);
        if (after) after.parentNode.insertBefore(aside, after.nextSibling);
      }
    }
  }

  // ---------- Add note ----------

  function makeAddButton(anchor) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'add-note-btn';
    btn.dataset.anchor = anchor;
    btn.textContent = '+ note';
    btn.title = 'Add a note for this section';
    btn.addEventListener('click', () => openAddForm(anchor, btn));
    return btn;
  }

  function openAddForm(anchor, triggerBtn) {
    const form = document.createElement('form');
    form.className = 'note-form note-form--add';
    form.dataset.anchor = anchor;

    const ta = document.createElement('textarea');
    ta.placeholder = 'Your note for this section...';
    ta.maxLength = MAX_TEXT_LEN;
    ta.required = true;
    ta.rows = 3;

    const saveBtn = document.createElement('button');
    saveBtn.type = 'submit';
    saveBtn.textContent = 'Save';

    const cancelBtn = document.createElement('button');
    cancelBtn.type = 'button';
    cancelBtn.textContent = 'Cancel';
    cancelBtn.addEventListener('click', () => form.replaceWith(triggerBtn));

    form.appendChild(ta);
    form.appendChild(saveBtn);
    form.appendChild(cancelBtn);

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = ta.value.trim();
      if (!text) return;
      saveBtn.disabled = true;
      try {
        let noteId;
        let source;
        if (backendAvailable) {
          noteId = await apiAdd(anchor, text);
          source = 'be';
        } else {
          noteId = lsAdd(anchor, text);
          source = 'ls';
        }
        const aside = makeAside(noteId, anchor, text, source);
        const after = lastNoteOrAnchor(anchor);
        if (after) after.parentNode.insertBefore(aside, after.nextSibling);
        form.replaceWith(triggerBtn);
        repositionAddButtons();
      } catch (err) {
        alert('Save failed: ' + err.message);
        saveBtn.disabled = false;
      }
    });

    triggerBtn.replaceWith(form);
    ta.focus();
  }

  function wireAddButtons() {
    document.querySelectorAll('[data-notable-anchor]').forEach(el => {
      const anchor = el.dataset.notableAnchor;
      const btn = makeAddButton(anchor);
      el.parentNode.insertBefore(btn, el.nextSibling);
    });
  }

  function repositionAddButtons() {
    document.querySelectorAll('button.add-note-btn').forEach(btn => {
      const anchor = btn.dataset.anchor;
      const last = lastNoteOrAnchor(anchor);
      if (last && last !== btn && last.nextSibling !== btn) {
        last.parentNode.insertBefore(btn, last.nextSibling);
      }
    });
  }

  // ---------- Edit / Delete ----------

  function wireNoteActions() {
    document.body.addEventListener('click', (e) => {
      const aside = e.target.closest('aside.user-note');
      if (!aside) return;
      if (aside.classList.contains('edit')) return;
      if (e.target.closest('button, textarea, form')) return;
      const isLs = aside.dataset.source === 'ls';
      if (!isLs && !backendAvailable) {
        // Baked or BE-sourced note in offline mode: cannot edit/delete here.
        alert('This note lives in the markdown source. To edit it, run the backend (python3 scripts/notes_server.py) and reload.');
        return;
      }
      openEditForm(aside);
    });
  }

  function openEditForm(aside) {
    const noteId = aside.dataset.noteId;
    const anchor = aside.dataset.anchor;
    const originalText = aside.textContent;
    aside.classList.add('edit');

    const form = document.createElement('form');
    form.className = 'note-form note-form--edit';

    const ta = document.createElement('textarea');
    ta.value = originalText;
    ta.maxLength = MAX_TEXT_LEN;
    ta.required = true;
    ta.rows = 3;

    const saveBtn = document.createElement('button');
    saveBtn.type = 'submit';
    saveBtn.textContent = 'Save';

    const deleteBtn = document.createElement('button');
    deleteBtn.type = 'button';
    deleteBtn.className = 'note-form__delete';
    deleteBtn.textContent = 'Delete';

    const cancelBtn = document.createElement('button');
    cancelBtn.type = 'button';
    cancelBtn.textContent = 'Cancel';
    cancelBtn.addEventListener('click', () => {
      aside.innerHTML = '';
      aside.textContent = originalText;
      aside.classList.remove('edit');
    });

    form.appendChild(ta);
    form.appendChild(saveBtn);
    form.appendChild(deleteBtn);
    form.appendChild(cancelBtn);

    aside.textContent = '';
    aside.appendChild(form);
    ta.focus();
    ta.setSelectionRange(ta.value.length, ta.value.length);

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const newText = ta.value.trim();
      if (!newText) return;
      saveBtn.disabled = true;
      try {
        const isLs = aside.dataset.source === 'ls';
        if (isLs || !backendAvailable) {
          if (isLs) lsUpdate(noteId, newText);
          else throw new Error('cannot edit backend note while backend is offline');
        } else {
          await apiUpdate(noteId, newText);
        }
        aside.innerHTML = '';
        aside.textContent = newText;
        aside.classList.remove('edit');
      } catch (err) {
        alert('Save failed: ' + err.message);
        saveBtn.disabled = false;
      }
    });

    deleteBtn.addEventListener('click', async () => {
      if (!confirm('Delete this note?')) return;
      deleteBtn.disabled = true;
      try {
        const isLs = aside.dataset.source === 'ls';
        if (isLs || !backendAvailable) {
          if (isLs) lsDelete(noteId);
          else throw new Error('cannot delete backend note while backend is offline');
        } else {
          await apiDelete(noteId);
        }
        aside.remove();
        repositionAddButtons();
      } catch (err) {
        alert('Delete failed: ' + err.message);
        deleteBtn.disabled = false;
      }
    });
  }

  // ---------- Server banner (index.html) ----------

  function wireServerBanner() {
    const banner = document.getElementById('server-banner');
    if (!banner) return;
    const msg = document.getElementById('server-banner-msg');
    const cmd = banner.querySelector('.server-banner__cmd');
    if (mode === 'be') {
      msg.textContent = 'Backend running at ' + location.origin + '. New notes save straight to markdown.';
      banner.classList.remove('callout--info');
      banner.classList.add('callout--ok');
      if (cmd) cmd.style.display = 'none';
    } else if (mode === 'ls') {
      msg.textContent = 'Backend not running. Notes save to your browser only. Start the backend to write notes back to markdown:';
    } else {
      msg.textContent = 'Read-only deployment. Notes save to your browser only. To write notes back to your markdown source, clone the repo and run the backend locally:';
    }
    banner.hidden = false;
    banner.querySelectorAll('[data-copy-target]').forEach(btn => {
      btn.addEventListener('click', async () => {
        const target = document.getElementById(btn.dataset.copyTarget);
        if (!target) return;
        try {
          await navigator.clipboard.writeText(target.textContent);
          const old = btn.textContent;
          btn.textContent = 'copied';
          setTimeout(() => { btn.textContent = old; }, 1200);
        } catch {
          const range = document.createRange();
          range.selectNodeContents(target);
          const sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
        }
      });
    });
  }

  // ---------- Mode pill (non-index pages) ----------

  function wireModePill() {
    if (document.getElementById('server-banner')) return;
    const pill = document.createElement('div');
    pill.className = 'mode-pill mode-pill--' + mode;
    pill.textContent = mode === 'be' ? 'BE live' :
                       mode === 'ls' ? 'BE off' :
                       'view-only';
    pill.title = mode === 'be' ? 'Backend running. Notes save to markdown.' :
                 mode === 'ls' ? 'Backend not running. Notes save to your browser only. Run python3 scripts/notes_server.py for markdown writeback.' :
                 'Read-only deployment. Notes save to your browser only.';
    document.body.appendChild(pill);
  }

  // ---------- Import / Export ----------

  function escapeAttrsText(text) {
    return text.replace(/\\/g, '\\\\').replace(/\*/g, '\\*').replace(/\{/g, '\\{').replace(/\}/g, '\\}');
  }

  function unescapeAttrsText(text) {
    let out = '', i = 0;
    while (i < text.length) {
      const c = text[i];
      if (c === '\\' && i + 1 < text.length) {
        const n = text[i + 1];
        if (n === '\\' || n === '*' || n === '{' || n === '}') { out += n; i += 2; continue; }
      }
      out += c; i++;
    }
    return out;
  }

  function exportLsAsMarkdown() {
    const state = lsLoad();
    const anchors = Object.keys(state).sort();
    const lines = [
      '# Daily page user notes (browser export)',
      '',
      'Exported ' + new Date().toISOString() + ' from ' + location.origin,
      'Format mirrors daily_notes.md so notes_server.py can read it back.',
      '',
    ];
    for (const anchor of anchors) {
      lines.push('<!-- user-notes:' + anchor + ' -->');
      let n = 0;
      for (const note of state[anchor]) {
        n++;
        const newId = 'note-' + anchor + '-' + n;
        lines.push('*' + escapeAttrsText(note.text) + '*{.user-note #' + newId + '}');
      }
      lines.push('<!-- /user-notes:' + anchor + ' -->');
      lines.push('');
    }
    return lines.join('\n');
  }

  function downloadMarkdown(text, filename) {
    const blob = new Blob([text], { type: 'text/markdown' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function parseImportMarkdown(text) {
    const lines = text.split(/\r?\n/);
    const openRe = /^\s*<!--\s*user-notes:([a-z0-9-]+)\s*-->\s*$/;
    const closeRe = /^\s*<!--\s*\/user-notes:([a-z0-9-]+)\s*-->\s*$/;
    const noteRe = /^\*(.*)\*\{\.user-note\s+#(note-[a-z0-9-]+-\d+)\}\s*$/;
    const result = {};
    let current = null;
    for (const line of lines) {
      const o = openRe.exec(line);
      if (o) { current = o[1]; result[current] = result[current] || []; continue; }
      const c = closeRe.exec(line);
      if (c) { current = null; continue; }
      if (!current) continue;
      const m = noteRe.exec(line);
      if (m) result[current].push({ text: unescapeAttrsText(m[1]), note_id: m[2] });
    }
    return result;
  }

  async function importMarkdown(text) {
    const parsed = parseImportMarkdown(text);
    let imported = 0;
    let skipped = 0;
    if (backendAvailable) {
      for (const anchor of Object.keys(parsed)) {
        for (const note of parsed[anchor]) {
          try { await apiAdd(anchor, note.text); imported++; }
          catch (e) { console.warn('skipped', anchor, e); skipped++; }
        }
      }
      alert('Imported ' + imported + ' notes to backend' +
        (skipped ? ' (' + skipped + ' skipped)' : '') +
        '. Reload to see them.');
    } else {
      const state = lsLoad();
      for (const anchor of Object.keys(parsed)) {
        state[anchor] = state[anchor] || [];
        for (const note of parsed[anchor]) {
          const newId = 'note-ls-' + anchor + '-' + Date.now().toString(36) + '-' + imported;
          state[anchor].push({ note_id: newId, text: note.text, ts: Date.now() });
          imported++;
        }
      }
      lsSave(state);
      alert('Imported ' + imported + ' notes to browser. Reload to see them.');
    }
  }

  function wireNotesTools() {
    const exportBtn = document.getElementById('notes-export');
    const importInput = document.getElementById('notes-import');
    const clearBtn = document.getElementById('notes-clear-ls');
    const summary = document.getElementById('notes-tools-summary');
    if (!exportBtn || !importInput || !summary) return;
    const cnt = lsCount();
    summary.textContent = 'You have ' + cnt + ' notes in your browser. ' + (
      mode === 'be' ? 'Backend is running; new notes save straight to markdown.' :
      mode === 'ls' ? 'Backend is not running; new notes save to your browser only.' :
      'View-only deployment; new notes save to your browser only.'
    );
    if (cnt > 0) { exportBtn.disabled = false; clearBtn.disabled = false; }
    exportBtn.addEventListener('click', () => {
      const text = exportLsAsMarkdown();
      const today = new Date().toISOString().slice(0, 10);
      downloadMarkdown(text, 'daily_notes_export_' + today + '.md');
    });
    importInput.addEventListener('change', async (e) => {
      const file = e.target.files[0];
      if (!file) return;
      try {
        const text = await file.text();
        await importMarkdown(text);
      } catch (err) {
        alert('Import failed: ' + err.message);
      } finally {
        importInput.value = '';
      }
    });
    clearBtn.addEventListener('click', () => {
      if (!confirm('Clear all browser notes? This cannot be undone. Export first if you want a backup.')) return;
      localStorage.removeItem(LS_KEY);
      alert('Cleared. Reload to confirm.');
    });
  }

  // ---------- Init ----------

  async function init() {
    backendAvailable = await probeBackend();
    if (backendAvailable) mode = 'be';
    else if (['localhost', '127.0.0.1'].includes(location.hostname) || location.protocol === 'file:') mode = 'ls';
    else mode = 'pages';

    renderLsNotes();
    wireAddButtons();
    repositionAddButtons();
    wireNoteActions();
    wireServerBanner();
    wireModePill();
    wireNotesTools();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
