---
date: '2025-07-24 17:37:47'
layout: post
tags:
- StudyNotes/StudyTech
title: Long term retention decks?
---

# Long term retention decks - aren't *all* decks supposed to help with long term retention?

This is an **excellent** question that cuts to the heart of Anki philosophy. Let's clarify the distinction:

---

### **What "Long-Term Retention Decks" Really Means**
While *all* Anki decks aim for long-term retention, the term **"long-term retention decks"** specifically refers to decks where:
1.  **Time Horizon is Indefinite:** You intend to retain the knowledge for **decades or life** (e.g., medical licensing facts, language vocabulary, foundational concepts in your field).
2.  **Retention Demand is Ultra-High:** You need **≥90-95% retention** because failure has high costs (misdiagnosis, professional errors, fluency breakdowns).
3.  **Content is Static:** Facts won't change significantly over time (e.g., anatomy, historical dates, core vocabulary).

**Contrast with "Shorter-Term" Decks:**
- Exam cram decks (retain for 6 months).
- Learning a language for an upcoming trip (retain for 1–2 years).
- Memorizing talk points for a conference (retain for 1 month).

---

### **Why the IM 80% + Easy 170% Combo is Risky for *True* Long-Term Retention**
This setting tweak (common in older Anki optimizations) has two interacting effects:
1.  **Interval Modifier = 80%:**  
    → *Decreases* all intervals by 20%.  
    → **Result:** Reviews happen *more frequently* than the algorithm prescribes.  
2.  **Easy Bonus = 170%:**  
    → *Increases* intervals for "Easy" reviews by 70%.  
    → **Result:** Cards rated `Easy` jump to *much* longer intervals.  

**The Deadly Combination:**  
- Frequent reviews (from IM 80%) increase workload unnecessarily for mature cards.  
- But when you *do* hit `Easy`, cards vault to extremely long intervals (e.g., 3 years → 5.1 years).  
- **Problem:** At intervals >2–3 years, memory predictability plummets. A card at 90% retrievability today might decay to 40% in 4 years due to:  
  - **Stability plateauing:** Memory stability (S) growth slows dramatically at very high values.  
  - **Interference:** New experiences degrade old memories unpredictably.  
  - **Algorithmic limits:** SM-2 wasn't designed for 10-year intervals.  

**Result:** You *think* a card is "locked in" (you rated it `Easy`!), but years later, it has **vanished**. This is the **"illusion of knowledge"** on a multi-year scale.  

---

### **Why This Isn't a Problem for Shorter-Term Decks**
- If your goal is retention for **≤2 years**:  
  - Intervals rarely exceed 1–1.5 years even with `Easy`.  
  - The risk of catastrophic forgetting is low.  
  - Frequent reviews (from IM 80%) might even be *beneficial* for exam prep.  

---

### **The Core Conflict: Workload vs. Ultra-Long-Term Reliability**
| Goal                | IM 80% + Easy 170%          | Safer Long-Term Settings (e.g., IM 100%, Easy 130%) |
|---------------------|------------------------------|-----------------------------------------------------|
| **Workload**        | Lower (fewer total reviews)  | Higher (more reviews of mature cards)              |
| **Retention Risk**  | High (for intervals >3 yrs)  | Low (intervals grow conservatively)                |
| **"Easy" Meaning**  | "I know this *today*"        | "I know this *deeply* for the long haul"           |

**FSRS Note:** Modern FSRS (v5.0+) handles this natively by:  
- Using **retention targets** (e.g., 90% vs. 95%).  
- Automatically adjusting intervals to hit your target *without* combo hacks.  

---

### **Card to Lock This In (Updated)**
**Front:**  
For Anki decks targeting **lifelong retention**, why is the "Interval Modifier 80% + Easy Bonus 170%" combo risky?  

**Back:**  
It creates **unpredictable gaps** for mature cards:  
1. `Easy` ratings send intervals to extremes (>3 yrs),  
2. where memory decay becomes erratic and hard to model.  
Result: High chance of **catastrophic forgetting** years later.  

**Extra:**  
- *Safe alternative:* Use FSRS (target 90-95% retention) or SM-2 with conservative Easy Bonus (≤130%).  
- *Exception:* Combo is acceptable for decks with retention horizons <2 years.  

---

### Key Insight
**Anki optimizes for *efficient* long-term retention, not *infinite* retention.** Truly "permanent" memory requires either:  
1. **Ultra-conservative scheduling** (high workload), or  
2. **Contextual reactivation** (using knowledge in real life).  

The IM/Easy hack trades reliability for workload—a gamble justified only for short-term goals.
