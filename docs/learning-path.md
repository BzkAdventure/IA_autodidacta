# Learning path

Write these programs in order, in Python 3. Keep each one. Later programs import the earlier ones.

Start the next program when the current one runs and you can explain what it is doing.

**Where you are.** Programs 1–4 are skipped. Current work is program 5 (tests) and program 6 (maze solver). Continue from program 7.

**Size.** Small: one idea, one file. Medium: a few files, and the edge cases are part of the work. Large: several parts that work only as a system.

**Tools.** Programs 1–15 use the Python standard library. NumPy starts at program 16, when the work is arrays. PyTorch starts at program 21, when the work is automatic gradients. A local open-weight instruction model starts at program 31, when the work is the harness around a model that already follows instructions. Each of those programs says why.

1. [Programs, from zero](#1-programs-from-zero)
2. [Math, through programs](#2-math-through-programs)
3. [Learning from examples](#3-learning-from-examples)
4. [Neural nets, derived](#4-neural-nets-derived)
5. [Language models](#5-language-models)
6. [A real training run](#6-a-real-training-run)
7. [Post-training](#7-post-training)
8. [Scale and matched serving](#8-scale-and-matched-serving)
9. [Agents](#9-agents)
10. [Frontier systems (October 2026)](#10-frontier-systems-october-2026)

## 1. Programs, from zero

The machine runs what you write: data, control, files, and a way to prove a program still works.

### 1. Number guessing — small

- **Build:** The program picks an integer, reads guesses, and says higher or lower until the guess is right. It prints how many guesses that took.
- **Teaches:** Running a Python file, variables, input, branches, and a loop that stops.
- **Already able to:** Install Python 3 and open a terminal.

### 2. Word counter — small

- **Build:** Read a text file. Count words with a dictionary. Print the ten most common, highest count first.
- **Teaches:** Strings, lists, dictionaries, and a loop over data.
- **Already able to:** Run a program that branches and loops.

### 3. Unit converter — small

- **Build:** Each conversion is a function. A menu reads a choice and calls one. An unknown choice asks again.
- **Teaches:** Functions, arguments, and return values.
- **Already able to:** Store values and loop over input.

### 4. Ledger — small

- **Build:** Append dated lines of an amount and a note to a file. A command prints every line and the total. A non-numeric amount is refused and the file is left unchanged.
- **Teaches:** Files, parsing a line, and data that outlives the run.
- **Already able to:** Write functions and format strings.

### 5. Tests — small

- **Build:** A second file of assertions for the converter and the ledger: empty input, a bad amount, and a missing file. A passing run prints nothing. A failing run prints a traceback that names the assertion.
- **Teaches:** Assertions, edge cases, and reading an error.
- **Already able to:** Write functions and read a file.

### 6. Maze solver — small

- **Build:** A maze in a text file. Breadth-first search, with a queue and a visited set, prints a shortest path from start to end.
- **Teaches:** Search that remembers where it has been. You will reuse this search when a later program plans inside a simulator.
- **Already able to:** Read a file, use a dictionary, and write a test.

## 2. Math, through programs

Counting, chance, vectors, matrices, and a derivative, each as a program you run.

### 7. Column summary — small

- **Build:** Write a small CSV by hand. Load it with your own parser. For one column print the count, mean, median, min, and max.
- **Teaches:** Tables, and a summary that says more than a single average.
- **Already able to:** Read files, loop, and test edge cases, including an empty column.

### 8. Coin and dice — small

- **Build:** Simulate a coin and a die for many throws. Print each face's frequency. Then price a bet: print the average payout over the throws, and the payout you would expect from the probabilities.
- **Teaches:** Probability as a long-run frequency, and expectation as a weighted average of outcomes.
- **Already able to:** Loop, count with a dictionary, and compute a mean.

### 9. Vectors — small

- **Build:** Points in the plane as lists. Compute distance, a dot product, and the nearest point in a set to a query point.
- **Teaches:** A vector, length, and similarity as a dot product.
- **Already able to:** Write functions over lists and compute a mean.

### 10. Matrix transforms — medium

- **Build:** A shape as a list of points. Matrices that rotate and scale it, multiplied with nested loops. Print the shape before and after as a text grid.
- **Teaches:** Matrix multiply and the shape of the result (which dimensions must match).
- **Already able to:** Compute a dot product and place points on a grid.

### 11. Line fit — medium

- **Build:** Noisy points around a straight line. Start from a guessed slope and intercept. Repeatedly nudge each one in the direction that cuts the mean squared error. Print the error every step. Run it again with a tiny step and a huge step.
- **Teaches:** A loss, a partial derivative as "which nudge helps," and a step size that either crawls or diverges.
- **Already able to:** Write functions, average a column, and compute a dot product.

## 3. Learning from examples

A model is a function whose parameters are set by examples, then scored on examples it did not see.

### 12. Nearest neighbors — small

- **Build:** A table of labeled points. Predict a new point from the majority label among its nearest neighbors. Hold out a slice of the table and print the accuracy on that slice only.
- **Teaches:** Features, labels, and a score on data the prediction rule does not consult.
- **Already able to:** Compute distances and summarize a column.

### 13. Logistic regression — medium

- **Build:** From scratch, fit a weighted score plus a sigmoid to labeled rows, by gradient descent on log loss. Print training loss and held-out accuracy every pass. Add extra junk columns until the training score rises while the held-out score falls.
- **Teaches:** Weights, a probability output, log loss, and overfitting.
- **Already able to:** Fit a line by nudging parameters, and score a held-out set.

### 14. Exam runner — small

- **Build:** Tasks live in a folder. The runner loads them, asks a model function for predictions, prints a score, and writes that score to a result file. Training reads a different folder. Pass the task folder on the command line.
- **Teaches:** A fixed exam, separate from training data, that later programs import and reuse.
- **Already able to:** Write tests, import your own functions, and score held-out predictions.

## 4. Neural nets, derived

One network whose gradient you derive and check, then the same network written so a batch can train.

### 15. Two-layer network — large

- **Build:** In pure Python, a network with one ReLU hidden layer that learns XOR, a pattern a single weighted sum cannot separate. Initialize weights small and random. Train with the log loss from logistic regression. Write the forward pass and the backward pass. For every weight, compare your gradient to the change in loss from a tiny nudge.
- **Teaches:** Layers, ReLU, and the chain rule as a local multiplier. A wrong gradient trains nothing useful, and the nudge check is how you catch it.
- **Already able to:** Fit logistic regression, multiply matrices, and write tests.

### 16. Batched network — medium

- **Build:** The same network in NumPy, on a few thousand points. Each epoch appends the loss to a file. Why NumPy: a batch is an array. The idea is the model, and arrays keep the batch readable and fast enough to finish.
- **Teaches:** Shapes, vectorized matrix multiply, and a learning curve you can inspect after the run.
- **Already able to:** Check a gradient by nudging weights, and read a loss from a training loop.

## 5. Language models

Text becomes ids. The training signal is the probability of the next id.

### 17. Byte-pair tokenizer — medium

- **Build:** A tokenizer that starts from bytes and repeatedly merges the most common pair, plus a decode. Tests check that decode(encode(text)) returns the text, including an empty string and a character outside your sample.
- **Teaches:** Tokens, a vocabulary, and why the unit of text changes what the model can see.
- **Already able to:** Count with dictionaries, handle strings, and write tests.

### 18. Next-token trainer — medium

- **Build:** An embedding table. From only the previous token id, predict a distribution over the next id. Train on a short text with cross-entropy computed in log space. Report perplexity on a held-out slice.
- **Teaches:** Embeddings, softmax, cross-entropy, and perplexity. One previous token is a weak context; the next program widens it.
- **Already able to:** Train a batched NumPy model, tokenize text, and score a held-out set.

### 19. Attention head — medium

- **Build:** One attention head over a short sentence you choose. Print the attention weights. A causal mask limits each position to itself and earlier tokens. Include a test that a future token gets weight zero.
- **Teaches:** Query, key, value, and softmax as a distribution of attention over the prefix.
- **Already able to:** Multiply matrices and compute a softmax.

### 20. Tiny transformer — large

- **Build:** A 2-layer decoder-only model in NumPy: a few heads, a small width, residual connections, layer norm, and a position vector added at each index. Train it with Adam — each weight keeps a moving average of its gradient and of its squared gradient — on a short corpus you choose. Sample a continuation.
- **Teaches:** A causal language model as a stack of the pieces you already wrote, and an optimizer that gives noisy parameters smaller steps.
- **Already able to:** Train the next-token model, run a masked attention head, and check a gradient.

## 6. A real training run

Same model, lab tooling, a corpus, and a measured effect from changing the data.

### 21. PyTorch transformer — medium

- **Build:** Rewrite the tiny transformer in PyTorch. On one fixed batch, its logits match your NumPy logits to a tight tolerance. Why PyTorch: autograd computes the gradient you already derived and checked, so later programs can change the objective and the data.
- **Teaches:** Modules, tensors, and a numerical match between two implementations of one model.
- **Already able to:** Train the NumPy transformer and test two implementations against each other.

### 22. Corpus run — large

- **Build:** Train on a book or on your own writing. Save a checkpoint and load it to continue. Record per-token log-probabilities while sampling. Report held-out perplexity with the exam runner. Print samples at a few temperatures. CPU is enough at this size.
- **Teaches:** A data pipeline, checkpoints, temperature, and samples that can look fluent while the exam is still weak. The recorded log-probabilities are the input to post-training.
- **Already able to:** Train the PyTorch model and run the exam on a held-out folder.

### 23. Data mix — medium

- **Build:** Two training mixes from the same sources: one raw, one with exact duplicates removed and very short or repetitive documents dropped. Train both from the same start. Write a table of held-out perplexity.
- **Teaches:** The data mix moves the exam score when the architecture stays fixed.
- **Already able to:** Run a full training job to a checkpoint and score it on the exam.

## 7. Post-training

The pretrained model learns to follow instructions, to prefer a better answer, and to put probability on answers a program can check.

### 24. Instruction fine-tune — medium

- **Build:** Pairs you write: a prompt and a target answer, in one fixed text format. Supervised fine-tune from your checkpoint. After training, report the new exam score and the old held-out perplexity side by side.
- **Teaches:** Supervised fine-tuning, a prompt format, and the effect of that update on the original language-model exam.
- **Already able to:** Train from a checkpoint and sample with log-probabilities.

### 25. Preference update — medium

- **Build:** Triples you judge: a prompt, a better completion, a worse completion. Increase the log-probability gap between the better and the worse. Add a term that keeps both near the supervised model's log-probabilities: pass the gap through a sigmoid, take the negative log, and let a constant beta set how hard that nearness pulls. This is the DPO pattern.
- **Teaches:** Learning from a comparison when several answers are acceptable and a person prefers one.
- **Already able to:** Fine-tune on prompt-answer pairs and compute a completion's log-probability.

### 26. Verifiable-reward training — large

- **Build:** Arithmetic problems and short Python tasks. For each prompt, sample a group of completions that contain a scratchpad and a final line. A verifier scores only the final line, by exact match or a unit test. Advantage is the score minus the mean score in that group. Weight each completion's log-probability by its advantage and update. Skip a group where every score is equal. This is the GRPO pattern. Then loosen the verifier (accept a trailing extra token, or skip a test) and watch the exam.
- **Teaches:** Reinforcement learning with a verifiable reward, a group baseline, and reward hacking when the check is looser than the task.
- **Already able to:** Sample with log-probabilities, update from preferences, and write tests as verifiers.

### 27. Distill the traces — medium

- **Build:** Keep the short correct traces from the verifiable-reward run. Supervised fine-tune a fresh copy of the pretrained model on those traces. Compare it with the reinforcement-learning model on the same exam.
- **Teaches:** Distillation. The stack you have now is the one labs run: pretrain, supervised fine-tune, verifiable-reward reinforcement learning, then distill the good traces.
- **Already able to:** Fine-tune on pairs and produce verifier-accepted traces.

## 8. Scale and matched serving

Frontier models in 2026 are mixture-of-experts networks. The tokens served at sampling time have to be the tokens the update trains on.

### 28. Mixture of experts — large

- **Build:** Replace each feed-forward block in your transformer with several expert feed-forwards and a router. Each token uses the top two experts. Log how many tokens each expert receives. Add a penalty that pulls that load toward even, and show the load with and without the penalty.
- **Teaches:** Conditional compute, router collapse (one expert taking the tokens), and a load-balance penalty. This is the architecture family behind current frontier models.
- **Already able to:** Train the transformer and read a learning curve.

### 29. Cached generation — medium

- **Build:** While generating, store each layer's keys and values for tokens already produced. A test compares the next-token logits from the cache with logits from a full forward pass on the same prefix.
- **Teaches:** Inference state. A faster path is finished when its numbers match the slow path.
- **Already able to:** Run attention, sample from the model, and write a numerical test.

### 30. Router replay — medium

- **Build:** While sampling, save the expert index each token used at each layer. In the update, run two forwards: one that routes again, and one that forces the saved experts. Log the mean absolute gap in token log-probabilities. Train on the forced path.
- **Teaches:** Router replay. Frontier reinforcement learning records the serving decision because a fresh route picks different experts and the update then trains on a different computation.
- **Already able to:** Train the mixture-of-experts model, generate with a cache, and read token log-probabilities.

## 9. Agents

The program around the model chooses the context, runs the tools, and keeps the score.

From program 31 on, call a small open-weight instruction model through its loader, with its own tokenizer. Why: tool calls have to be reliable, and your transformer is too small a component for that. The program you are writing is the loop, the state, and the verifiers. Training programs still use PyTorch on your own models.

### 31. Tool-calling loop — medium

- **Build:** The model emits a tool name and arguments. Your program runs a calculator or a file read, appends the result, and calls the model again, in a new turn, until it emits a final answer. A bad parse is returned to the model as an error message. Tests cover a bad parse, a tool exception, and a loop that hits a turn limit.
- **Teaches:** The agent loop. The harness runs the action; the model proposes it.
- **Already able to:** Sample text, parse structured lines, and write tests.

### 32. Retrieval over your files — medium

- **Build:** Chunk a folder of documents. Embed each chunk with a bag-of-words vector hashed into a fixed length. Given a question, put the nearest chunks into the prompt, then answer. A test checks that a planted sentence is retrieved from the right file.
- **Teaches:** Memory as a store the prompt views, scored by the same distance you wrote for vectors.
- **Already able to:** Build the tool loop, compute a dot product, and read a folder of files.

### 33. Coding agent — large

- **Build:** A sandbox of small Python tasks with hidden tests. The agent reads the failure, edits the file, and reruns. It stops when the tests pass or the attempt budget ends. Run the tests in a subprocess. Why a subprocess: the task under study is a program in an environment, and the reward is that program's own result.
- **Teaches:** A terminal agent. Execution is the reward, which is how current coding agents are trained and scored.
- **Already able to:** Run the tool loop and write tests that a verifier can execute.

### 34. Action gate — medium

- **Build:** File writes and shell commands pass a gate before they run. The gate checks a written checklist and a second model pass, then logs allow or deny with the reason. A denied action returns the reason to the agent.
- **Teaches:** A harness that can refuse an action. Long-running agents in current labs check consequential steps before they happen.
- **Already able to:** Run the coding agent and log a decision to a file.

## 10. Frontier systems (October 2026)

This is the work labs are doing now. The model is a mixture-of-experts network, post-trained with supervised updates and with reinforcement learning on rewards a program can check. Around it, a harness keeps the research state, starts a fresh model call for each job, chooses the next experiment, runs several fresh attempts and keeps the best, and changes its own prompts and tools only when a verifier agrees. You build that system at a size you can run.

### 35. Harness-owned research log — large

- **Build:** A log on disk of attempts, scores, and notes. Every model call starts from an empty session and sees only the summary the harness inserts. Two roles: an advisor that names the next task, and a worker that performs that task. Why the open-weight model, still: it fills the two roles. The state is yours; the session holds none of it.
- **Teaches:** Stateless agents. Current long-horizon research systems keep state in the harness and rebuild each call's context on purpose.
- **Already able to:** Run the tool loop, retrieve from a store, and record an exam score.

### 36. Work-order loop — large

- **Build:** The advisor reads the log and emits a stop, or a work order with a hypothesis, the file the worker may change, and a tool-call budget. The worker carries out that order. The verifier appends the score. The advisor's next decision sees the new log and a new session.
- **Teaches:** Meta-reasoning as its own policy: what to try next, scored at the work-order boundary.
- **Already able to:** Run the harness-owned log and score a result with a verifier.

### 37. Fork and keep the best — medium

- **Build:** Copy the workspace. Start several workers with empty chats and the same tool-call budget. Continue from the copy with the best verifier score, and append the other scores to the log.
- **Teaches:** A long single trajectory settles into one region of ideas. A fresh context on the same files is how current research agents leave that region under a fixed compute budget.
- **Already able to:** Run the work-order loop and compare verifier scores.

### 38. Verified harness edit — large

- **Build:** A second loop proposes one edit to a prompt, a tool description, or the gate's checklist. Replay tasks that previously failed. Keep the edit only when those tasks improve and a protected held-out set does not get worse. Weights stay frozen.
- **Teaches:** The harness evolves under execution-based checks. This is the system labs train when the optimizer rewrites prompts, tools, and workflow, and the model weights stay fixed.
- **Already able to:** Run the coding agent, split an exam into train and held-out tasks, and keep a research log.

### 39. Executable world model — large

- **Build:** A small grid puzzle whose rule is hidden. The agent writes a Python function `next_state(grid, action)`. Check it against transitions already observed. On a mismatch, the agent revises the function and the gate reviews the file write. When the check passes, search that function for a short action list — the same breadth-first search as the maze solver — then run the list on the real puzzle.
- **Teaches:** A world model as code that must match observation, then planning in the checked model. Coding agents that write and verify a simulator are a current approach on hard grid tasks (ARC-AGI-3).
- **Already able to:** Search a grid, run the coding agent, and pass actions through the gate.

### 40. Narrow autoresearch loop — large

- **Build:** Aim the harness at one scored question: which data filter lowers held-out perplexity of your small model. The open-weight model is the advisor and the worker. Your model is the one being trained. The log stores runs. The advisor spends a fixed budget of work orders. Workers edit the filter, train, and record the exam score. The fork from program 37 continues from the better filter. A proposed edit to the advisor's prompt is kept only when a held-out slice of the exam improves.
- **Teaches:** How the current frontier fits in one system you can run: harness-owned state, fresh calls, a policy for the next experiment, parallel attempts that escape a weak idea, and harness changes accepted by a verifier. The scarce resource is checked experiments, spent on a model you know how to train.
- **Already able to:** Train your small model, score it on the exam, fork workers, and accept a harness edit only after held-out replay.
