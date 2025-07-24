---
date: '2025-06-26 17:36:10'
layout: post
tags:
- StudyNotes/StudyTech
title: Interval Modifiers in an Anki Deck - when to change
---

# Interval Modifiers in an Anki Deck - when to change

Here's a structured guide on when and why to adjust Anki's Interval Modifier (IM), with actionable diagnostics and settings:

---

### **When to Change the Interval Modifier**  
#### ✅ **INCREASE IM (>100%)**  
**Scenario 1: Reviews Feel Too Easy**  
- *Signs*: Consistently hitting "Easy" (>90% correct), feeling bored  
- *Action*: Set IM to 120-150%  
- *Why*: Accelerates spacing of mastered material (e.g., mature language decks).  

**Scenario 2: Reducing Review Burden**  
- *Signs*: Overwhelmed by daily reviews despite high retention (>90%)  
- *Action*: Gradually increase IM by 10% weekly until reviews stabilize.  
- *Example*: 200 reviews/day → IM 130% → ~150 reviews/day.  

**Scenario 3: Long-Term Retention Focus**  
- *For*: Knowledge you’ll need for years (e.g., foundational anatomy).  
- *Settings*: IM 110-130% + Max Interval cap (prevents excessive spacing).  

---

#### ✅ **DECREASE IM (<100%)**  
**Scenario 1: Struggling with Retention**  
- *Signs*: <80% correct on mature cards, frequent "Again"  
- *Action*: Set IM to 70-90%  
- *Why*: Forces more exposure (e.g., complex pharmacology mechanisms).  

**Scenario 2: High-Stakes Exam Prep**  
- *Signs*: Forgetting nuances (e.g., drug side effects)  
- *Action*: IM 80% + Max Interval 30-60d.  
- *Science*: Compresses intervals to combat *instability* before test day.  

**Scenario 3: "Ease Hell" Recovery**  
- *Signs*: Cards stuck in short intervals despite correct reviews.  
- *Fix*: IM 85% + reset card ease (via add-ons like "Reset Ease").  

---

#### ⚠️ **When NOT to Change IM**  
- If retention is 85-90% → Default 100% is optimal.  
- For learning-phase cards → Adjust **learning steps** instead.  
- If using FSRS → Tune *desired retention* (not IM).  

---

### **Diagnostic Cheat Sheet**  
| **Symptom**                | **Solution**          | **Example Workflow**          |  
|----------------------------|----------------------|-------------------------------|  
| "I know this too well"     | IM ↑ (120-150%)      | Language vocab: 100% → 130%   |  
| "I keep forgetting"        | IM ↓ (70-90%)        | Medical syndromes: 100% → 80% |  
| Reviews feel trivial       | IM ↑ + Max Interval ↑ | Mature deck: IM 140%, Max 5y   |  
| Exam in 2 months           | IM ↓ + Max Interval ↓ | IM 80%, Max 45d               |  

---

### **Key Cards to Cement This**  
#### Card 1 (Decision Trigger)  
**Front**:  
You have 92% retention but 300+ daily reviews. What setting change reduces burden WITHOUT hurting retention?  
**Back**:  
**Increase Interval Modifier to 120-130%**  
- Gradually raises intervals → fewer reviews  
- *Monitor*: Keep retention >85%  

#### Card 2 (Error Recovery)  
**Front**:  
Your pharmacology deck has 75% retention. What TWO actions fix this?  
**Back**:  
1. **Lower Interval Modifier (e.g., 80%)**  
2. **Cap Maximum Interval (e.g., 60d)**  
*Reason*: More frequent exposure + constrained spacing  

#### Card 3 (FSRS Note)  
**Front**:  
How does Interval Modifier function change under FSRS?  
**Back**:  
**FSRS replaces IM with "Desired Retention"**:  
- Want fewer reviews? Lower retention (e.g., 85%)  
- Want higher retention? Accept more reviews (e.g., 92%)  

---

### **Pro Tips**  
1. **Change gradually**: Adjust IM by 10-20% increments, not 50%.  
2. **Track metrics**: Use add-ons like *True Retention by Card Maturity* before/after changes.  
3. **Combine tactics**: For exams: IM 80% + Easy Bonus 170% + Max Interval 60d.  

> Always test changes on a *subdeck* first. It takes 2-3 weeks to see effects!

## What will happen in Pro Tip Scenario 3 - IM 80% and Easy Bonus 170%

Here's a precise breakdown of how **IM 80% + Easy Bonus 170%** works in exam prep, including *why* this combo is powerful and its practical effects:

---

### **Mechanics & Workflow**  
#### **Baseline Scenario**  
- Card due in 30 days  
- You rate it **"Easy"**  
- Default settings:  
  - Interval Modifier (IM): 100%  
  - Easy Bonus: 130%  
  → *New interval = 30 × 1.3 = 39 days*  

#### **With Your Combo (IM 80% + Easy Bonus 170%)**  
- Same card due in 30 days  
- You rate it **"Easy"**  
- Calculation:  
  **Step 1**: Apply IM first → `30d × 0.8 = 24d`  
  **Step 2**: Apply Easy Bonus → `24d × 1.7 = 40.8d`  
  → *New interval ≈ 41 days*  

---

### **Why This Combo Rocks for Exams**  
| **Component**   | **Function**                                  | **Exam Benefit**                          |  
|-----------------|----------------------------------------------|------------------------------------------|  
| **IM 80%**      | Compresses *all* intervals by 20%            | Forces more reviews for **weak cards**   |  
| **Easy Bonus 170%** | Aggressively stretches "Easy" intervals | Rewards **strong cards** with fewer reviews |  

#### **Real-World Impact**  
1. **For a card you *barely* know** (rated "Hard"):  
   - Default: 30d → 24d (IM 80%)  
   - **Result**: Sees it sooner → reinforces fragile memory  

2. **For a card you *know cold*** (rated "Easy"):  
   - Default: 30d → 39d  
   - **Your Combo**: 30d → **41d** (slightly *longer* than default!)  
   - **Key Insight**: Strong cards "escape" the IM compression → **reduces unnecessary reviews**  

---

### **When to Use This**  
#### ✅ **Ideal For:**  
- **Volume-heavy exams** (e.g., USMLE, bar exams)  
- **Decks with mixed difficulty** (e.g., some cards easy, some brutal)  
- **Last 2-3 months before exam**  

#### ⚠️ **Risks if Misused:**  
- Overusing "Easy" → Cards disappear until *after* exam  
- **Solution**: Add **Max Interval = exam date - 1 week** (e.g., 60d cap)  

---

### **Card Examples to Cement This**  
#### Card 1 (Combo Logic)  
**Front**:  
Why pair IM 80% with Easy Bonus 170% for exam prep?  
**Back**:  
- **IM 80%**: Safeguards against forgetting (↓ intervals)  
- **Easy Bonus 170%**: Prevents over-reviewing mastered material (↑ easy intervals) → *Net efficiency*  

#### Card 2 (Calculation)  
**Front**:  
Card interval = 50d. You hit "Easy" with IM 80% + Easy Bonus 170%. New interval?  
**Back**:  
`50 × 0.8 = 40` → `40 × 1.7 = 68d`  
*Key: Strong cards stretch further despite IM compression*  

#### Card 3 (When NOT to use)  
**Front**:  
Why avoid IM 80% + Easy Bonus 170% for long-term retention decks?  
**Back**:  
**Over-aggressive Easy Bonus**:  
- Cards rated "Easy" leap to 68d (example above) → risk memory decay  
- *Better for long-term*: IM 100% + Easy Bonus 130%  

---

### **Pro Tip: Safety Settings**  
Pair this combo with:  
1. **Max Interval Cap**: 45-60d (ensures no card escapes exam date)  
2. **"Hard" Penalty**: 110% (gently resets struggling cards)  
3. **Daily Review Limit**: 200-300 (prevents burnout)  

> **Example Workflow**:  
> - **Pre-exam**: IM 80% + Easy Bonus 170% + Max Interval 60d  
> - **Post-exam**: Revert to IM 100% + Easy Bonus 130% + Max Interval 365d  

This strategy turns Anki into an *exam-specific tuning fork*: vibrating weakly known knowledge into focus while letting solid knowledge resonate at a distance.

## Explain "Hard" Penalty: 110% (gently resets struggling cards) - how to set this up?

Here's a clear breakdown of the **"Hard Penalty"** setting in Anki—how it works, why it's useful, and how to configure it—with medical exam examples:

---

### **What "Hard Penalty" Does**
- **Function**: Multiplies the interval of a card when you rate it **"Hard"**.  
- **Default Value**: 120% (Anki's built-in default).  
- **Your Proposed Value**: **110%** (a "gentler" reset).  

#### **Key Impact**  
| Rating | Default (120%) | Your Setting (110%) |  
|--------|----------------|---------------------|  
| **Hard** | Interval × 1.2 | Interval × 1.1 |  
| **Effect** | Resets interval more aggressively | Subtler reset → *Keeps cards in rotation longer* |  

---

### **Why 110% is "Gentle"**
Imagine a pharmacology card with a **30-day interval**:  
- **Default (120%)**:  
  `30d × 1.2 = 36d` → Card *increases* slightly (counterintuitive!).  
- **Your Exam Setting (110%)**:  
  `30d × 1.1 = 33d` → Barely changes → Card reappears **sooner** but not punished severely.  

**Why this helps struggling cards**:  
- Cards rated "Hard" are *almost known* but need reinforcement.  
- A 110% penalty keeps them **closer to their original interval** → More frequent exposure without demoralizing resets.  

---

### **How to Set It Up**  
#### Step-by-Step Configuration  
1. Open Anki → Click the gear icon next to your deck → **"Options"**  
2. Navigate to the **"Reviews"** tab  
3. Find the setting:  
   **"Hard interval"** (labeled *"Interval multiplier when you answer 'Hard'"*)  
4. Change the value to **110** (default is 120):  
   ![Anki Hard Penalty Setting](https://i.imgur.com/Zk9nYdP.png)  

#### Companion Settings for Exam Prep  
Pair with these for best results:  
| **Setting**         | **Value** | **Function** |  
|---------------------|-----------|--------------|  
| Interval Modifier   | 80%       | Compresses all intervals |  
| Easy Bonus          | 170%      | Rewards "Easy" aggressively |  
| Maximum Interval    | 60d       | Prevents long escapes |  

---

### **Real-World Scenario**  
**Card**: *"Mechanism of metformin"*  
- **Current interval**: 25 days  
- You rate it **"Hard"** (recalled it slowly):  

| **Setting**      | New Interval | Consequence |  
|------------------|--------------|-------------|  
| Default (120%)   | 25d × 1.2 = **30d** | Delays review → Risk of forgetting before exam |  
| **Your (110%)**  | 25d × 1.1 = **27.5d** | Sees it 3 days sooner → Reinforces weak memory |  

---

### **Cards to Cement the Concept**  
#### Card 1 (Mechanics)  
**Front**:  
You rate a card "Hard" with Hard Penalty=110%. If its interval was 40d, what’s the new interval?  
**Back**:  
`40 × 1.1 = 44d`  
*Note: Interval increases slightly but stays close to original.*  

#### Card 2 (Why "Gentle"?)  
**Front**:  
Why is 110% Hard Penalty gentler than default 120% for exam prep?  
**Back**:  
**Delays the card LESS**:  
- 110% → Smaller interval boost → Sooner review  
- Prevents struggling cards from "hiding" until post-exam  

#### Card 3 (Config)  
**Front**:  
To make "Hard" reviews *gentler*, you change:  
A) Hard interval = 110%  
B) New interval = 110%  
C) Easy bonus = 110%  
**Back**:  
**A) Hard interval = 110%**  

---

### When to Use 110% vs. Default  
| **Use 110% Hard Penalty When**      | **Use Default 120% When** |  
|-------------------------------------|----------------------------|  
| Prepping for exams (<3 months)      | Long-term retention        |  
| Cards are "almost known" (slow recall)| Cards truly need full reset |  
| Avoiding ease hell                  | General use                |  

