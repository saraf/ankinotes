---
date: '2025-06-25 18:14:59'
layout: post
tags:
- StudyNotes/StudyTech
title: How is Ease Factor different from Interval Modifier
---

# How is Ease Factor different from Interval Modifier

## Difference Between Interval Modifier and Ease Factor in Anki

**Interval Modifier** and **Ease Factor** both influence how long Anki waits before showing you a card again, but they operate at different levels and serve different purposes:

### **Ease Factor**
- **What it is:**  
  The Ease Factor is a property of each individual card. It reflects how easy or difficult that specific card is for you to remember.
- **How it works:**  
  - Every card starts with a default ease factor (usually 250%).
  - When you answer a card:
    - "Good": Ease stays the same.
    - "Easy": Ease increases by 15%.
    - "Hard": Ease decreases by 15%.
    - "Again": Ease decreases by 20%[1][4][8].
  - The next review interval for a card is calculated by multiplying the current interval by the card’s ease factor (and other modifiers)[6][8].
- **Scope:**  
  - **Per-card:** Each card’s ease factor changes based on your performance with that card.
  - **Long-term memory:** Cards you struggle with will show up more often because their ease drops; cards you find easy will be scheduled further apart.

### **Interval Modifier**
- **What it is:**  
  The Interval Modifier is a deck-wide setting. It multiplies the intervals for all cards in a deck, regardless of their individual ease factors.
- **How it works:**  
  - If set to 100% (1.0), intervals are unchanged.
  - If set to 80% (0.8), all intervals are shortened by 20%.
  - If set to 120% (1.2), all intervals are lengthened by 20%[1][3][6].
- **Scope:**  
  - **Per-deck:** Applies to every card in the deck equally, regardless of individual ease.
  - **Global adjustment:** Useful if you want all cards in a deck to come up more or less frequently, such as for particularly difficult or easy material.

### **How They Work Together**
- When you review a card, the new interval is calculated as:
  $$
  \text{New Interval} = \text{Current Interval} \times \text{Ease Factor} \times \text{Interval Modifier}
  $$
  (plus other bonuses or modifiers depending on your answer)[6][5].

### **Summary Table**

| Feature           | Applies To         | Changes Over Time? | Typical Use                                  |
|-------------------|-------------------|--------------------|----------------------------------------------|
| Ease Factor       | Individual cards  | Yes, per answer    | Adjusts interval based on card difficulty    |
| Interval Modifier | Whole deck        | No, unless changed | Adjusts all intervals for a deck uniformly   |

### **Why the Difference Matters**
- **Ease Factor** personalizes scheduling for each card, adapting to your memory of that fact.
- **Interval Modifier** is a blunt tool to make a whole deck easier or harder, regardless of individual card performance.

**In summary:**  
*Ease Factor* is dynamic and card-specific, reflecting how well you remember each fact, while *Interval Modifier* is a static, deck-level setting that scales all intervals up or down for every card in the deck[1][3][6][8].

[1] https://forums.ankiweb.net/t/deck-options-explained/213
[2] https://www.reddit.com/r/Anki/comments/av3r24/converting_between_interval_modifier_and_ease/
[3] https://docs.ankiweb.net/deck-options.html
[4] https://readbroca.com/anki/ease-hell/
[5] https://zhighley.com/anki-settings/
[6] https://gist.ly/youtube-summarizer/dissecting-anki-intervals-and-learning-steps-a-complete-no-fluff-guide
[7] https://eshapard.github.io/anki/thoughts-on-a-new-algorithm-for-anki.html
[8] https://www.youtube.com/watch?v=1XaJjbCSXT0