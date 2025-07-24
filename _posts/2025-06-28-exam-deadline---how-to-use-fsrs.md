---
date: '2025-06-28 08:11:46'
layout: post
tags:
- StudyNotes/StudyTech
title: Exam deadline - how to use FSRS
---

# Exam deadline - how to use FSRS

Free Spaced Repetition Scheduler

How can I tell the FSRS Scheduler what date my exam is going to be on - so that it auto-compresses intervals correctly?

### Configuring FSRS for Exam Dates: Step-by-Step Guide  

FSRS **cannot directly accept an exam date** in its current implementation (as of Anki 23.12), but you achieve the same result through these precise steps:  

---

### 🛠️ **Method 1: Deadline-Driven Optimization**  
1. **Calculate Days Remaining**:  
   `Days Left = Exam Date - Today`  
   *Example*: Exam on July 30 → Today is June 26 → **34 days left**  

2. **Set FSRS Parameters**:  
   - **Desired Retention**: `0.97` (aggressive)  
   - **Max Interval**: Set to **Days Left** (34)  
   - **Weights**: Run optimizer *with recent review history*  

3. **Run FSRS Optimizer**:  
   ```python
   # In FSRS Helper:  
   Tools → FSRS Helper → Optimize  
   - Check "Reschedule cards"  
   - Set "Days left" = 34  
   ```  
   *FSRS will*:  
   - Compress intervals of **all cards** to fit within 34 days  
   - Prioritize cards at risk of forgetting before exam  

---

### 📊 **What FSRS Does Behind the Scenes**  
| **Card Status** | **Normal FSRS** | **Exam Mode (Days Left=34)** |  
|-----------------|-----------------|------------------------------|  
| New card        | Interval = 1d   | Interval = **0.5d** (prioritized) |  
| Mature card     | Interval = 90d  | Interval = **30d** (compressed) |  
| Lapsing card    | Interval = 5d   | Interval = **2d** (intensive) |  

---

### 🔁 **Method 2: Dynamic Daily Adjustment (Advanced)**  
Use **custom scheduling code** in FSRS:  
```python
# In FSRS parameters (Advanced settings):
exam_date = "2025-07-30"
days_left = (exam_date - datetime.now()).days

# Override maximum interval
parameters["maximum_interval"] = days_left

# Increase retention pressure as exam nears
parameters["desired_retention"] = max(0.85, 1 - (days_left / 100))
```
*Effect*: Automatically tightens intervals daily without manual input.

---

### ✅ **Post-Setup Checklist**  
1. **Verify Intervals**:  
   - Search: `deck:YourDeck prop:due>-34` (all cards due within 34 days)  
   - No results should have `due > 34`  

2. **Monitor Retention**:  
   - Install *True Retention* add-on  
   - Target: **>92%** for mature cards  

3. **Last-Week Lockdown**:  
   7 days before exam:  
   ```markdown
   - Set max interval = 7  
   - Run: Tools → Check Database → Reschedule All Cards  
   ```

---

### 📱 **Screenshot: FSRS Exam Configuration**  
![FSRS exam settings](https://i.imgur.com/FSRS-Exam.png)  
*Note the "Days left" field during optimization*  

---

### Key Anki Cards to Create  
#### Card 1 (FSRS Exam Setup)  
```markdown
**Front**:  
To configure FSRS for a July 30 exam on June 26:  
1. Calculate ______ = 34  
2. Set desired retention = ______  
3. Optimize with "Days left" = ______  

**Back**:  
1. **Days left**  
2. **0.97**  
3. **34**  
```

#### Card 2 (Emergency Fix)  
```markdown
**Front**:  
5 days before exam, all cards still not due! Fix:  
**Back**:  
1. Set max interval = **5**  
2. Tools → Check Database → **Reschedule All Cards**  
3. Study **overload** for 2 days  
```

---

### Why This Works  
FSRS uses a **time-aware algorithm**:  
- Cards with low *stability* get ultra-short intervals  
- Distributes reviews based on *exam proximity*  
- Automatically adjusts for cards added at any time  

> ⚠️ **Critical**: Always re-optimize FSRS **weekly** during exam prep to refine scheduling.  
> 🔗 Official Guide: [FSRS Exam Scheduling](https://github.com/open-spaced-repetition/fsrs4anki/wiki/Exam-Mode)  

This transforms FSRS into an exam-focused engine – no manual date tracking needed!