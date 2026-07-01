# Glossary — CS + AI Foundation (2-week program)

| Term | Definition | Source anchor |
|------|------------|---------------|
| **AI engineering** | Building applications on top of readily available foundation models (model-as-a-service). | AIE ch1 |
| **Agent** | System that perceives an environment and acts via tools; RAG and SQL pipelines count. | AIE ch6 |
| **AI-as-judge** | Using an LLM to score another model's outputs; watch position/verbosity/self-preference bias. | AIE ch3 |
| **Autoregressive LM** | Predicts next token given prior tokens; default "language model" in AIE. | AIE ch1–2 |
| **BFS** | Breadth-first search; fewest **hops** on unweighted graphs. | Grokking ch6 |
| **Big O** | Worst-case growth rate as input size increases; not wall-clock speed. | Grokking ch1 |
| **BM25** | Length-normalized term-frequency IDF variant for lexical retrieval. | AIE ch6 |
| **Bradley–Terry** | Pairwise comparison model underlying Elo-style rankings. | AIE ch3 |
| **Change amplification** | Small change forces edits in many places. | Ousterhout ch2 |
| **Chinchilla** | Compute-optimal scaling: model size and data should scale together. | AIE ch2 |
| **Cognitive load** | How much a reader must hold in mind to follow code. | Ousterhout ch2 |
| **Compound accuracy** | Multi-step pipelines multiply per-step error rates. | AIE ch6 |
| **Context (LLM)** | Tokens visible to the model for one request; "per-query feature engineering." | AIE ch6 |
| **Crawl-Walk-Run** | Human-in-loop automation ramp (Microsoft framing in AIE). | AIE ch1 |
| **Deep module** | Large functionality behind a simple interface. | Ousterhout ch4 |
| **Dijkstra** | Shortest **weighted** path with non-negative edges. | Grokking ch9 |
| **EDD** | Evaluation-driven development. | AIE ch4 |
| **Embedding** | Dense vector representation of text for semantic similarity. | AIE ch3, ch6 |
| **Foundation model** | Large pretrained model others build upon (prompt/RAG/finetune). | AIE ch1 |
| **Functional correctness** | pass@k style: does generated code pass tests? | AIE ch3 |
| **Generation effect** | Self-generated answers remembered better than read-only. | Pedagogy D |
| **Greedy algorithm** | Locally optimal choice each step; not always globally optimal. | Grokking ch10 |
| **Hallucination** | Plausible but false model output. | AIE ch2 |
| **Hash table** | Key→bucket mapping; O(1) average, O(n) worst with collisions. | Grokking ch5 |
| **Hybrid search** | Combine lexical (BM25) + vector retrieval; often RRF fusion. | AIE ch6 |
| **ICL** | In-context learning; few-shot examples in the prompt. | AIE ch5 |
| **Information hiding** | Design decisions in implementation, not interface (Parnas). | Ousterhout ch5 |
| **Information leakage** | Interface exposes internals callers shouldn't need. | Ousterhout ch5 |
| **KV cache** | Stored attention keys/values to speed autoregressive decode. | AIE ch9 |
| **k-NN** | k-nearest neighbors; classify/regress by nearby training points. | Grokking ch12 |
| **LLM** | Large language model; scale tracked by parameters + data. | AIE ch1 |
| **LoRA** | Low-rank adaptation; PEFT method for finetuning. | AIE ch7 |
| **Method of loci** | Memory palace; spatial anchors for ordered recall. | Pedagogy D |
| **NP-complete** | Problems with no known fast exact solution; approximation OK. | Grokking ch10 |
| **Pass-through method** | Method that only delegates; shallow layer smell. | Ousterhout ch7 |
| **Perplexity** | LM metric; lower is better on training distribution; weak post-SFT proxy. | AIE ch3 |
| **Prompt injection** | Adversarial instructions embedded in untrusted content. | AIE ch5 |
| **QLoRA** | Quantized LoRA; finetune with reduced memory. | AIE ch7 |
| **RAG** | Retrieval-augmented generation; retrieve then generate. | AIE ch6 |
| **ReAct** | Reasoning + acting interleaved in agent loops. | AIE ch6 |
| **Recursion** | Base case + smaller subproblem that calls itself. | Grokking ch3 |
| **Retrieval practice** | Testing yourself beats re-reading for retention. | Pedagogy D |
| **RLHF** | Reinforcement learning from human feedback; preference tuning. | AIE ch2 |
| **RRF** | Reciprocal rank fusion for merging ranked lists. | AIE ch6 |
| **Self-supervision** | Labels inferred from raw text (next-token prediction). | AIE ch1 |
| **Shallow module** | Small benefit, complex interface; classitis symptom. | Ousterhout ch4 |
| **Spaced repetition** | Review on expanding intervals; Anki implements this. | Pedagogy D |
| **Strategic programming** | Invest continuously in design vs tactical patch-and-ship. | Ousterhout ch3 |
| **Token** | Subword unit models read/write; not always whole words. | AIE ch1 |
| **Transfer-appropriate processing** | Practice in the form you'll be tested in. | Pedagogy D |
| **TTFT** | Time to first token; latency metric for streaming APIs. | AIE ch9 |
| **TPOT** | Time per output token during decode. | AIE ch9 |
| **Unknown unknowns** | Surprises you didn't know to look for; worst complexity symptom. | Ousterhout ch2 |
