---
date: '2025-07-12 07:23:11'
layout: post
tags:
- StudyNotes/StudyTech
title: Image Occlusion Advanced - explanatory Q and A for cards
---

# Image Occlusion Advanced - explanatory Q and A for cards
Created on: 2025-07-12T12:53:39

Say - I have three masks on one image. And I am generating three hide-one-guess-one cards. 
When any of these three cards are displayed when reviewing, I would like to display some question text connected with the masked region when the Front is shown, and I would like to display some explanatory text that is connected to the answer when the masked region is revealed. How can I achieve this?


Created on: 2025-07-12T12:53:46

**Image Occlusion Enhanced** does not natively allow you to link a unique text question and answer to each individual mask/occlusion within a single note. The fields you add to the note (like “Text Question” or “Text Answer”) are shared across all cards generated from that note, not specific to each mask.

### What is possible with current features:

#### 1. **Using the Label Tool for Mask-Specific Questions**
- When you create or edit a mask in the Image Occlusion Editor, you can use the **label tool** (the “A” icon) to add text directly onto each mask[4].
- This label appears on the front of the card when that mask is being tested, effectively serving as a per-mask question or hint.
- However, this label will not appear on the answer side, and there is no built-in way to have a different, per-mask explanatory text appear only on the back.

#### 2. **Using the “Remarks” Field for Explanations**
- The “Remarks” or “Extra” field can be used to add general explanations that will appear on the back of all cards generated from the note[3].
- This is not mask-specific: the same explanation appears on the back of every card for that image.

#### 3. **Workaround for Mask-Specific Explanations**
- If you need **different explanations for each mask**, the only robust method is to create **separate notes** for each mask, each with its own explanation in a field (but this duplicates the image, which you wanted to avoid).

### Summary Table

| Goal                                 | Supported Natively? | Workaround/Partial Solution                |
|---------------------------------------|---------------------|--------------------------------------------|
| Per-mask question text (front)        | Yes (via label tool)| Use label tool to add text to each mask[4] |
| Per-mask answer/explanation (back)    | No                  | Create separate notes per mask             |
| General answer/explanation (back)     | Yes                 | Use “Remarks”/“Extra” field[3]             |

### Practical Steps

1. **Add mask-specific question:**  
   - In the Image Occlusion Editor, select the mask and click the “A” icon to add a label (question/hint) for that mask[4].

2. **Add general explanation:**  
   - Use the “Remarks” field for an explanation that appears on the back of all cards[3].

3. **If you need mask-specific explanations:**  
   - You must create a separate note for each mask, each with its own explanation in a field.

**In summary:**  
- You can display mask-specific question text on the front using the label tool.
- You cannot natively display mask-specific answer/explanation text on the back for each mask within the same note; only a general explanation for all masks is possible via the “Remarks” field[3][4].
- For true mask-specific answers, you must create separate notes per mask.

[1] https://www.youtube.com/watch?v=G1iI62Hfn7Q
[2] https://www.youtube.com/watch?v=xou_c2AK0_M
[3] https://forums.ankiweb.net/t/set-max-height-for-image-occlusion/45124
[4] https://www.youtube.com/watch?v=9WTVnc9ptQw
[5] https://www.youtube.com/watch?v=7pU9L0XybyI
[6] https://forums.ankiweb.net/t/image-occlusion-text-box-changes-sizes/41412
[7] https://forums.ankiweb.net/t/image-occlusion-enhanced-official-support-thread/924?page=2
[8] https://ankiweb.net/shared/info/1374772155
[9] https://www.reddit.com/r/Anki/comments/11k1b45/image_occlusion_enhanced_does_not_save_as_a/
[10] https://forums.ankiweb.net/t/editor-apply-font-color-background-color-custom-class-custom-style-official-thread/550