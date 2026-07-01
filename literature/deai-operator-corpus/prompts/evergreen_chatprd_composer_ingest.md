# Evergreen Prompt: ChatPRD Research Document → Cursor Composer Ingest

> **Scholia deai-operator-corpus:** use `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/prompts/CORPUS_SYNTH_CONTRACT.md` (v0.2 semantic preservation protocol) for ingest/refine/digest; research scratchpad at `/Users/dubs/Projects/scholia.skill/literature/deai-operator-corpus/localonly/research/opus46-synthesis-scratchpad.md`. This evergreen doc is for general palamedes→Composer handoff only.

## Purpose

Transform epistemically rigorous, long-form research documents produced by ChatPRD (palamedes template) into a format that Cursor's Auto mode can reliably consume and act on.

Auto selects from a model pool that includes Composer 2.5 (Cursor's RL-trained coding model built on Moonshot's Kimi K2.5) and other models, optimizing for cost, speed, and reliability. The models in this pool are optimized for code-task execution, not general analytical reasoning. This prompt compensates for that asymmetry.

---

## Section 1: Receiver Model Constraints

Cursor Auto selects models "balancing intelligence, cost efficiency, and reliability" from a dedicated usage pool. \[Source: Cursor Docs — Models and Pricing, cursor.com/docs/models-and-pricing, verified 2026-06-27\]

Composer 2.5, the most common Auto selection, is built on Moonshot's Kimi K2.5 base with Cursor's proprietary RL post-training, optimized for "long-horizon agentic coding tasks" including file edits, terminal operations, and tool calls. \[Source: Cursor Blog — Introducing Composer 2.5, cursor.com/blog/composer-2-5, verified 2026-06-27\]

| Constraint | Evidence | Implication for document design |
| --- | --- | --- |
| Coding-optimized, not general-reasoning | Cursor Blog: "trained to be highly capable for agentic coding." DataCamp: "Not suited for broad, high-context, long-horizon reasoning tasks or wide-context planning." | Decision logic must arrive pre-resolved. The model should execute directives, not weigh evidence. |
| Context degrades with length | Anthropic: "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases." Chroma research confirms non-linear degradation. EMNLP 2025 finding: 13.9-85% performance drops from length alone. | Keep research context documents short. Front-load critical constraints. |
| Auto routes down on thin context | AI Tools Guidebook: "Auto optimizes for intelligence, cost, and reliability using only the signals it can see (prompt length, attached files, keywords)." Short/vague prompts trigger cheaper models. | Structured, explicit documents with clear intent signals reduce misrouting risk. |
| Compaction is lossy | Cursor Blog on self-summarization: compaction "can cause the model to forget critical information from the context." Amp (Sourcegraph) described compaction as "lossy" — "what's in the context window gets replaced with a summary." | Anchor values that must survive compaction in explicit, structured formats (YAML blocks, named constants). |
| Cursor retrieves context selectively | Cursor Docs: auto-context from open tabs, indexed codebase, and chat history. Community guidance converges on 2-5 files per task for signal quality. | Design sections to be independently parseable. Cross-references that depend on other sections being co-loaded will fail. |

---

## Section 2: Architectural Principles

### 2.1 Concept Distillation: Strong Model Output → Weak Model Input

Concept Distillation (Boateng et al., NAACL Industry 2025, aclanthology.org/2025.naacl-industry.52) demonstrates that when a strong model distills explicit rules and concepts into a prompt, weak models improve substantially on complex tasks. Empirical results: Phi-3-mini-3.8B accuracy on HumanEval rose from 0.48 to 0.82 (+34%); Mistral-7B on Multi-Arith rose from 0.41 to 0.67 (+26%). \[verified — Gate A: 200 OK, Gate B: Tables 1 and 2 in paper confirm exact figures\]

Design implication: ChatPRD's palamedes output is the strong-model artifact. The preprocessing prompt distills its analytical conclusions into explicit, imperative rules the receiving model can follow without re-deriving the reasoning. This is concept distillation applied to the research-to-implementation handoff.

Failure mode: Distilled rules may be over-specific to the base case, missing edge conditions the original analysis covered. Mitigation: preserve contrarian findings as labeled ANTI-PATTERN blocks.

### 2.2 Intent-Preserving Artifacts Over Compressed Summaries

