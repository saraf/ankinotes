---
date: '2025-07-18 10:22:50'
layout: post
tags:
- StudyNotes/StudyTech
title: Retrievability should be read as Expected or Predicted Retrievability
---

# Retrievability should be read as Expected or Predicted Retrievability
Created on: 2025-07-18T15:53:09

In many places I feel that 'Retrievability' actually means 'expected retrievability' - since it can be confused with actual retrievabiiity - i.e. how easy it was for me to recall (again, hard, good, easy)

You are absolutely correct—and this is a *very important distinction* in spaced repetition theory and FSRS especially.

### Retrievability: What It Means in FSRS/Anki’s Memory Model

**"Retrievability"** in the context of FSRS (and most memory models, including SM2) refers to the **expected probability of recall** at the time a review is due. It’s sometimes called "**expected retrievability**" or "**predicted retrievability**."

- It is a *model prediction* based on your review history, previous intervals, stability, and difficulty.
- It is *not* how easy it *felt* for you to remember the card at that moment (which is reflected in your response: 'Again', 'Hard', 'Good', 'Easy').

### Why Is This Confusing?

- **Actual retrievability (as felt by you):** How easy or hard it was to recall the card—a subjective experience, rated by your response.
- **Expected retrievability (FSRS/SM2):** The probability (from 0 to 1) that you recall a card, *as predicted by the memory model* at the scheduled time, *before* you review.
  - For example: A card with expected retrievability of 0.9 is predicted by the model to have a 90% chance you'll remember it.

### Why This Matters

- The *grade* you give ("Again"/"Hard"/"Good"/"Easy") says whether you did or didn't recall (and how easy it was).
- The **model** uses the *predicted retrievability* (not your felt experience) to decide how much to adjust stability after your answer.

### Best Practice in Wording

To avoid confusion, you should refer to this as "**expected retrievability**" or "**predicted retrievability**" whenever discussing the model's calculations. Only refer to "actual retrievability" if you mean your *felt* ease or difficulty during recall.

### Example Language

> "In FSRS, 'retrievability' refers to the model's predicted probability that you'll successfully recall an item at the scheduled review time—i.e., expected retrievability—not how easy it *felt* for you to answer that card (which is your response: 'Again', 'Hard', 'Good', or 'Easy')."

**Summary:**  
You are right! "Retrievability" in the Anki/FSRS memory model is best thought of as **expected retrievability** (the model's predicted recall probability), not your subjective recall experience.