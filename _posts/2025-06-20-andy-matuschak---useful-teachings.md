---
date: '2025-06-20 15:51:40'
layout: post
tags:
- StudyNotes/StudyTech
title: Andy Matuschak - Useful teachings
---

# Andy Matuschak - Useful teachings

Channeling **Andy Matuschak’s approach** to spaced repetition (as seen in his essays like *[How to write good prompts](https://andymatuschak.org/prompts/)* and *[Effective spaced repetition systems](https://andymatuschak.org/srs/)*), here’s how to craft prompts that build **actionable, durable knowledge**—not just inert facts:

---

### **Andy’s Core Philosophy: Knowledge as Tools**
> *"Prompts should simulate how you’ll **use** the knowledge in the wild. If it doesn’t change your behavior, it’s trivia."*  
Focus on **generative retrieval** (recalling *how* to apply ideas) over static recall.

---

### **The 3 Deadly Sins of Bad Prompts (Avoid These!)**
1. **"Trivia Traps"**  
   Testing facts without context:  
   *Bad:* "What does AWS IAM stand for?"  
   *Good:* "You need to grant an S3 bucket access to a Lambda function. What IAM construct connects them?"

2. **"Verbatim Warnings"**  
   Rewording a textbook definition:  
   *Bad:* "Define ‘fault tolerance’."  
   *Good:* "Your EC2 instance fails. What AWS service ensures users don’t notice? Why?"

3. **"Isolated Factoids"**  
   Missing connections to prior knowledge:  
   *Bad:* "What’s the max size of an S3 object?"  
   *Good:* "You’re uploading a 6TB database backup. How must you structure the S3 upload? Why?"

---

### **4 Pillars of Andy-Style Prompts**
#### **1. Generative & Transfer-Oriented**  
   *Prompt:*  
   > "A colleague set up an S3 bucket with public read access. What’s the *hidden risk* in their `bucket policy`? How would you fix it?"  
   *Answer:*  
   > Risk: `"Principal": "*"` allows anonymous access → Fix: Restrict to specific IAM roles/VPC endpoints.  

   *Why it works:* Forces *diagnosis* and *action*—not just recalling "block public access."

#### **2. Effortful Retrieval with Clues**  
   *Prompt:*  
   > "To debug ‘403 Forbidden’ errors in API Gateway, what 3 IAM layers must you check? *(Hint: Execution, resource, identity)*"  
   *Answer:*  
   > 1. Resource policy (API GW)  
   > 2. IAM policy (calling user/role)  
   > 3. Authorizer (Lambda/Cognito)  

   *Why it works:* Clues scaffold retrieval without giving answers.

#### **3. Self-Derived Knowledge**  
   *Prompt:*  
   > "Why does Andy argue that ‘cloze deletions’ often create brittle knowledge? What’s his alternative?"  
   *Answer:*  
   > Clozes train pattern-matching, not understanding → Use **application prompts** that require synthesizing concepts.

   *Why it works:* You must *reconstruct his argument*—not parrot it.

#### **4. Procedural & Causal**  
   *Prompt:*  
   > "You enable S3 Versioning. What *new risk* emerges? What service controls it?"  
   *Answer:*  
   > Risk: Accidental overwrites create versions → Cost bloat.  
   > Control: S3 Lifecycle Policies to auto-delete old versions.  

   *Why it works:* Tests understanding of *system dynamics*, not just features.

---

### **Matuschak’s Prompt Patterns for AWS/SRS**
| **Pattern**              | **Bad Prompt**                          | **Andy-Style Prompt**                                  |
|--------------------------|----------------------------------------|--------------------------------------------------------|
| **Debugging Scaffold**   | "What does CloudTrail do?"             | "Your CloudTrail shows no logs. What 2 permissions are missing in the IAM role?" |
| **Tradeoff Analysis**    | "List EBS volume types."               | "Your app needs 16K IOPS at lowest cost. Which EBS type? Why *not* io2?" |
| **Prevention Focus**     | "Define DDoS protection."              | "How would AWS Shield Advanced change your response to a SYN flood attack vs. no Shield?" |
| **Conceptual Analogy**   | "What is VPC Peering?"                 | "How is VPC Peering like a tunnel between offices? What security limits apply?" |

---

### **Why This Works for AWS Cloud Practitioner**
1. **Simulates exam questions:** CLF-C02 tests *scenario-based judgment*, not definitions.  
2. **Builds operational intuition:** Prepares you for real cloud architecture decisions.  
3. **Reduces interference:** Isolates subtle distinctions (e.g., IAM Roles vs. Policies).  

> *Andy’s litmus test:* **"If you answer correctly, will you *do* something differently?"**  
> e.g., After reviewing a card about S3 Lifecycle Policies, you immediately audit your buckets.

---

### **Your Action Plan**
1. **Autopsy bad cards:** Find prompts you keep failing. Rewrite them using:  
   *"When [scenario], how do I [action]? Why [principle]?"*  
2. **Add "why" layers:** For every fact, ask *"What would this help me prevent/build/optimize?"*  
3. **Test in Anki:** Use tags like `#MatuschakStyle` to track rewritten cards’ retention rates.  

*"Knowledge wants to be a verb."* — Andy’s ghost in your SRS. 👻