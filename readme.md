🧠 Explain-My-Mistake Engine

Cognitive Mistake Taxonomy for GATE CS (v1.0)

> *Why did a wrong answer feel right at the moment of choice?*

---

Overview

The **Explain-My-Mistake Engine** is a cognitive analysis framework designed for **competitive MCQ-based exams**, with a primary focus on **GATE Computer Science**.

Instead of analyzing *what* went wrong (topic, formula, syllabus area), this system analyzes:

> **Which mental process failed at the moment the answer was selected.**

This repository contains the **canonical v1.0 taxonomy** — a closed, non-overlapping set of cognitive mistake categories that explain **decision-making failures**, not knowledge gaps.

---

## 🎯 Why This Exists

Traditional exam analysis focuses on:

* Accuracy percentage
* Topic-wise weakness
* Correct vs incorrect counts

These approaches fail to explain a crucial phenomenon:

> *“I knew this… why did I still get it wrong?”*

This framework answers that question by modeling **human cognition under exam pressure**.

---

## 🧠 Core Design Philosophy

This taxonomy is built on the following principles:

* **Exactly 8 mistake categories** (closed set)
* **Non-overlapping at the cognitive level**
* **One dominant mistake per attempt**
* **Explainable and observable**
* **Aligned with real GATE CS exam behavior**
* **Independent of syllabus or subject**

Each mistake category answers a single diagnostic question:

> **What mental process failed at the moment of decision?**

---

## 🧠 The 8 Cognitive Mistake Categories

### 🧠 Mistake 1: Impulse Guessing under Time Pressure

**Definition**
Selecting an option before meaningful reasoning begins, driven by urgency, anxiety, or perceived lack of time.

**Core Cognitive Failure**
Analytical thinking is suppressed; speed replaces reasoning.

**Key Signals**

* Extremely low time spent (relative to baseline)
* Low or absent confidence
* No elimination or reasoning evidence

**Dominance Rule**
If triggered, this mistake **overrides all others** — reasoning never started.

**Corrective Action**
Introduce a mandatory pause before answering urgent-feeling questions.

---

### 🧠 Mistake 2: Familiarity / Recognition Trap

**Definition**
Choosing an option because it *looks familiar*, without verifying whether it satisfies all conditions.

**Core Cognitive Failure**
Recognition heuristics replace verification.

**Key Signals**

* Normal time spent
* Medium to high confidence
* Keyword or formula recognition
* Shallow comparison of alternatives

**Dominance Rule**
Cannot trigger if deep multi-step reasoning is present.

**Corrective Action**
Ask explicitly: *“Why could this option be wrong?”*

---

### 🧠 Mistake 3: Illusion of Competence (Confident but Flawed Reasoning)

**Definition**
Structured reasoning is applied, but the reasoning itself is logically incorrect, incomplete, or based on a false assumption — with high confidence.

**Core Cognitive Failure**
Internal coherence is mistaken for correctness.

**Key Signals**

* High confidence
* Multi-step reasoning present
* Identifiable logic or assumption error

**Dominance Rule**
Dominates whenever a **logic flaw** is detected.

**Corrective Action**
Explicitly state assumptions and attempt to disprove them.

---

### 🧠 Mistake 4: Elimination Failure / Partial Knowledge Trap

**Definition**
Using elimination based on incomplete criteria and selecting an option that is partially correct but not fully valid.

**Core Cognitive Failure**
Relative correctness replaces absolute correctness.

**Key Signals**

* Explicit elimination behavior
* Moderate confidence
* Final option is contextually or partially correct

**Dominance Rule**
Requires explicit elimination behavior.

**Corrective Action**
Verify the remaining option against **every condition** in the question.

---

### 🧠 Mistake 5: Misreading / Condition Skipping Error

**Definition**
Failure to correctly read, register, or apply explicit conditions in the question.

**Core Cognitive Failure**
Expectation-driven reading overrides literal parsing.