The preprocessing output must be an intent-preserving artifact — not a summary of what was researched, but a specification of what to build and what constraints to obey.

The industry has not converged on whether handoff artifacts or auto-compaction is superior. Sourcegraph's Amp agent moved from compaction to explicit handoffs (ampcode.com/news/handoff), then reversed back to auto-compaction (ampcode.com/news/neo, Quote: "So handoff is out. Compaction is in."). This oscillation indicates neither approach dominates universally. \[verified — both Amp pages fetched, 200 OK, quotes confirmed\]

For the ChatPRD→Cursor use case specifically, the artifact approach is preferable because: (a) the handoff crosses system boundaries (ChatPRD → file system → Cursor), so there is no shared conversation history to compact; (b) Anthropic's context engineering guidance recommends curating "the smallest possible set of high-signal tokens." \[verified — Anthropic, anthropic.com/engineering/effective-context-engineering-for-ai-agents, quote confirmed\]

Failure mode: Intent-preserving artifacts discard the reasoning chain, making it impossible for the receiving model to adapt if conditions differ from those assumed.

### 2.3 Section Independence

Cursor's auto-context system pulls from open tabs, indexed codebase, and chat history. There is no guarantee that all sections of a multi-section document will be co-loaded. Practitioner guidance consistently recommends scoping to 2-5 files per task. \[inferred — convergent practitioner sources: vibecoder.me (3-5 files), developertoolkit.ai (2-3 files), web2md.org (4-5 files). No Cursor-official number exists.\]

Design implication: Every section must be self-contained, restating critical assumptions at the point of use. Redundancy is deliberate.

Failure mode: Over-scoping section independence creates excessive token overhead from repeated context blocks.

### 2.4 Explicit Reasoning Scaffolding

