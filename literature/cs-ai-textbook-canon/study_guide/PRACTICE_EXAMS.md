# Practice Checks — CS + AI Foundation

**Format:** Open-book against your EPUB/PDF + study guide. Time-boxed retrieval practice (no AI assistant during the mock).

---

## Mock A — Track A (Day 5) · 90 minutes

### Section 1: Algorithms (45 min)

1. **Binary search precondition.** State the requirement on the input list. Walk through finding a name in a 240,000-entry phone book: how many steps worst case? Show the halving logic in your own words.  
   *Source: Grokking ch1 — "you can only perform binary searches on sorted lists."*

2. **Big O trap.** Bob claims binary search is "15 times faster" at 1B items because 1B/240k ≈ 4000 and log scales slowly. Why is that reasoning wrong? What does log₂(1B) ≈ 32 actually mean?  
   *Source: Grokking ch1 NASA/Bob anecdote.*

3. **Arrays vs linked lists.** When is insert-in-middle cheaper? When is random access cheaper? Tie to one real API design choice.  
   *Source: Grokking ch2.*

4. **Recursion.** Write base case + recursive case for summing a list. What structure records unfinished calls?  
   *Source: Grokking ch3.*

5. **Quicksort vs merge sort.** When might quicksort degrade? What does "random pivot" buy you in practice vs worst case?  
   *Source: Grokking ch4 — contested average-case claim flagged in ingest.*

6. **Hash tables.** Why does the author call O(1) lookup a "white lie"? What is load factor?  
   *Source: Grokking ch5.*

7. **BFS vs Dijkstra.** One uses edge count; one uses total weight. Give a 3-node counterexample where they pick different paths.  
   *Source: Grokking ch6, ch9.*

8. **Greedy failure.** Why does value-greedy fail 0/1 knapsack? What chapter introduces the fix?  
   *Source: Grokking ch10–11.*

### Section 2: Software design (45 min)

9. **Define complexity** in Ousterhout's practical sense. List three symptoms and two causes.  
   *Quote anchor: "anything that makes software harder to understand and modify."*

10. **Deep vs shallow module.** Contrast Unix `open()` with Java's three-stream file open. Which is deeper and why?

11. **Information leakage.** Give one HTTP/course-project example from ch5. How do you fix leakage vs back-door leakage?

12. **Pull complexity down.** Why is "expose every config parameter" often wrong? Use the retry-interval example.

13. **Clean Code debate.** Summarize Ousterhout's position on small functions (ch9). When is splitting harmful?

14. **From Appendix principles (ch22).** Pick any **3 of 16** design principles and explain each in one sentence without looking, then verify.

**Scoring guide:** 70%+ = ready for week 2. Misses go to Appendix B miss patterns in the study guide.

---

## Mock B — Track B (Day 10) · 120 minutes

### Section 1: Foundations & models (30 min)

1. Why does Huyen call post-2020 AI **"scale"**? Name two consequences of scaling.  
   *Quote: "If I could use only one word to describe AI post-2020, it'd be scale."*

2. Define **foundation model** and three adaptation strategies named in ch1.

3. **Self-supervision** vs manual labels: why did it unlock LLM scaling?

4. Name three ways AI engineering differs from traditional ML engineering (ch1 table).

5. **Sampling:** what do temperature and top-p control? Why does that create inconsistency?

### Section 2: Evaluation (35 min)

6. Why is FM evaluation harder than classic ML? List **four** structural difficulties (ch3).

7. When is perplexity useful vs misleading?

8. **AI-as-judge:** name three biases and one mitigation.

9. **EDD four buckets** from ch4 (domain, generation, instruction-following, cost/latency).

10. Why should you distrust public leaderboards for your product decision?

### Section 3: Context & adaptation (35 min)

11. **RAG vs long context:** give two reasons RAG persists even as context windows grow.

12. **Compound accuracy:** if each agent step is 95% accurate, what is 10-step success rate?

13. **Finetune vs RAG:** "facts vs form" heuristic (Ovadia). Apply to a customer-support tone scenario.

14. **Prompt injection:** indirect vs direct; one defensive pattern from ch5.

15. **Dataset engineering:** name three data-quality dimensions from ch8.

### Section 4: Production (20 min)

16. **TTFT vs TPOT** — which matters more for chat UX vs batch?

17. **Architecture stack (ch10):** order these layers: guardrails, semantic cache, router, raw context.

18. **Observability:** metrics vs logs vs traces — one example each for an LLM app.

19. **Feedback loops:** why can RLHF-style training increase sycophancy?

20. **MDCalc-pattern (no employer claims):** which two ch10 patterns matter for regulated/clinical-adjacent deployments? (guardrails, human escalation, PHI in cache — pick and justify.)

**Scoring guide:** 75%+ = wave-1 foundation complete. Review ingests for missed chapters.

---

## Daily retrieval drills (5–10 min each evening)

| Day | Drill |
|-----|-------|
| D1 | Recite binary search steps; define change amplification |
| D2 | Write quicksort partition pseudocode; define tactical vs strategic |
| D3 | Hash collision example; define information hiding |
| D4 | Dijkstra 4 steps; define pass-through method |
| D5 | One greedy success + one failure; recite 3 red flags from ch22 |
| D6 | Draw three-layer AI stack from memory |
| D7 | List eval biases; one custom eval metric you'd ship |
| D8 | Sketch RAG pipeline boxes; define ReAct loop |
| D9 | LoRA in one sentence; define "decide what matters" |
| D10 | Walk memory palace once; TTFT/TPOT definitions |
