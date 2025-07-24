---
date: '2025-07-23 07:01:26'
layout: post
tags:
- StudyNotes/StudyTech
title: Desired Retention = Desired Retrievability
---

# Desired Retention = Desired Retrievability
Created on: 2025-07-23T12:32:11

**Desired Retention** and **Desired Retrievability** refer to the same concept in FSRS (Free Spaced Repetition Scheduler): the minimum probability that you want to have of recalling a card when it becomes due for review.

- **Desired Retention** is the target probability that you will correctly recall a card at the scheduled review time. For example, a desired retention of 0.9 means the scheduler aims for you to have a 90% chance of recall when the card comes up for review[6][8].
- **Desired Retrievability** can be used interchangeably, referring to the retrievability threshold (i.e., probability of correct recall) that triggers the next review[2][5][8].

Both terms refer to the exact same value in FSRS settings and mathematics—the threshold probability of recall at which the scheduler plans your next review[2][6][8]. In implementation and documentation, "desired retention" and "desired retrievability" are synonymous in FSRS.

**Key points:**
- FSRS schedules reviews so that, when a card is due, your predicted probability of recall (retrievability) is at or just above your desired retention/desired retrievability value[6][8].
- After review, the retrievability jumps close to 100% and gradually decays; when it reaches the set threshold (e.g., 90%), it’s time for another review[7][8].

Sometimes in literature, "retention" and "retrievability" have subtle distinctions, but in the context of FSRS configuration, **Desired Retention = Desired Retrievability**[2][6][8].

[1] https://www.reddit.com/r/Anki/comments/15mab3r/fsrs_explained_part_1_what_it_is_and_how_it_works/
[2] https://help.remnote.com/en/articles/9337171-understanding-spaced-repetition
[3] https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler
[4] https://forums.ankiweb.net/t/retrievability-vs-retention/51764
[5] https://www.youtube.com/watch?v=OqRLqVRyIzc
[6] https://pypi.org/project/fsrs/
[7] https://www.politesi.polimi.it/retrieve/b39227dd-0963-40f2-a44b-624f205cb224/2022_4_Randazzo_01.pdf
[8] https://journal.jngjourney.com/index.php?post%2F2024%2F12%2F28%2FFree-Spaced-Repetition-Scheduler
[9] https://write.justanexperiment.com/%F0%9F%8F%A1-earth/Neuroscience/Memory/Spaced-Repetition
[10] https://docs.ankiweb.net/deck-options.html


Created on: 2025-07-23T12:32:29

## FSRS: Retention vs Retrievability

In FSRS (Free Spaced Repetition Scheduler), **retention** and **retrievability** are closely related but represent two distinct concepts. Understanding their difference is crucial for interpreting FSRS settings and statistics:

### Retention

- **Definition:** In FSRS, retention usually refers to the *desired retention*—the percentage probability that a card will be recalled correctly at its *scheduled review* time. For example, a desired retention of 90% means the system aims for you to recall 90% of your cards when they are due for review.
- Retention can also refer to *true retention*, which is the actual recall rate achieved, measured from your review history.
- Retention is about your performance at the moment cards are scheduled for review, not across all moments you might see them[1][2][3].

### Retrievability

- **Definition:** Retrievability is the *current probability* of recalling a particular card at any given moment, based on its forgetting curve. Each card's retrievability starts at 100% right after review and *decays* over time[4][5].
- *Average retrievability* (sometimes formerly called *average predicted retention*) is the mean probability of recalling any card in your deck *today*—not just the ones scheduled for review.
- Retrievability is continuously changing, whereas retention is focused on one point in time: the review[1][4][6][7].

### Comparison Table

| Term            | Definition                                                                               | FSRS Role                                  |
|-----------------|-----------------------------------------------------------------------------------------|--------------------------------------------|
| Retention       | % of cards recalled at their scheduled review time (usually set as a target, e.g. 90%)   | Determines review frequency and goal       |
| Retrievability  | Probability of recalling a card at any given time (based on forgetting curve for each)   | Predicts current recall ability per card   |

### Key Nuances

- **They are not the same:** Retention (in FSRS) is a *target* for scheduling reviews, while retrievability is the *current, predicted state* of memory for each card[1][4][7].
- **Relationship:** Reviews are scheduled when the card’s retrievability decays to the desired retention threshold. For instance, if desired retention is 90%, reviews are timed so predicted retrievability drops to 90%[4].
- **Measuring Knowledge:** Average retrievability gives an estimate of your total “knowledge” (what you could recall at this moment), not just at the review boundary[1][6].

### Summary

- **Retention:** What you want to achieve at review time (a threshold).
- **Retrievability:** The continuous probability of recall, which FSRS tracks and uses to determine when to review a card[1][4][7].

They are related but *not interchangeable*; FSRS uses both concepts to optimize your study schedule.

[1] https://expertium.github.io/Retention.html
[2] https://www.reddit.com/r/Anki/comments/1anfmcw/you_dont_understand_retention_in_fsrs/
[3] https://github.com/open-spaced-repetition/fsrs4anki/wiki/The-optimal-retention
[4] https://borretti.me/article/implementing-fsrs-in-100-lines
[5] https://expertium.github.io/Algorithm.html
[6] https://help.remnote.com/en/articles/9337171-understanding-spaced-repetition
[7] https://forums.ankiweb.net/t/retrievability-vs-retention/51764
[8] https://forums.ankiweb.net/t/clarify-what-optimal-retention-means/42803
[9] https://www.youtube.com/watch?v=OqRLqVRyIzc
[10] https://www.youtube.com/watch?v=uo-qQvOZDfg
[11] https://www.quizcat.ai/blog/fsrs-algorithm-next-gen-spaced-repetition
[12] https://www.reddit.com/r/Anki/comments/1be6f4s/true_retention_vs_card_retrievability/
[13] https://anki-decks.com/blog/post/anki-fsrs-explained/
[14] https://www.youtube.com/watch?v=ZvrAw_T7A_4
[15] https://community.ankihub.net/t/anki-fsrs-retention-for-im-shelf-too-much-above-90/424027
[16] https://docs.ankiweb.net/deck-options.html
[17] https://feedback.remnote.com/p/fsrs-compute-minimum-recommended-retention
[18] https://www.reddit.com/r/Anki/comments/15mab3r/fsrs_explained_part_1_what_it_is_and_how_it_works/
[19] https://community.ankihub.net/t/question-about-retention-w-fsrs/351510
[20] https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler