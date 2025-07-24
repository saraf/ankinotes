---
date: '2025-06-19 15:16:43'
layout: post
tags:
- StudyNotes/StudyTech
title: Michael Nielsen paper based tutorial - augmenting long term memory
---

# Michael Nielsen paper based tutorial - augmenting long term memory

The article — **[“Augmenting Long-term Memory”](https://augmentingcognition.com/ltm.html)** by Michael Nielsen — is a masterwork. It presents a **vision of learning** where you **deliberately build long-term memory** as a way to **augment your thinking and creativity**, not just memorize facts.

Here’s a **pragmatic, actionable tutorial** that distills and applies the key principles of that essay to your context — **a senior developer-architect learning AWS and teaching a team**.

---

## 🎯 Core Insight

> **Memory isn’t just storage. It’s a foundational tool for thinking.**

We often think: “I don’t need to memorize; I can Google it.”
But this misses the point:

> You can only *think deeply* about what you can *hold in your head*.

---

## 🧰 Goals of This Tutorial

You will learn to:

1. Create **atomic**, **meaningful** flashcards.
2. Use spaced repetition (Anki) **strategically**, not obsessively.
3. Build a **knowledge scaffolding** that amplifies your problem-solving.
4. Teach others using these same techniques.

---

## 🧠 Step 1: Make Memory a First-Class Goal

> “Deliberate memory creation is not rote memorization. It is *precision engineering* of your future cognitive toolkit.”
> — Michael Nielsen

Don’t make cards about everything.
Make cards for things you want **at your fingertips** while thinking or designing.

### Ask:

* What should I *not* have to look up when coding or designing?
* What concepts are like **joints in the skeleton** of this subject?
* What facts unlock or collapse mental effort when solving a problem?

✅ **Examples (good):**

* “What does IAM stand for, and why is it foundational in AWS?”
* “What AWS service lets you trigger code in response to S3 uploads?”
* “What’s the difference between `Provisioned` and `Reserved` concurrency in Lambda?”

🚫 **Bad (rote):**

* “The pricing tiers of DynamoDB in cents per GB per month.”
* “The exact syntax of a boto3 method call.”

(Unless you *personally* need those — this is contextual.)

---

## 🛠 Step 2: Design Atomic, Thoughtful Cards

### Nielsen’s Rule:

> “A good memory question produces a brief moment of *desirable difficulty*, not a tedious struggle.”

So, break ideas down:

Instead of:

> Q: “What are the three pillars of the AWS Well-Architected Framework?”

Make:

* Q1: “Which pillar of AWS WAF relates to limiting blast radius of failure?”
* Q2: “What AWS WAF pillar emphasizes cost-effectiveness?”
* Q3: “Name 1 pillar of AWS WAF that helps you monitor and improve systems.”

👉 Each card = **1 fact or distinction**, with **context or a clue**.

---

## 🧠 Step 3: Use Retrieval to Deepen Thinking

Don’t just memorize. Use Anki to *interrogate your own ideas*.

> “Spaced repetition is most powerful when it operates on **rich, meaningful representations**.” — Nielsen

### In practice:

* After watching 10 mins of Nick Garner’s AWS video, **pause**.
* Ask: “What are the *3 most important ideas* I want to keep forever?”
* Write them as **questions**, not summaries.

Use **prompts**, **cloze deletions**, or **self-explanation** cards.

🟢 Example prompt card:

```html
Q: What happens behind the scenes when you deploy to AWS Elastic Beanstalk?
A: It provisions an EC2 instance, sets up an environment, loads the application bundle, and monitors health with ELB and CloudWatch.
```

🟢 Self-explanation (great for building depth):

```html
Q: Explain in your own words how SQS differs from SNS.
```

---

## 🗃 Step 4: Organize Cards by Meaning, Not Topic

Don’t try to “cover” the syllabus.
Try to **grow a web of interlocking concepts**.

Use Anki **tags** and **hierarchical decks** to reflect how you think:

* `aws::lambda`
* `aws::networking`
* `aws::mental_models`

This way, when reviewing or teaching, you can focus reviews on **key systems** instead of arbitrary topics.

---

## 🔁 Step 5: Review Strategically (Don’t Let It Become a Chore)

You already experienced **Anki fatigue** while learning Kanji. That’s real.

So:

* **Keep daily reviews small** (20–40 cards/day max unless preparing for a test).
* **Delete cards** that are not useful. Be ruthless.
* **Merge cards** if they feel fragmented.
* **Skip reviews** when sick or overloaded. Then **triage** later.

Use **Anki’s “Ease” buttons** to make boring or obvious cards reappear less frequently.

---

## 🎓 Bonus: Use the Technique as a Teacher

With your team:

* Instead of giving them notes or documents — **give them questions**.
* Create Anki decks with **cloze cards and hints**.
* Run **weekly “quiz circles”** where each engineer brings 3 questions based on what they learned that week.

This builds:

* Individual memory
* Team-wide epistemic clarity

---

## 📚 Recommended Tools + Resources

| Resource                                                                              | Why it’s useful                                             |
| ------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [Augmenting Long-Term Memory](https://augmentingcognition.com/ltm.html)               | Original essay — worth rereading deeply                     |
| [Effective Anki](https://docs.ankiweb.net)                                            | Official manual — search for “card types” and “ease factor” |
| [Michael Nielsen’s Quantum Anki Cards](https://quantum.country/qcvc)                  | Interactive tutorial on Anki use                            |
| Add-on: [Hint Hotkeys](https://ankiweb.net/shared/info/1844908621)                    | Use hints to scaffold recall                                |
| Add-on: [Custom CSS and JS per note type](https://ankiweb.net/shared/info/1666520655) | Advanced control for Anki deck UX                           |

---

## 🧠 In 5 Sentences

1. Deliberately growing your memory is a force multiplier on thinking.
2. Spaced repetition (Anki) is a tool for making facts fluent and durable.
3. Focus only on knowledge worth **having at your mental fingertips**.
4. Make each card **atomic**, **meaningful**, and **connected to your thinking**.
5. Teach and reinforce via prompts, not lectures.

---

Would you like me to create a **template deck + guide** based on this workflow — tailored to your AWS Developer Associate course?