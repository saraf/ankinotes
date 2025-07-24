---
date: '2025-06-23 07:19:50'
layout: post
tags:
- StudyNotes/StudyTech
title: When to use Custom Scheduling or Review Settings
---

# When to use Custom Scheduling or Review Settings

## Concrete Example: When Custom Scheduling or Different Review Settings Are Needed

A good example is **learning a foreign language and preparing for a medical exam at the same time**. Each subject has different review needs, so you would benefit from custom scheduling or separate review settings for each deck.

### **Scenario**

- **Deck 1: Language Learning (e.g., Spanish Vocabulary)**
  - You want to review new words very frequently at first, then gradually space them out.
  - Example settings:
    - Learning steps: 10min, 1h, 1h, 1d, 2d, 3d, 5d, 7d, etc.
    - Remove the "fuzz factor" (randomization of intervals) for more predictable review times.
    - You want to see both directions (Spanish→English and English→Spanish) in the same session, so you adjust the sibling burying and review order[5].

- **Deck 2: Medical Exam Prep (e.g., Pharmacology)**
  - You have a large volume of material and want to avoid overwhelming daily reviews.
  - Example settings:
    - Longer learning steps: 20min, 4h, 1d, 3d.
    - Maximum interval capped at 30 days, so you see cards more often before the exam.
    - Increase the "easy bonus" so cards you know well are spaced out even more[3].

### **Why Custom Scheduling?**

- **Different Memory Demands:** Vocabulary requires frequent, short-term repetition; exam facts may need less frequent, but more sustained, review.
- **Personal Preferences:** You might prefer to see motivational cards or reminders at a fixed interval (e.g., every 3 months), regardless of how you answer them[2].
- **Exam Deadlines:** For time-limited studying (like exams), you might want to cap intervals so nothing is postponed until after your test date[3].

### **How This Works in Anki**

- You set up **custom deck options** for each deck, adjusting learning steps, interval modifiers, maximum intervals, and other settings as needed[1][3][5].
- This ensures each subject is reviewed at the optimal frequency for your goals, making your study more efficient and tailored to your needs.

**Summary:**  
You need custom scheduling or different review settings when you have decks with different learning goals, memory demands, or deadlines—such as language learning (frequent review, custom intervals) versus exam prep (capped intervals, different review pacing)[1][3][5].

[1] https://forums.ankiweb.net/t/custom-scheduling-help/55761
[2] https://www.reddit.com/r/Anki/comments/186ammo/custom_scheduling_see_some_cards_regularly/
[3] https://forums.ankiweb.net/t/custom-scheduling-v3-add-deck-related-info/24147
[4] https://forums.ankiweb.net/t/custom-scheduling-through-js-scripts-inquiry/55814/3
[5] https://forums.ankiweb.net/t/custom-scheduling-through-js-scripts-inquiry/55814
[6] https://github.com/open-spaced-repetition/fsrs4anki
[7] https://docs.ankiweb.net/deck-options.html
[8] https://community.ankihub.net/t/implementing-custom-scheduler-fsrs-on-a-per-deck-basis-with-ankihub-syncing/35