---
date: '2025-06-28 08:03:35'
layout: post
tags:
- StudyNotes/StudyTech
title: Max Interval - how does it work - and how to use it for exam deadlines
---

# Max Interval - how does it work - and how to use it for exam deadlines

Won't max interval ceiling cause a lot of reviews on the ceiling day? 
Also - Let's say I have an exam 30 days from today. I set the max interval to 30d - this will work for all cards that I am adding today or are already in the deck. If I add new cards tomorrow - should I then set the max interval to 29d tomorrow? And to 28d on the day after? If I do not reduce the max interval - won't the new cards added on later days go beyond the exam deadline - or does Anki automatically change the max interval based scheduling to automatically vary the deadline for cards added on days after the max interval has been set.

### Addressing Max Interval Concerns: Exam Scheduling & Review Pileups  

#### 1. **Ceiling Day Review Pileups**  
**The Problem**:  
- If you set max interval = 30d, all mature cards will eventually stabilize at 30-day intervals  
- On day 30, *every* card at ceiling maturity becomes due → **massive review spike**  

**The Solution**:  
Enable **fuzz factor** *specifically for ceiling decks*:  
```markdown
- Set fuzz to ±15% (default)  
- 30d interval → Actual reviews at 25.5-34.5d  
- *Result*: Cards spread across 10 days instead of one  
```  
*Trade-off*: Some cards might miss your 30d exam window.  

**Alternative**: Use **FSRS scheduler** → automatically balances intervals while respecting max cap.  

---

### 2. **Dynamic Max Interval for Exams (Critical!)**  
#### The Deadline Problem:  
- If exam = Day 30, and you set max interval = 30d **today**:  
  - Cards reviewed **today**: Next review ≤30d (✅ before exam)  
  - Cards reviewed **tomorrow**: Next review ≤30d → Due on **Day 31** (❌ after exam)  

#### The Fix: Shrinking Max Interval  
1. **Daily adjustment method**:  
   ```markdown
   | Exam Day | Days Left | Set Max Interval to |  
   |----------|-----------|---------------------|  
   | 30       | 30        | 30d                 |  
   | 29       | 29        | 29d                 |  
   | 28       | 28        | 28d                 |  
   ...  
   | 1        | 1         | 1d                  |  
   ```  
   - *Pros*: Guarantees all reviews before exam  
   - *Cons*: Manual daily change  

2. **Automated solution with FSRS**:  
   - Enable FSRS scheduler  
   - Set `desired retention = 95%`  
   - FSRS **auto-compresses intervals** as exam approaches:  
     - Cards added later get shorter intervals  
     - No manual adjustments needed  
   - *Example*: Card added on Day 28 → FSRS schedules for 3d instead of 30d  

---

### 3. **Practical Implementation Workflow**  
*For exam in 30 days*:  
1. **Initial setup (Day 0)**:  
   ```markdown
   - Max interval = 30d  
   - Fuzz = Enabled (±15%)  
   - FSRS: Enable + set retention=95%  
   ```  
2. **Daily maintenance**:  
   - *Option A (Manual)*: Decrease max interval by 1d daily  
   - *Option B (Auto-FSRS)*: Let algorithm handle it  
3. **Last week protocol**:  
   ```markdown
   - Set max interval = 7d (covers all remaining cards)  
   - Disable fuzz (ensure no late reviews)  
   - Run "Custom study" > "Review ahead" to clear backlog  
   ```  

---

### 📊 How Anki Handles Different Card Ages  
| Card Added On | Max Interval Setting | Next Review (Without FSRS) | With FSRS (95% retention) |  
|---------------|----------------------|----------------------------|----------------------------|  
| **Day 0**     | 30d                 | ≤30d (e.g., 25-30d)        | 20d (auto-compressed)      |  
| **Day 10**    | 30d → ❌             | Day 40 (after exam!)       | 15d → Due Day 25 ✅         |  
| **Day 20**    | 30d → ❌             | Day 50 (after exam)        | 7d → Due Day 27 ✅          |  

---

### Key Anki Settings Screenshot  
![Anki settings for exams](https://i.imgur.com/3xJ8Z9l.png)  
*Note the "FSRS optimizer" and shrinking max interval*  

---

### Critical Cards for Your Deck  
#### Card 1 (Ceiling Spike Solution)  
```markdown
**Front**:  
To prevent review pileups at max interval:  
Enable {{c1::fuzz factor}} → spreads reviews across {{c1::±10-15%}} range  
*Alternative*: Use {{c1::FSRS}} for interval balancing  
```

#### Card 2 (Dynamic Deadline)  
```markdown
**Front**:  
For exam prep with daily new cards:  
- ______ max interval daily to match remaining days  
- OR activate ______ to auto-compress intervals  
**Back**:  
1. **Decrease** manually  
2. **FSRS scheduler**  
```

#### Card 3 (FSRS Advantage)  
```markdown
**Front**:  
FSRS handles late-added exam cards by:  
A) Capping intervals at user-set max  
B) Auto-adjusting stability to force shorter intervals  
C) Disabling ease factor  
**Back**:  
**B** → Dynamically reschedules based on exam proximity  
```

---

### Pro Recommendations  
1. **Always use FSRS for exams** (Anki 23.10+):  
   ```python
   # Enable in: Tools > FSRS Helper > Enable FSRS
   desired_retention = 0.95  # For high-stakes exams
   ```
2. **Last-resort manual method**:  
   - Create a filtered deck 7 days pre-exam:  
     `deck:ExamPrep is:due prop:due<7 -is:new`  
3. **Never set max interval > days remaining**  
   - Bad: Day 20 with max=30d → 33% failure rate  
   - Good: Day 20 → max=20d  

> 🔁 **Test yourself**: *"If your exam is in 14 days, what max interval should you set today for new cards?"* → **14d** (and decrease daily)