**Key Signals**

* Missed keywords (NOT, EXCEPT, ONLY, ALWAYS)
* Otherwise correct reasoning
* Medium to high confidence

**Dominance Rule**
Dominates if concepts and reasoning are otherwise correct.

**Corrective Action**
Restate the question in your own words before evaluating options.

---

### 🧠 Mistake 6: Overthinking / Second-Guessing Error

**Definition**
The student initially reaches the correct answer but changes it unnecessarily due to doubt or fear of traps.

**Core Cognitive Failure**
Confidence collapses after sufficient reasoning.

**Key Signals**

* High time spent
* Falling confidence
* Answer changed after correct reasoning

**Dominance Rule**
Initial reasoning must be correct.

**Corrective Action**
Change answers **only** if a concrete contradiction is found.

---

### 🧠 Mistake 7: Mechanical / Formula / Procedure Misuse

**Definition**
Correct concept and method are known, but execution fails due to arithmetic, formula, or procedural errors.

**Core Cognitive Failure**
Autopilot execution without validation.

**Key Signals**

* Near-correct result
* Correct method selection
* Localized error

**Dominance Rule**
Method must be logically correct.

**Corrective Action**
Perform sanity checks on magnitude, units, or boundaries.

---

### 🧠 Mistake 8: Personal Habitual Pattern (Meta-Mistake)

**Definition**
A recurring mistake pattern identifiable only across multiple attempts.

**Core Cognitive Failure**
Learned exam habits dominate behavior under pressure.

**Key Signals**

* Repetition of the same primary mistake
* Subject-specific clustering
* Stable time/confidence patterns

**Dominance Rule**
Never primary for a single attempt. Always meta-level.

**Corrective Action**
Define subject-specific personal operating rules.

---

## 📊 Master Summary Table

| # | Mistake                | Core Failure           | Key Signal                | Corrective Action     | Dominance Rule      |
| - | ---------------------- | ---------------------- | ------------------------- | --------------------- | ------------------- |
| 1 | Impulse Guessing       | No reasoning           | Very low time             | Forced pause          | Overrides all       |
| 2 | Familiarity Trap       | Shallow reasoning      | Keyword comfort           | Verify conditions     | No deep logic       |
| 3 | Illusion of Competence | Logic flaw             | Confident wrong reasoning | State assumptions     | Dominates logic     |
| 4 | Elimination Failure    | Strategy misuse        | Partial correctness       | Full condition check  | Needs elimination   |
| 5 | Misreading Error       | Interpretation failure | Missed condition          | Restate question      | Logic correct       |
| 6 | Overthinking           | Confidence collapse    | Answer change             | Require contradiction | Initial logic right |
| 7 | Mechanical Misuse      | Execution slip         | Near-correct result       | Sanity check          | Method correct      |
| 8 | Personal Pattern       | Habitual behavior      | Repetition over time      | Personal rules        | Meta-only           |

---

## 🚀 Intended Use Cases

* Post-mock exam analysis
* Error-log systems
* Coaching diagnostics
* Self-reflection frameworks
* Future automation or ML-based exam analytics

---

## 🧠 What This Is *Not*

* ❌ A topic-wise weakness list
* ❌ A syllabus analysis tool
* ❌ A confidence tracker
* ❌ A motivation framework

This system is purely about **cognitive decision failures**.

---

## 🔮 Roadmap (Planned)

* Decision-tree–based mistake assignment protocol
* Logging schema (Sheets / Notion / App)
* Mistake × Subject heatmaps
* Confidence vs time analytics
* Personal rule generation engine

---

## 📜 License & Usage

This taxonomy is shared for **educational and research purposes**.
Attribution is appreciated. Commercial usage should seek permission.

---

## ✨ Final Note

If you’ve ever thought:

> *“I knew this… why did I still mess it up?”*

This framework exists for you.

---
