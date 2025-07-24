---
date: '2025-07-23 15:14:02'
layout: post
tags:
- StudyNotes/StudyTech
title: Cloze Overlapping - what are Steps?
---

# Cloze Overlapping - what are Steps?
Created on: 2025-07-23T20:44:16

Let’s unpack the **“ideal steps”** in the Cloze Overlapper plugin with a **clear, detailed example** using real Sanskrit text.

---

## 🔁 **What Are “Steps” in Practice?**

The `Steps` field in Cloze Overlapper tells Anki how to build a **series of cloze cards**, each hiding a **progressively overlapping portion** of the verse.

### 👇 Format Recap:

```
[Number of tokens per card] [Number of overlapping tokens between cards]
```

For example:

```
3 2
```

Means:

* Each card will have 3 tokens (words),
* Each new card will **share 2 tokens** with the previous one.

---

## 📘 Example: Patanjali Yogasutra 1.2

**Original Verse**:

```
yogaḥ citta vṛtti nirodhaḥ
```

Let’s tokenize this (using space as separator):

```
[1] yogaḥ  
[2] citta  
[3] vṛtti  
[4] nirodhaḥ
```

---

## 🔎 Example with Steps `2 1`

You want to learn **2 words at a time**, with a 1-word overlap between cards.

### Resulting Cards:

1. **Card 1**
   Cloze: `{{c1::yogaḥ citta}} vṛtti nirodhaḥ`
   → You are asked to recall "yogaḥ citta"

2. **Card 2**
   Cloze: `yogaḥ {{c1::citta vṛtti}} nirodhaḥ`
   → Recall "citta vṛtti"

3. **Card 3**
   Cloze: `yogaḥ citta {{c1::vṛtti nirodhaḥ}}`
   → Recall "vṛtti nirodhaḥ"

### ✅ Benefits:

* Low difficulty — you only recall two words at a time.
* Strong contextual overlap between cards.
* Good for **beginners** or unfamiliar vocabulary.

---

## 🔎 Example with Steps `3 2`

Now you want to learn **3 words at a time**, still overlapping 2 of them with each new card.

### Resulting Cards:

1. **Card 1**
   Cloze: `{{c1::yogaḥ citta vṛtti}} nirodhaḥ`

2. **Card 2**
   Cloze: `yogaḥ {{c1::citta vṛtti nirodhaḥ}}`

> Notice how the middle part of each card overlaps with the next. You build from a foundation.

### ✅ Benefits:

* Slightly more difficult.
* More efficient (fewer cards).
* Great for intermediate learners.

---

## 🔎 Example with Steps `1 1`

You're learning **one word at a time** with **complete overlap**:

1. `{{c1::yogaḥ}} citta vṛtti nirodhaḥ`
2. `yogaḥ {{c1::citta}} vṛtti nirodhaḥ`
3. `yogaḥ citta {{c1::vṛtti}} nirodhaḥ`
4. `yogaḥ citta vṛtti {{c1::nirodhaḥ}}`

### ✅ Use When:

* You want total control and precision.
* Very complex or dense philosophical phrases.

---

## 🎯 Ideal Steps: How to Choose

| Skill Level         | Recommended Steps | Why                             |
| ------------------- | ----------------- | ------------------------------- |
| **Beginner**        | `2 1` or `1 1`    | Smaller chunks, easier recall   |
| **Intermediate**    | `3 2`             | Balanced efficiency and context |
| **Advanced**        | `4 2`, `5 3`      | Fewer cards, faster learning    |
| **Recitation Goal** | `3 2` + audio     | Reinforces rhythm and fluency   |

---

## 🧘 Use Case: Yogasutra Study

Let’s say you're working through *Samādhi Pāda* and want to truly **understand and recite each sutra**:

* Use **`2 1`** for early sutras (they’re dense!).
* Once familiar, switch to **`3 2`** to review and reinforce.
* Add **translation or commentary** in the "Extra" field to deepen your insight.

---

## 🔧 Bonus: Adjusting the Separator

For Sanskrit, sometimes a **custom separator** improves tokenization.

For example:

* If you're entering one **word per line**, set:

  ```
  Separator: \n
  ```
* If using `॥` to mark the end of a segment, use:

  ```
  Separator: ॥
  ```

---

## ✅ Summary: Ideal Steps

| Steps | Use When...                         | Result                            |
| ----- | ----------------------------------- | --------------------------------- |
| `1 1` | You're new or learning word-by-word | Many easy cards                   |
| `2 1` | You want a balance of ease and flow | Slight challenge, good for sutras |
| `3 2` | You're getting comfortable          | Fewer cards, stronger context     |
| `4 2` | You're reviewing or reinforcing     | Most efficient, harder recall     |

---

Would you like a table generator or small tool to preview what a specific Steps configuration would produce for any verse you input? I can build that for you here.