> **Pro Tip**: In the last month before exams, set:  
> - **Hard Penalty = 110%**  
> - **"Again" interval = 50%** (more aggressive reset for forgotten cards)  
> This creates a *tiered* response:  
> - "Again": Major reset (50%)  
> - "Hard": Minor delay (110%)  
> - "Good": Normal progression  
> - "Easy": Large jump (170%)

## What is 'Ease Hell'

"Ease Hell" (or "Low Interval Hell") is a problematic state in Anki where cards with artificially low **ease factors** cause excessively short review intervals, leading to overwhelming daily review loads and burnout. Here’s a breakdown of its causes, mechanics, and solutions, based on Anki’s algorithm:

---

### 🔥 **What Causes Ease Hell?** 
1. **Ease Factor Tanking**:
   - Each card starts with an ease factor of **250%**. 
   - Answering **"Again"** reduces ease by **20%**; **"Hard"** reduces it by **15%**.
   - Answering **"Good"** leaves ease unchanged, while **"Easy"** increases it by **15%**.
   - After repeated lapses (e.g., 6+ **"Again"** responses), ease bottoms out at **130%** – the minimum.

2. **Consequences of Low Ease**:
   - **Intervals grow painfully slow**:  
     - A card at 250% ease: 10d → 25d → 62d.  
     - The same card at 130% ease: 10d → 13d → 17d.  
   - Low-ease cards flood reviews, wasting time on cards you *actually* know.

3. **Why Users Get Trapped**:
   - Avoiding the **"Easy"** button (e.g., during exam prep) prevents ease recovery .
   - Momentary lapses (distraction, fatigue) permanently penalize cards .
   - Anki assumes low ease = "inherently difficult," ignoring contextual memory slips .

---

### ⚠️ **Real-World Impact** 
- **Medical/Language Students**: High-volume decks (e.g., pharmacology, Japanese) become unmanageable.
- **Review Pileups**: 100s of daily reviews for cards that *feel* easy but are stuck at low ease.
- **Burnout Risk**: Users quit Anki due to unsustainable workloads.

---

### 🛠️ **How to Escape Ease Hell** 
#### ✅ **Prevention Strategies**
1. **Longer Learning Steps**:  
   - Use steps like `10m 2h 1d 3d` (not `1m 10m`).  
   - *Why*: Failing cards in the *learning phase* doesn’t tank ease .  

2. **Avoid Overusing "Hard"**:  
   - Reserve **"Hard"** for true struggles; use **"Good"** for normal recall.  

3. **Press "Easy" Strategically**:  
   - If a card feels effortless, use **"Easy"** to boost ease and intervals .  

#### 🔧 **Fixes for Existing Ease Hell**
| **Solution**               | **How It Works**                                  | **Limitations**                     |
|----------------------------|--------------------------------------------------|-------------------------------------|
| **Reset Ease Factors**     | Manually set all cards back to 250% via add-ons or SQL . | Temporary fix; problem may recur. |
| **Increase Interval Modifier** | Apply a global multiplier (e.g., 150%) to stretch all intervals . | Doesn’t address root cause. |
| **Adopt FSRS**             | Anki’s new scheduler ignores ease factors; uses ML to optimize intervals . | Requires setup; not backward-compatible. |
| **Adjust Lapse Settings**  | Set "New Interval" to 20–50% (not 0%) for failed cards . | Reduces penalty but doesn’t fix ease. |

---

### 🤔 **Controversy: Is Ease Hell a Myth?** 
- **Yes, if...**: You press **"Easy"** liberally and design cards well.  
- **No, if...**: You’re prepping for exams and avoid **"Easy"** to force shorter intervals .  
- **FSRS Users**: Report fewer ease issues, but may face "difficulty stagnation" .  

---

### 💡 **Key Takeaway**  
Ease Hell stems from **Anki’s algorithm penalizing lapses too harshly** while making ease recovery difficult. To avoid it:  
- Optimize learning steps for tough material (e.g., `20m 4h 1d` for medical decks).  
- Reset ease factors periodically or switch to **FSRS**.  
- Use **"Easy"** without fear for truly mastered cards .  

> Pro Tip: Track ease factors with add-ons like *True Retention by Card Maturity*. If >20% of mature cards have ease ≤150%, you’re in Ease Hell .