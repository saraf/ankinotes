---
date: '2025-06-30 11:53:14'
layout: post
tags:
- StudyNotes/StudyTech
title: FSRS - Memory Stability and Card Difficulty
---

# FSRS - Memory Stability and Card Difficulty

FSRS (Free Spaced Repetition Scheduler) fundamentally rethinks Anki's scheduling by replacing the monolithic **Ease Factor** with two scientifically grounded, machine-learning-predicted variables: **Memory Stability (S)** and **Card Difficulty (D)**. Here's a precise breakdown of their definitions, differences, and interplay:

---

### **1. Memory Stability (S)**  
**Definition**:  
*The **expected duration** (in days) until retrievability drops to a predefined threshold (e.g., 90%) after a successful review.*  
- **Formula**: Governs the exponential decay of retrievability:  
  `R(t) = exp(-t / S)`  
  where `R(t)` = probability of recall at time `t`.  
- **Interpretation**:  
  - If `S = 30`, the card has a 90% recall chance 30 days after review.  
  - **Increases** after successful reviews (especially when recall is effortful).  
  - **Decreases** after failed reviews.  

**Key Properties**:  
- **Card-specific**: Stability is tracked per card.  
- **Dynamic**: Adjusts with each review based on performance.  
- **Goal**: Maximize stability to achieve longer intervals (↓ review frequency).  

---

### **2. Card Difficulty (D)**  
**Definition**:  
*A **unitless scalar** (typically 1–10+) quantifying how hard a card is to learn and retain.*  
- **Interpretation**:  
  - `D = 1` → Very easy (e.g., "Capital of France?")  
  - `D = 5` → Moderately hard  
  - `D ≥ 8` → Very difficult (e.g., abstract concepts, subtle distinctions)  
- **Fixed**: Unlike Anki’s Ease Factor, **D does not change** unless the card is modified.  
  - *Exception: FSRS may slightly refine D early in learning*.  

**Key Properties**:  
- **Modulates Stability Growth**: Controls how much stability increases after successful reviews.  
- **Impacts Lapses**: High-difficulty cards lose more stability after failures.  

---

### **3. How They Interact**  
FSRS uses a **stability growth function** where **Difficulty (D) throttles Stability (S) gains**:  
```  
Stability_after_success = S_current * f(D, R)  
```  
- `f(D, R)` is a **stability multiplier** (always ≥1).  
- **Critical insight**:  
  - **Easy cards (low D)**: Large stability jumps (e.g., `f(D,R) = 3.0` → interval triples).  
  - **Hard cards (high D)**: Tiny stability gains (e.g., `f(D,R) = 1.2` → interval grows 20%).  
- **Retrievability (R)** matters: Gains are larger when recalling at low retrievability (~50-80%).  

#### **Example Workflow**:  
| Step | Card A (Easy, D=2) | Card B (Hard, D=8) |  
|------|---------------------|--------------------|  
| **Initial Review** | S = 2 days | S = 2 days |  
| **Review @ 2 days (Success)** | S_new = 2 * 3.0 = **6 days** | S_new = 2 * 1.2 = **2.4 days** |  
| **Next Interval** | 6 days | 2.4 days |  
| **After 5 successes** | S ≈ 150 days | S ≈ 5 days |  

**Outcome**: Easy cards accelerate to long intervals quickly; hard cards require frequent reviews.  

---

### **4. Contrast with Anki's Ease Factor**  
| Feature          | Anki (SM-2)         | FSRS                |  
|------------------|---------------------|---------------------|  
| **Core Metric**  | Ease Factor (EF)   | Stability (S) + Difficulty (D) |  
| **EF/S Behavior** | Changes per review (punished for lapses) | S: Dynamic per review; D: Mostly static |  
| **Interval Calc** | `Last Interval × EF` | ML-predicted based on S, D, and target retention |  
| **Adaptiveness** | Heuristic           | Bayesian optimization + Neural Networks |  
| **Response to Failure** | EF ↓ → Permanent interval penalty | S ↓ → Temporary recovery possible |  

---

### **5. Why This Matters**  
- **Precision**: FSRS models human memory more accurately by decoupling:  
  - **Stability (S)** → *How ingrained the memory is*.  
  - **Difficulty (D)** → *How intrinsically hard the card is*.  
- **Resilience**: No "ease hell" – hard cards (high D) naturally get shorter intervals without permanent penalties.  
- **Efficiency**: Optimizes intervals to minimize reviews while hitting target retention (e.g., 90%).  

---

### **Practical Implications**  
1. **Hard cards stay in rotation longer** (low stability gains) but **won’t bury you** (unlike ease-factor decay).  
2. **Modify cards** if `D > 7`: Split complex cards per Minimum Information Principle.  
3. **Trust FSRS scheduling** – it leverages S and D to space reviews optimally.  

FSRS transforms Anki from a heuristic tool into a memory-optimized engine. To use it effectively: focus on creating atomic cards (controlling D) and review honestly (so S updates accurately).