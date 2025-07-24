---
date: '2025-07-04 18:08:29'
layout: post
tags:
- StudyNotes/StudyTech
title: Cases where Basic Front and Back cards are better than Cloze deletion cards
---

# Cases where Basic Front and Back cards are better than Cloze deletion cards
Created on: 2025-07-04T23:39:01

Yes, there are several cases where **basic Front and Back cards** are better than cloze deletions in Anki:

### When Basic Front/Back Cards Are Better

- **Conceptual or Open-Ended Questions:**  
  When you want to test understanding, reasoning, or the ability to explain a concept in your own words, a basic card is clearer and more effective.  
  *Example:*  
  - Front: "Why does S3 offer high durability?"  
  - Back: "Because it redundantly stores data across multiple devices and facilities."

- **Relationship or Causal Questions:**  
  When you need to explain relationships, causes, or effects, front/back cards allow for more context and depth[5].  
  *Example:*  
  - Front: "What happens if you set an S3 bucket policy to public?"  
  - Back: "Anyone on the internet can access the bucket's contents."

- **Lists or Multi-Part Answers:**  
  If the answer is a list or has multiple parts that don't fit naturally into a single sentence, basic cards are more readable and manageable.  
  *Example:*  
  - Front: "List three AWS services used for compute."  
  - Back: "EC2, Lambda, Elastic Beanstalk."

- **Why/How Questions:**  
  Cloze deletions are best for facts or fill-in-the-blank style recall. For "why" or "how" questions, basic cards are better because they require explanation and synthesis[5].

- **When the Statement Is Not a Natural Sentence:**  
  If the information doesn't fit well into a sentence or is too awkward to cloze, a basic card is clearer.

### When to Use Cloze Deletions

- **Simple facts within a sentence:**  
  Cloze is best for hiding a single word or phrase in a sentence to test recall of that specific detail[2][4].
- **Dense factual material:**  
  When you want to break a complex statement into several recallable facts.

### Summary Table

| Use Case                          | Best Card Type         |
|------------------------------------|-----------------------|
| Conceptual, open-ended, "why/how"  | Basic Front/Back      |
| Relationships/causality            | Basic Front/Back      |
| Lists, multi-part answers          | Basic Front/Back      |
| Simple facts in context            | Cloze Deletion        |
| Dense, detail-heavy statements     | Cloze Deletion        |

**In summary:**  
Use basic Front/Back cards for conceptual, explanatory, or multi-part questions, and cloze deletions for targeted recall of specific facts within a sentence[5]. This approach ensures clarity and maximizes learning efficiency.

[1] https://workbookpdf.com/learn/anki-cloze
[2] https://www.memo.cards/blog/how-to-review-cards-in-anki
[3] https://github.com/matthayes/anki_cloze_anything
[4] https://docs.ankiweb.net/editing.html
[5] https://www.reddit.com/r/medicalschoolanki/comments/ernvn7/cloze_deletion_vs_frontback_which_do_you_prefer/
[6] https://forums.ankiweb.net/t/why-use-the-basic-note-type-when-you-can-use-cloze/40053
[7] https://www.youtube.com/watch?v=MicMAY2TNqY
[8] https://forums.ankiweb.net/t/cloze-overlapper-addon-how-to-have-a-front-and-back/5556
[9] https://docs.ankiweb.net/studying.html
[10] https://www.youtube.com/watch?v=4uIVBkLeCPQ 


Here are **simple examples and counterexamples** illustrating when basic Front/Back cards are better than cloze deletions, and vice versa:

### 1. **Conceptual or Open-Ended Questions**

**Better with Basic Front/Back:**

- **Example:**  
  - Front: Why does S3 offer high durability?  
  - Back: Because it redundantly stores data across multiple devices and facilities.

- **Counterexample (cloze not ideal):**  
  - "S3 offers high durability because it {{c1::redundantly stores data across multiple devices and facilities}}."  
  - This cloze is awkward and doesn’t prompt for an explanation in your own words.

