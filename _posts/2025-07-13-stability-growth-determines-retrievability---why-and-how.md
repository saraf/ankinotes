---
date: '2025-07-13 06:38:20'
layout: post
tags:
- StudyNotes/StudyTech
title: Stability Growth determines Retrievability - Why and How
---

# Stability Growth determines Retrievability - Why and How
Created on: 2025-07-13T12:08:46

### The Relationship Between Stability Growth and Retrievability  
**Stability Growth (ΔS)** determines future **Retrievability (R)** by reshaping the *forgetting curve* - here's the precise cognitive mechanism:

---

### 🔬 Core Mechanism: The Forgetting Curve Remodeling  
```math
R(t) = e^{-t/S_{\text{new}}}
```
**Where:**  
- $S_{\text{new}} = S_{\text{old}} + \Delta S$ *(Updated stability after growth)*  
- $t$ = Time since last review  
- $R(t)$ = Probability of recall at time $t$  

**How Stability Growth Improves Retrievability:**  
1. **Before Growth** (Small S):  
   - Rapid decay: R drops to 50% in 5 days  
   ```math
   R(5) = e^{-5/10} = 61\%  \ \ \ (S=10)
   ```
2. **After Growth** (Larger S):  
   - Slower decay: R stays at 85% for 5 days  
   ```math
   R(5) = e^{-5/20} = 78\%  \ \ \ (S=20)
   ```  
   **ΔS=10 → 17% higher retention!**

---

### 🧠 Cognitive Psychology Basis  
1. **Synaptic Consolidation** (Dudai, 2012):  
   - Stability growth → **Increased dendritic spines**  
   - More neural pathways → Slower signal decay  

2. **Transfer Theory** (McClelland, 1995):  
   - Hippocampal memory (fragile) → Cortical memory (stable)  
   - ΔS measures **transfer completeness**  

3. **Retrieval Strength Paradox** (Bjork, 2011):  
   > "High current retrievability *reduces* stability gains, while low retrievability *maximizes* them"  
   - Thus: Big ΔS at low R → Future high R  

---

### 🌊 Water Tank Analogy Upgrade  
| **Tank System**       | **Memory Equivalent**          | **Retrievability Effect**       |  
|------------------------|--------------------------------|---------------------------------|  
| Expanding tank walls   | Stability growth (ΔS)          | Slower water level drop         |  
| New capacity: 200L → 300L | S=20d → S=30d              | 50% level now takes 15d vs 10d  |  
| Reinforced materials   | Protein synthesis (LTP)        | Reduced "leakage" over time     |  

**Why this determines R:**  
- **Larger tank** = More water buffer before "empty" (R=0%)  
- **Stronger walls** = Slower leakage (gradual forgetting)  

---

### ⚡ Real-World Example: Language Learning  
1. **New word**: `S=2 days`  
   - R drops to 40% by day 2 → *Hard recall*  
   - Successful review → **ΔS=+300%** (S=8 days)  

2. **After growth**:  
   - Day 2: R=88% (was 40%)  
   - Day 7: R=41% (previously impossible)  

---

### 💎 Summary Card  
**Front**:  
Stability growth (ΔS) determines future retrievability by ______.  

**Back**:  
**Reshaping the forgetting curve**  
- Formula: $R(t) = e^{-t/S_{\text{new}}}$  
- Higher S → Slower R decay  
**Extra**:  
> *"ΔS is the engine, R is the speedometer - one sets the other's limits"*  

### 🔄 Cause-Effect Card  
**Front**:  
If stability grows from 10→15 days, how does R at t=7d change?  
**Back**:  
```math
R_{\text{old}} = e^{-7/10} = 50\% → R_{\text{new}} = e^{-7/15} = 63\%  
```  
*(26% relative improvement)*  

---

### 🧩 Why This Matters in Practice  
1. **Optimal Scheduling**:  
   - Target reviews when R≈90% → Maximizes ΔS → Improves future R  

2. **Troubleshooting**:  
   - Consistently low R? → Need larger ΔS (atomize cards, add mnemonics)  

3. **FSRS Optimization**:  
   ```python
   if predicted_R < 0.85: 
       schedule_soon()  # Boost ΔS opportunity
   ```

This reveals why struggling with cards (low R) is valuable - it fuels the stability growth that makes future recall effortless!