Structured, schema-driven prompts improve reasoning in instruction-tuned models that lack extended thinking. The STROT framework (arxiv 2505.01636) demonstrates explicit task planning via schema-guided context improves robustness in high-variance tasks. "Table as Thought" (EMNLP Findings 2025) shows that predefined schemas outperform free-form chain-of-thought for constrained models. "Fast Thinking with Structured Prompts" (RANLP 2025) reports up to 10% improvement from graph-based reasoning structures even in 0.5B-parameter models. \[inferred — papers exist and are real; extrapolation to Cursor's Auto pool models is reasonable but untested on those specific models\]

Design implication: Replace analytical prose with decision tables, constraint lists, and IF/THEN rules.

Failure mode: Over-structuring may constrain a capable model's ability to exercise judgment when judgment is actually needed.

---

## Section 3: The Preprocessing Prompt

Place this in a ChatPRD thread after generating a palamedes-template research document.

### Usage

1. Complete your research synthesis in ChatPRD using the palamedes template
2. Paste the prompt below into the same thread
3. Save output as docs/ai-context/{topic}.md in your project
4. Reference in Cursor with @docs/ai-context/{topic}.md

### The Prompt

```
TASK: Transform the research document above into a Cursor Composer ingest
artifact. The receiving model is a coding-optimized LLM selected by
Cursor's Auto mode. It excels at file operations and tool use. It does
not excel at weighing evidence or reasoning through ambiguity. Design the
output so every section can be understood in isolation.

TRANSFORMATION RULES (apply in order):

1. STRIP EPISTEMICS — Remove confidence scores, calibration gates,
   source tier annotations, and methodology discussion. The receiving
   model cannot weigh evidence. Convert every analytical finding into
   a resolved directive.

2. DECISIONS → IMPERATIVES — For every "the evidence suggests X,"
   produce "DIRECTIVE: X. Do not implement alternatives unless
   explicitly instructed."

3. FLATTEN NUANCE — Where the research presents bull/bear/base cases,
   select the base case as the default. Preserve alternatives only as
   labeled exceptions:
   "EXCEPTION (bull case): if {condition}, then {behavior}."

4. SECTION INDEPENDENCE — Each output section must begin with:

   TOPIC: {what this section covers}
   DEPENDS-ON: {critical assumptions, restated here}
   CONSTRAINTS: {hard rules within this section}

5. ANCHOR CRITICAL VALUES — Numbers, thresholds, percentages, dates,
   and named entities that affect implementation must appear in a
   YAML-style key-value block at the section top:

   market_size_tam: $4.2B
   growth_rate_cagr: 12.3%
   target_segment: SMB (10-200 employees)
   pricing_floor: $29/mo

6. REPLACE TABLES WITH DECISION MATRICES — Comparison tables become
   decision matrices with a RECOMMENDED column and explicit IF/THEN
   selection logic below the table.

7. SPLIT BY THEME IF LONG — If the transformed output exceeds \~2000
   tokens, split into independently parseable files:
   - {topic}-market.md (sizing, competitive landscape)
   - {topic}-technical.md (architecture, stack constraints)
   - {topic}-execution.md (timeline, milestones, resources)
   - {topic}-risks.md (failure modes, mitigations)
   Rationale: context quality degrades with length; multiple focused
   files referenced selectively outperform one large file.
   Limit to 3-4 files per prompt when referencing in Cursor.

8. USE IMPLEMENTATION-ORIENTED HEADERS — Begin headers with verbs:
   "Implement," "Configure," "Validate," "Avoid," "Enforce."
   Avoid analytical headers like "Analysis of" or "Overview."
   Rationale: clear intent signals in the document help both the
   human operator and the model understand the expected action.

9. PRESERVE CONTRARIAN FINDINGS — Encode disconfirming evidence and
   failure modes as ANTI-PATTERNS:

   ANTI-PATTERN: Do not assume organic acquisition below $50 CAC.
   Evidence base: 73% of comparable startups exceeded $120 CAC
   in first 18 months.

10. EMIT METADATA — Prepend with:
    ---
    source: chatprd-palamedes
    research_date: {date}
    confidence_floor: {lowest confidence from source document}
    review_by: {research_date + 90 days}
    stale_after: {research_date + 180 days}
    split_files: {list if split}
    ---

OUTPUT FORMAT: Clean Markdown. Fenced code blocks only for YAML value
anchors and anti-pattern blocks. H2 max heading depth. Bullet lists
over prose. No bold/italic decorators in running text.

```

---

## Section 4: Companion MDC Rule

Place as .cursor/rules/research-context.mdc in your project. This uses glob-triggered activation per Cursor's MDC rule system. \[Source: Cursor Docs — Rules, cursor.com/docs/rules, verified 2026-06-27\]

```yaml
---
description: "Governs behavior when ChatPRD research context documents are referenced"
globs:
  - "docs/ai-context/\*\*/\*.md"
alwaysApply: false
---

```

Rule body:

```
When files matching docs/ai-context/\*\*/\*.md are in context:

1. Treat DIRECTIVE lines as hard constraints. Do not deviate without
   explicit user override in the current prompt.

2. Treat ANTI-PATTERN blocks as prohibitions. If your planned
   implementation matches an anti-pattern, halt and report the
   conflict before proceeding.

3. Use YAML key-value anchors as source-of-truth for any referenced
   values. Do not infer or round these values.

4. If a research context file contains a stale_after date that has
   passed, warn the user before applying its directives.

5. When multiple research files conflict:
   - technical.md overrides market.md on architecture decisions
   - risks.md overrides execution.md on timeline assumptions
   - User's current prompt overrides all research context

6. Do not summarize or paraphrase research context. Quote specific
   directives when referencing them.

```

---

## Section 5: Workflow Integration

### File structure

```
project-root/
  docs/
    ai-context/
      {topic}-market.md
      {topic}-technical.md
      {topic}-execution.md
      {topic}-risks.md
    ai-context/archive/
  .cursor/
    rules/
      research-context.mdc

```

### Referencing in Composer

* Single file: @docs/ai-context/{topic}-technical.md
* Selective pack: @docs/ai-context/{topic}-market.md + @docs/ai-context/{topic}-technical.md (limit to 3-4 files per prompt)
* Task prompt pattern: "Using @docs/ai-context/fintech-market.md as constraints, implement the pricing module per the directives in that file."

### Model selection guidance

* For routine implementation against research directives: Auto mode is adequate
* For cross-file refactors or novel architecture: manually select a stronger model (Sonnet 4.6+) per Cursor community best practice
* For high-stakes sessions: pin model in workspace settings via cursor.chat.defaultModel

### Refresh cycle

* Research documents carry review_by and stale_after dates
* At review_by: re-run the palamedes research prompt with updated sources
* At stale_after: move to docs/ai-context/archive/ and regenerate
* The MDC rule warns on stale documents

---

## Section 6: Evidence Base

| Technique | Problem it solves | Evidence | Claim status |
| --- | --- | --- | --- |
| Concept distillation (strong to weak) | Coding-optimized models lack analytical reasoning to derive implementation rules from research prose | Phi-3-mini +34%, Mistral-7B +26% on benchmarks (Boateng et al. NAACL 2025) | verified |
| Intent-preserving artifacts | Cross-system handoff (ChatPRD to file system to Cursor) has no shared history to compact | Anthropic: curate "smallest possible set of high-signal tokens"; Amp oscillation confirms no universal winner between handoff and compaction | verified (principle); inferred (application) |
| Section independence | Cursor loads context selectively; co-loading all sections is not guaranteed | Convergent practitioner guidance: 2-5 files per task. Cursor auto-context docs describe selective retrieval. | inferred |
| Structured scaffolding over prose | Non-frontier models produce better outputs with schema-driven, pre-resolved structures | STROT (arxiv 2505.01636), Table as Thought (EMNLP 2025), Fast Thinking (RANLP 2025) | inferred |
| Value anchoring in YAML blocks | Compaction loses information; anchored values in structured format are more salient than inline prose | Cursor Blog: compaction "can cause the model to forget critical information." General LLM recall research. | inferred |
| Anti-pattern encoding | Concept Distillation identifies that distilling failure-case concepts is critical to the method | NAACL 2025 paper Deduction/Verification phase explicitly mines failure cases | verified |
| Context length discipline | LLM performance degrades with input length regardless of retrieval quality | Chroma context rot research; EMNLP 2025 (13.9-85% drops); arxiv 2601.15300 (collapse at 40-50% of max context) | verified |

---

## Section 7: Known Limitations and Risks

* This preprocessing is lossy by design. Epistemic nuance from the palamedes output is deliberately destroyed. Always retain the original ChatPRD document as the source of truth.
* The split threshold (\~2000 tokens per file) is a practitioner heuristic, not an empirically validated optimum for Cursor's specific models. Adjust based on observed behavior.
* The MDC rule cannot enforce behavioral guarantees. Auto-pool models may ignore directives. For high-stakes sessions, pin to a stronger model.
* Auto mode routing heuristics are undisclosed. Claims about what improves routing (header format, prompt length, verb choice) are practitioner inference, not Cursor-documented behavior.
* The Concept Distillation evidence comes from HumanEval and Multi-Arith benchmarks (code generation and math reasoning). Transfer to business research context is assumed, not tested.
* This prompt assumes the palamedes template output structure. Other ChatPRD templates require adapted transformation rules.

---

## Appendix: Adversarial Review — Kill List

Claims falsified, downgraded, or excluded during the adversarial review pass.

| Claim | Verdict | Detail |
| --- | --- | --- |
| "Auto routes to Composer 2.5" | OVERSTATED | Auto selects from a pool. Composer 2.5 is one option, not guaranteed. Cursor Docs: "Auto allows Cursor to select models that balance intelligence, cost efficiency, and reliability." Rewritten to reflect pool-based selection. |
| "Handoff artifacts outperform compaction" (citing Sourcegraph) | WRONG | Sourcegraph Amp first retired compaction for handoffs, then reversed: "So handoff is out. Compaction is in." (ampcode.com/news/neo). The cited GitHub source returned 404. Replaced with intent-preserving artifact framing specific to the cross-system use case. |
| "Attention degrades past \~10k tokens" (citing arxiv 2411.07858) | WRONG | The cited paper (Zhang et al. 2024) studies Verbosity Compensation behavior, not attention degradation thresholds. It does not contain the claimed 10k threshold. Replaced with actual context degradation evidence from Chroma, EMNLP 2025, and arxiv 2601.15300. |
| "Compaction drops numbers, exact phrasing" | OVERSTATED | Cursor Blog says compaction "can cause the model to forget critical information" — general, not specific to numbers. Rewritten as general information loss. |
| "Action-verb headers improve Auto routing" | UNTESTED | No primary source confirms header format affects routing. Retained as practitioner advice with explicit uncertainty label. |
| Composer 2.5 "1.04T params, 32B active" | OVERSTATED | These figures appear in third-party analysis (digitalapplied.com), not in Cursor's official publications. Removed specific parameter counts. |