### 2. **Relationship or Causal Questions**

**Better with Basic Front/Back:**

- **Example:**  
  - Front: What happens if you set an S3 bucket policy to public?  
  - Back: Anyone on the internet can access the bucket's contents.

- **Counterexample (cloze not ideal):**  
  - "If you set an S3 bucket policy to public, {{c1::anyone on the internet can access the bucket's contents}}."  
  - This cloze deletion is less natural and doesn’t encourage you to explain the consequence.

### 3. **Lists or Multi-Part Answers**

**Better with Basic Front/Back:**

- **Example:**  
  - Front: List three AWS services used for compute.  
  - Back: EC2, Lambda, Elastic Beanstalk.

- **Counterexample (cloze not ideal):**  
  - "AWS compute services include {{c1::EC2}}, {{c2::Lambda}}, and {{c3::Elastic Beanstalk}}."  
  - Cloze deletions here can fragment your recall and make it harder to synthesize the list as a whole.

### 4. **Why/How Questions**

**Better with Basic Front/Back:**

- **Example:**  
  - Front: How does S3 achieve high availability?  
  - Back: By replicating data across multiple availability zones.

- **Counterexample (cloze not ideal):**  
  - "S3 achieves high availability by {{c1::replicating data across multiple availability zones}}."  
  - This cloze deletion doesn’t prompt for a full explanation or understanding.

### 5. **Simple Facts in Context**

**Better with Cloze Deletion:**

- **Example:**  
  - "Canberra was founded in {{c1::1913}}."  
  - This is a straightforward fact that fits naturally into a cloze deletion[1].

- **Counterexample (basic not ideal):**  
  - Front: Canberra was founded in...?  
  - Back: 1913  
  - While this works, the cloze deletion keeps the context and is more efficient for targeted recall.

### 6. **Dense, Detail-Heavy Statements**

**Better with Cloze Deletion:**

- **Example:**  
  - "The capital of Australia is {{c1::Canberra}} and it was founded in {{c2::1913}}."[1]

- **Counterexample (basic not ideal):**  
  - Front: What is the capital of Australia and when was it founded?  
  - Back: Canberra, 1913  
  - This basic card requires recalling two facts at once, which can be split more efficiently with cloze deletions.

**Summary Table:**

| Use Case                     | Example (Better)             | Counterexample (Not Ideal)      |
|------------------------------|------------------------------|---------------------------------|
| Conceptual/Why/How           | Basic Front/Back             | Cloze Deletion                  |
| Lists/Multi-Part Answers     | Basic Front/Back             | Cloze Deletion                  |
| Simple Facts in Context      | Cloze Deletion               | Basic Front/Back                |
| Dense, Detail-Heavy Facts    | Cloze Deletion               | Basic Front/Back                |

**In short:**  
Use **basic Front/Back cards** for explanations, open-ended questions, and lists. Use **cloze deletions** for targeted recall of specific facts within a sentence[1][2][3][4].

[1] https://docs.ankiweb.net/editing.html
[2] https://github.com/matthayes/anki_cloze_anything
[3] https://docs.ankiweb.net/templates/generation.html
[4] https://www.reddit.com/r/Anki/comments/1c9s5hk/opinions_on_cloze_vs_basic_cards_is_cloze_overall/
[5] https://forums.ankiweb.net/t/why-use-the-basic-note-type-when-you-can-use-cloze/40053
[6] https://ankiweb.net/shared/info/1990296174
[7] https://www.youtube.com/watch?v=MicMAY2TNqY
[8] https://forums.ankiweb.net/t/cloze-cards-to-regular-flashcards/7410
[9] https://www.youtube.com/watch?v=z30xe_qASvs
[10] https://forums.ankiweb.net/t/cloze-overlapper-addon-how-to-have-a-front-and-back/5556