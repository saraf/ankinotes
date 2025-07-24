---
date: '2025-07-16 17:32:24'
layout: post
tags:
- StudyNotes/StudyTech
title: Stability Growth - more details
---

# Stability Growth - more details
Created on: 2025-07-16T23:03:22

Here's a precise yet simple explanation of the stability growth formula, using a **"Memory Investment"** analogy:

### 💡 Core Concept: Stability = Memory Durability
- **Stability (S)**: How long knowledge lasts without review  
- **After review**, your brain "invests" in upgrading this durability  

---

### 🔧 The Investment Formula Simplified
```math
\text{New Stability} = \text{Old Stability} \times \left(1 + \text{Investment Return}\right)
```
Where **Investment Return** =  
```math
\underbrace{f_D}_{\text{Difficulty Tax}} \times \underbrace{f_S}_{\text{Size Fee}} \times \underbrace{f_R}_{\text{Timing Bonus}} \times \underbrace{f_G}_{\text{Effort Reward}}
```

---

### 🧩 Breaking Down the Investors
#### 1. **f₁(D) - Difficulty Tax ("The Leak")**  
   - **What**: Fee charged by *hard material*  
   - **Effect**:  
     - Easy cards (D=1) → 0% tax (full return)  
     - Hard cards (D=10) → 90% tax (only 10% return)  
   - **Formula**: `f₁(D) = (11 - D)/10`  
     *(D=3 → 80% return; D=8 → 30% return)*  

#### 2. **f₂(S) - Size Fee ("Diminishing Returns")**  
   - **What**: Fee for *already-large* memories  
   - **Effect**:  
     - New memories (S=1 day) → 0% fee  
     - Mature memories (S=100 days) → 70% fee  
   - **Formula**: `f₂(S) = 1 / \sqrt{S}`  
     *(S=9 → 33% fee; S=100 → 90% fee)*  

#### 3. **f₃(R) - Timing Bonus ("Struggle Reward")**  
   - **What**: Bonus for reviewing *when almost forgotten*  
   - **Effect**:  
     - Review at R=90% → 10% bonus  
     - Review at R=60% → 40% bonus  
   - **Peak reward**: R=75-80%  

#### 4. **Grade Factor ("Effort Tier")**  
   | Button  | Reward Multiplier |  
   |---------|-------------------|  
   | Again   | Reset (no gain)   |  
   | Hard    | 0.8×              |  
   | Good    | 1.0×              |  
   | Easy    | 1.3×              |  

---

### 🌰 Real Example 
**Card**: Capital of France (S=10 days, D=2)  
**Review**: At R=70% → Press "Good"  
```math
\begin{array}{rl}
f_D &= \dfrac{11 - 2}{10} = 0.9 \\
f_S &= \dfrac{1}{\sqrt{10}} \approx 0.32 \\
f_R &= 0.35 \quad \text{(R = 70\% bonus)} \\
f_G &= 1.0 \\
\text{Return} &= 0.9 \times 0.32 \times 0.35 \times 1.0 \approx 0.10 \\
\text{New S} &= 10 \times (1 + 0.10) = 11~\text{days}
\end{array}
```
*(10% growth for easy card reviewed optimally)*

---

### 💎 Key Insight Card  
**Front**:  
Stability grows through ______, where difficulty acts like ______, current stability like ______, and retrievability like ______.  

**Back**:  
**compounded investment ; a tax ; diminishing returns ; a timing bonus**  
**Extra**:  
> *Formula*:  
> `New S = Old S × [1 + f_D × f_S × f_R × f_G]`  

---

### ⚠️ Pitfall Card  
**Front**:  
True or False: Reviewing a mature card (S=100 days) gives larger *relative growth* than a new card (S=1 day).  
**Back**:  
**False**  
- New card: 1 → 2 days = **100% growth**  
- Mature card: 100 → 110 days = **10% growth**  
*(f₂(S) imposes diminishing returns!)*  

---

### 🌊 Water Tank Analogy Upgrade  
- **Pouring water** = Review effort  
- **Water retained** = `f_D × f_S × f_R × f_G`  
  - `f_D`: Leakiness (high D = leaky tank)  
  - `f_S`: Overflow loss (big tank = spillage)  
  - `f_R`: Rainfall bonus (dry season = bonus water)  
  - `f_G`: Pouring skill (Easy = precise funnel)  

---

### ✅ Why This Matters  
Optimize reviews by:  
1. **Lowering D** (split hard cards) → ↓ tax  
2. **Reviewing at R≈75%** → ↑ timing bonus  
3. **Using "Easy" wisely** → ↑ effort reward  
4. **Accepting slower mature gains** → ↓ frustration  

This transforms abstract parameters into actionable memory investment strategies!