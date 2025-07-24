---
date: '2025-07-13 06:56:30'
layout: post
tags:
- StudyNotes/StudyTech
title: Connection between Desired Retention and Stability/Stability Growth in Anki
  with FSRS?
---

# Connection between Desired Retention and Stability/Stability Growth in Anki with FSRS?
Created on: 2025-07-13T12:28:10

Here's a clear, simple explanation of how **Desired Retention** connects to **Stability** and **Stability Growth** in Anki with FSRS:

### 🎯 Desired Retention = Your "Memory Goal"
- **What it is**: The target probability you'll remember a card at review time  
  *(Default: 90% = "Remember 9 out of 10 cards")*
- **Where to set**: `Preferences > FSRS > Desired Retention slider`

---

### 🔄 How It Controls Stability
| **Desired Retention** | **Effect on Stability (S)** | **Real-World Analogy** |  
|------------------------|------------------------------|------------------------|  
| **Higher (95%)**       | → Smaller S growth           | Tightrope walker - small safe steps |  
| **Lower (85%)**        | → Larger S growth            | Marathon runner - big endurance leaps |  

**Why?**  
- FSRS adjusts intervals to hit *your exact retention target*  
- Higher retention = **Shorter intervals** = Less forgetting risk but slower S growth  
- Lower retention = **Longer intervals** = More forgetting risk but faster S growth  

---

### ⚙️ The Mathematical Link
FSRS calculates intervals using:  
```math
I = \frac{S}{\ln(R_{\text{desired}})} \times \text{DifficultyFactor}
```
- **I** = Next interval  
- **S** = Current stability  
- **R_desired** = Your chosen retention (e.g., 0.9)  

**Example**:  
- Card with S=30 days at R_desired=90%:  
  ```math
  I = \frac{30}{\ln(0.9)} ≈ \frac{30}{-0.105} ≈ 286\ days
  ```
- Same card at R_desired=80%:  
  ```math
  I = \frac{30}{\ln(0.8)} ≈ \frac{30}{-0.223} ≈ 134\ days
  ```

---

### 🌱 How This Affects Stability Growth
1. **Higher R_desired (95%)**:  
   - Reviews happen *sooner*  
   - You see cards at high retrievability (R≈95%)  
   - **Result**: Smaller stability gains (ΔS↓)  
   - *Like gently watering a plant daily → slow growth*  

2. **Lower R_desired (80%)**:  
   - Reviews happen *later*  
   - You see cards at lower retrievability (R≈60-80%)  
   - **Result**: Larger stability gains (ΔS↑)  
   - *Like deep watering weekly → explosive growth*  

---

### 📊 Trade-offs Summarized
|                      | R_desired=95%          | R_desired=85%          |  
|----------------------|------------------------|------------------------|  
| **Stability Growth** | Slow & steady          | Fast & risky           |  
| **Reviews**          | More frequent          | Less frequent          |  
| **Forgotten Cards**  | Fewer (5%)             | More (15%)             |  
| **Best For**         | Exams, high-stakes     | Leisure learning       |  

---

### 💡 Key Insight Card  
**Front**:  
In FSRS, setting higher Desired Retention ______ stability growth because reviews occur at ______ retrievability (R).  

**Back**:  
**reduces ; higher**  
*(High R → smaller stability gains per review)*  

**Extra**:  
> *Formula Insight:*  
> `Interval ∝ Stability / ln(DesiredRetention)`  
> Higher retention denominator → Smaller intervals → Less stability growth  

### 🔧 Optimization Tip  
**Want faster long-term growth?** Temporarily lower retention to 85% for mature cards:  
1. `deck:Mature prop:s>30`  
2. `Set R_desired=85%`  
3. Enjoy 30% larger stability jumps!  

*(Switch back to 90% for new/unstable cards)*  

This reveals the core FSRS trade-off: **Tighter memory control (high retention) vs. faster long-term growth (low retention)**. The choice depends on whether you prioritize short-term reliability or long-term efficiency!