---
date: '2025-06-25 17:11:20'
layout: post
tags:
- StudyNotes/StudyTech
title: What is the Ease Factor in Anki
---

# What is the Ease Factor in Anki

Here's the simplest explanation of **Ease Factor** (often called "Ease") in Anki:

---

### 🎯 **Ease Factor = Your Card's "Memory Strength Multiplier"**  
Imagine it as a **personalized growth rate** for *each card*.  
It determines **how much LONGER** a card waits between reviews when you answer **"Good"**.

---

### ⚙️ **How It Works**  
1. **Every card starts at 250% ease** (Anki's default).  
2. **When you review**:  
   - `New Interval = Previous Interval × Ease Factor`  
   - *Example*:  
     - Card interval = 10 days  
     - Ease = 250%  
     - After **"Good"** → `10 × 2.5 = 25 days`  

---

### 🔄 **How Your Ratings Change Ease**  
| **Rating** | **Effect on Ease** | **What Happens** |  
|------------|-------------------|------------------|  
| **Again**  | Ease **‑20%**     | Card resets → Ease drops → Future intervals grow SLOWER |  
| **Hard**   | Ease **‑15%**     | Interval barely grows → Card returns sooner |  
| **Good**   | Ease **unchanged**| Interval multiplies normally |  
| **Easy**   | Ease **+15%**     | Interval grows FASTER → Card stays away longer |  

---

### 💡 **Key Insight**  
- **High Ease (e.g., 250%)** = Card "graduates" quickly → Fewer reviews  
  `10d → 25d → 62d → 155d`  
- **Low Ease (e.g., 130%)** = Card "stalls" → More reviews  
  `10d → 13d → 17d → 22d`  

---

### 🌟 **Why Ease Matters**  
- **Self-correcting**: Cards you struggle with (**"Again"**/**"Hard"**) get *lower ease* → seen more often.  
- **Rewards mastery**: Cards you ace (**"Easy"**) get *higher ease* → seen less often.  
- **Danger zone**: If ease drops too low (**<150%**), you enter **[Ease Hell](https://faqs.ankiweb.net/what-is-ease-hell.html)** → cards get "stuck" in short intervals.

---

### 🔍 **See Ease in Anki**  
1. Enable **"Show Ease"** in card browser:  
   `Browse → Select card → Right-click → "Fields..." → Check "Ease Factor"`  
2. Or install the **"Advanced Review Browser"** add-on.  

---

### 🚫 **Avoid This Mistake**  
**Never** press **"Hard"** for cards you know well!  
- Why? It *lowers ease* → traps cards in frequent reviews.  
- **Better**: Use **"Good"** for normal recall, **"Easy"** for effortless cards.

---

### ⚖️ **Ease vs. Interval Modifier**  
| **Ease Factor**          | **Interval Modifier** |  
|--------------------------|------------------------|  
| *Per-card* setting       | *Deck-wide* setting    |  
| Self-adjusts (based on ratings) | Fixed (you set it manually) |  
| Default: 250%            | Default: 100%          |  

> 💡 **Pro Tip**: In **FSRS** (Anki's modern scheduler), ease factors are *replaced* by AI-driven memory stability predictions.  
> *(Enable in Anki 23.10+ via `Tools → FSRS Helper`)*  

### Example Card to Test Understanding  
**Front**  
After rating a card "**Hard**", does its ease factor:  
A) Increase  
B) Decrease  
C) Stay the same  
**Back**  
**B) Decreases by 15%**  
→ Future intervals grow slower → You'll see it more often!