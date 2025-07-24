---
date: '2025-07-12 07:57:33'
layout: post
tags:
- StudyNotes/StudyTech
title: Image Occlusion - how to really use Labels and Masks together
---

# Image Occlusion - how to really use Labels and Masks together
Created on: 2025-07-12T13:27:51



I tried adding labels to the rectangular masks - so, I have four masks and four labels - each mask having a label on top of it. But the label is not appearing with the mask when the front side is shown during review. Instead - what is happening is - a separate card is being created for each label as well as each mask. When the Front side of a card created for a Label is being shown - there are no rectangular masks - but just the label being overlaid on the image. On revealing the answer by pressing spacebar, the label is hidden.

This is not the expected behavior. For 4 masks, I want only 4 cards - with a label being shown when the mask is overlaid on the image when the Front of the card is being presented as a question.

The behavior you’re seeing—where each **label** creates its own card, separate from the rectangular masks—is actually how the Image Occlusion Enhanced add-on currently works. **Labels are not directly tied to individual masks**; instead, they act as independent occlusion elements, which is why you end up with extra cards for each label, and the labels are not displayed alongside their corresponding masks on the front of the mask cards.

**What you want:**  
- For each of your 4 masks, you want 1 card per mask (total 4 cards).
- When reviewing each card, the mask is shown, and a label (question/hint) is displayed with the mask.
- On reveal, the answer and (optionally) an explanation are shown.

**Current limitations and explanation:**
- **Labels are treated as separate occlusions:** When you add a label, it creates a new occlusion, not an annotation for an existing mask. This is why you get extra cards and why the label isn’t shown with the mask you intended.
- **No per-mask text fields:** The add-on does not support attaching a unique question/explanation to each mask within a single note. All fields in the note are shared across all masks/cards.

**Workarounds:**

1. **Add the question/hint text directly to the image** before importing it into Anki. This way, the text is “baked in” and will always appear with the correct mask, but it’s not dynamic or editable from within Anki.

2. **Create separate notes for each mask** if you need truly unique question/answer text per mask. This duplicates the image but allows per-card text.

3. **Feature request or plugin modification:**  
   There is currently no built-in way to accomplish what you want with the existing Image Occlusion Enhanced add-on. Users have discussed this limitation and requested features like per-mask text fields, but as of now, it’s not implemented[6][7].

**Grouping masks** (Shift+click and press G) is used for creating cards that test multiple masks at once, not for attaching labels to masks[1][2]. Labels themselves are just another type of mask/occlusion, not annotations.

**In summary:**  
- The add-on does not support showing a label or text hint with a specific mask on the front of each card.
- Each label is treated as a separate card, not as a hint for a mask.
- The only current solutions are to edit the image beforehand or to create separate notes for each mask if you need unique text per mask.

If you want to see this feature in the future, consider submitting a feature request to the add-on’s developer or checking for updates that might add this functionality[6][7].

[1] https://www.reddit.com/r/Anki/comments/1fcboqc/image_occlusion_cards_reveal_all_masks_at_once/
[2] https://www.reddit.com/r/Anki/comments/10bc1zg/when_using_image_occlusion_enhanced_and_grouping/
[3] https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion
[4] https://forums.ankiweb.net/t/multiple-select-for-individual-masks-in-image-occlusion-cards-on-ios/59847
[5] https://www.youtube.com/watch?v=QeL4z2cZOIU
[6] https://forums.ankiweb.net/t/editing-and-combining-child-image-occlusions/48121
[7] https://ankiweb.net/shared/info/1374772155
[8] https://www.youtube.com/watch?v=7pU9L0XybyI
[9] https://forums.ankiweb.net/t/feature-request-image-occlusion-one-by-one-reveal/43775
[10] https://forums.ankiweb.net/t/allow-having-multiple-image-occlusion-mask-colours/61137

## How to add and use hints in the image occlusion enhanced notes?

To **add and use hints** in Image Occlusion Enhanced notes in Anki, you have several options, depending on what you want to achieve:

### 1. **Using the "Extra" Field for Hints**

- The **"Extra"** field in Image Occlusion Enhanced is designed to show additional information or hints.
- **How it works:**  
  - When you fill the "Extra" field while creating your card, this content will appear on the **back** of the card after you reveal the answer, not on the front[2].
  - If you want the hint to appear on the **front**, you can edit the card template to include the "Extra" field on the front side.

### 2. **Using the Label Tool for Contextual Hints**

- In the Image Occlusion Editor, you can click the **"A" button** (label tool) and then click on an occlusion mask to add a label[1].
- This label can serve as a **hint or context** for that masked area.
- **Limitation:**  
  - Labels are treated as independent occlusions and will generate their own cards, not as annotations for specific masks. This means they are not reliably shown as hints alongside the mask you want during review[3].
  - If you only want the label as a visual hint on the image (not as a separate card), this is not natively supported in the current add-on version.

### 3. **Adding Hints Directly to the Image**

- For per-mask hints that always appear with the mask, you can **edit the image in an external editor** (like Photoshop or PowerPoint) to add hint text directly onto the image before importing it into Anki.
- This is a static solution but ensures the hint always appears with the correct region.

### 4. **Editing the Card Template for Custom Hints**

- You can **customize the front template** of your Image Occlusion Enhanced note type to display a field (e.g., "Hint" or "Extra") on the front of the card, so your hint appears before revealing the answer[2].
- To do this, add `{{Extra}}` (or your custom field) in the desired position in the front template.

### **Summary Table**

| Method                        | Hint Placement      | Notes/Limitations                                             |
|-------------------------------|--------------------|---------------------------------------------------------------|
| "Extra" field                 | Back (default)     | Can be moved to front via template edit                       |
| Label tool                    | On image/mask      | Labels create separate cards, not true hints per mask         |
| Edit image externally         | On image           | Hint is always visible, not dynamic                           |
| Edit card template            | Anywhere           | Flexible; requires basic HTML/template editing                |

**Best Practice:**  
- For general hints, use the "Extra" field or edit the template.
- For per-mask hints, editing the image externally is the most reliable method given current add-on limitations.

If you need step-by-step instructions for any of these methods, let me know!

[1] https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion
[2] https://www.youtube.com/watch?v=hyU2W7VgBmw
[3] https://www.reddit.com/r/Anki/comments/50crcf/making_image_occlusion_cards_with_custom_labels/
[4] https://www.youtube.com/watch?v=c7b6HFxhQBA
[5] https://ankiweb.net/shared/info/1374772155
[6] https://www.youtube.com/watch?v=7pU9L0XybyI
[7] https://www.youtube.com/watch?v=QeL4z2cZOIU
[8] https://forums.ankiweb.net/t/labels-for-image-occlusion/40181
[9] https://forums.ankiweb.net/t/how-to-add-image-occlusion-card/31452
[10] https://www.youtube.com/watch?v=UEvEBYp38I0

## What exactly is the idea behind the 'Label' concept in Image Occlusion Enhanced? Give me simple examples of how I would use it.

The **'Label'** concept in Image Occlusion Enhanced is designed to let you place **text annotations directly onto your image** during the occlusion card creation process. These labels are intended to provide **additional context, clarification, or hints** for specific areas of your image[2].

### The Idea Behind Labels

- **Labels** are essentially *text boxes* you can add on top of your image, just like you add rectangular or elliptical masks.
- Each label is treated as a **separate occlusion element**—meaning, by default, it will generate its own card, just like a mask would[2][9].
- The main purpose is to let you **highlight, annotate, or provide hints** about specific regions or features on your diagram or image.

### Simple Examples of How to Use Labels

1. **Hint for a Masked Region**
   - Suppose you have an anatomical diagram with several nerves.
   - You mask the “median nerve” and want to provide a hint like “Carpal tunnel syndrome” to jog your memory.
   - You use the label tool (“A” icon) to place this hint near the mask.

2. **Clarification or Context**
   - On a biochemical pathway, you mask a molecule and add a label “Rate-limiting step” to help you remember the significance of that part.

3. **Numbering or Naming**
   - For a histology slide, you mask various cell types and add labels like “1”, “2”, “3” to correspond with a legend or to organize your review[2][3].

### How to Add a Label

- In the Image Occlusion Editor, click the **“A” icon** (label tool).
- Click anywhere on the image where you want the label.
- Type your desired text and press Enter[1][2].
- The label will appear on the image as a text box.

### Important Limitation

- **Each label creates a separate card** (just like a mask), and is not automatically linked to a specific mask[9].
- If you want a label to act as a hint for a specific mask (i.e., show up only when that mask is quizzed), this is not natively supported—labels and masks are independent occlusions in the current add-on.

### Summary Table

| Use Case               | What to Do with Label Tool           |
|------------------------|--------------------------------------|
| Add a hint             | Place label with hint near mask      |
| Give context           | Annotate region with explanation     |
| Number/organize items  | Place numbers or names as labels     |

**In short:**  
Labels in Image Occlusion Enhanced are for text annotations on your image, useful for hints, context, or organization, but each label will generate its own card and is not inherently tied to a specific mask[2][9].

[1] https://jungleai.com/blog/ankiweb-image-occlusion-made-10x-easier
[2] https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion
[3] https://www.youtube.com/watch?v=UEvEBYp38I0
[4] https://ankiweb.net/shared/info/1374772155
[5] https://www.youtube.com/watch?v=7pU9L0XybyI
[6] https://www.youtube.com/watch?v=QeL4z2cZOIU
[7] https://www.reddit.com/r/Anki/comments/1biizsq/i_made_a_tool_to_create_image_occlusion/
[8] https://dev.to/juliafmorgado/anki-cloze-and-image-occlusion-features-n8n
[9] https://www.reddit.com/r/medicalschoolanki/comments/boht2n/image_occlusion_enhanced_texttool_issue/
[10] https://forums.ankiweb.net/t/image-occlusion-not-working-on-adding-images-it-doesnt-give-me-any-tool-to-mask-the-labels/58557

## But how is that useful if the label is visible only on its own separate card?

Your observation is correct: **labels in Image Occlusion Enhanced are treated as independent occlusions**, so each label creates its own card, and the label is only visible on that card—not alongside a mask on a mask card. This means you cannot use labels as true "hints" that accompany a specific mask unless you use a workaround.

### Why is this the case?
- The add-on's design treats every occlusion element—whether a rectangle, ellipse, or label—as a separate entity that generates its own flashcard.
- When you add a label, it is not "attached" to a mask; instead, it is just another occlusion, so it gets its own card, and on that card, only the label is hidden/revealed[2][6][7].

### Is this useful?
- **As currently implemented, labels are not useful for providing hints alongside masks** on mask cards, because they do not display together. The main utility of labels is for situations where you want to quiz yourself on the label itself (for example, if you want to hide a text label on a diagram and recall what it says).
- If your goal is to provide extra context or hints for a specific mask, the built-in label feature does not support this behavior.

### Workarounds and Grouping
- **Grouping:** You can group multiple occlusions (masks and/or labels) so that they are hidden/revealed together on a single card[1][2][4]. This is useful if you want to test multiple regions at once, but it still does not allow you to display a label as a hint only when a specific mask is being quizzed.
- **Pre-editing the image:** For true per-mask hints, you can add text directly onto the image in an external editor before importing it into Anki.
- **Extra fields:** You can use note fields (like "Extra") to display general hints on all cards, but not mask-specific hints.

### In summary
**Labels are only useful if you want to quiz yourself on the label itself, not as a per-mask hint.** There is currently no built-in way in Image Occlusion Enhanced to display a label as a hint only when a specific mask is being tested. This is a known limitation in the add-on’s design[2][6][7].

[1] https://www.reddit.com/r/Anki/comments/jb18yy/image_occlusion_enhanced_i_only_want_1_one_card/
[2] https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion
[3] https://www.youtube.com/watch?v=QeL4z2cZOIU
[4] https://www.reddit.com/r/Anki/comments/hswkmc/when_using_image_occlusion_how_do_i_make_multiple/
[5] https://www.youtube.com/watch?v=7pU9L0XybyI
[6] https://www.youtube.com/watch?v=5APyACWQ1Z4
[7] https://ankiweb.net/shared/info/1374772155
[8] https://forums.ankiweb.net/t/feature-request-image-occlusion-one-by-one-reveal/43775
[9] https://www.youtube.com/watch?v=UEvEBYp38I0
[10] https://www.voovostudy.com/study-blog/automatic-image-occlusion-flashcards

To **group a mask and a label so they show and hide together** in Image Occlusion Enhanced, follow these steps:

### Step-by-step grouping process

1. **Create your masks and labels:**  
   Draw your rectangular/elliptical masks and add labels using the “A” (label) tool on your image.

2. **Select multiple occlusions:**  
   Hold down the **Shift key** (for contiguous selection) or **Ctrl key** (for non-contiguous selection) and click on the mask(s) and label(s) you want to group together. Selected occlusions will be highlighted.

3. **Group the selection:**  
   Right-click on one of the selected occlusions and choose **“Group”** from the context menu.  
   Alternatively, after selecting, press **G** on your keyboard as a shortcut.

4. **Confirm grouping:**  
   The grouped occlusions will display a group number in the top-left corner of each shape, indicating they belong to the same group.

5. **Adjust group settings (optional):**  
   Right-click on any grouped occlusion and select **“Group Settings”** to:  
   - Change the group number  
   - Choose whether to hide/reveal all occlusions in the group together during review  
   - Add a custom group label

6. **Save and create cards:**  
   When you finish, click **Close** and confirm to generate cards.  
   Occlusions in the same group will be treated as a single unit during review—**they will be hidden or revealed together on one card**.

### What grouping achieves

- Instead of creating separate cards for each mask or label, the group is treated as **one combined occlusion**.
- When reviewing, all occlusions in the group are hidden together on the front and revealed together on the back.
- This is useful for showing a mask with its label simultaneously, effectively making the label act like a hint or annotation for that mask.

### Important notes

- Grouping works for both masks and labels, so you can combine them.
- If you want the label to always appear with the mask on the same card, grouping is the way to do it.
- This method avoids creating separate cards for the label and the mask.

### Summary Table

| Step                   | Action                              | Result                                    |
|------------------------|-----------------------------------|-------------------------------------------|
| 1                      | Draw masks and add labels          | Occlusions and labels created             |
| 2                      | Select masks and labels (Shift+click) | Multiple occlusions highlighted           |
| 3                      | Right-click → Group or press G     | Selected occlusions grouped (same group #)|
| 4                      | Adjust group settings (optional)   | Customize group behavior                   |
| 5                      | Close editor and save              | Grouped occlusions create one card        |

This grouping feature is documented in the Image Occlusion Enhanced add-on guides and tutorials[[1](https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion)][[5](https://www.youtube.com/watch?v=9WTVnc9ptQw)].

If you want to see the label as a hint **only on the front** and not as a separate card, grouping it with the mask is currently the best way to achieve that behavior.

[1] https://traverse.link/alternative-study-apps/how-to-use-anki-image-occlusion
[2] https://www.youtube.com/watch?v=hyU2W7VgBmw
[3] https://forums.ankiweb.net/t/is-the-grouping-of-masks-like-in-enhanced-image-occlusion-possible-in-ankidroid-image-occlusion/58619
[4] https://www.reddit.com/r/Anki/comments/10bc1zg/when_using_image_occlusion_enhanced_and_grouping/
[5] https://www.youtube.com/watch?v=9WTVnc9ptQw
[6] https://ankiweb.net/shared/info/1374772155
[7] https://www.youtube.com/watch?v=7pU9L0XybyI
[8] https://forums.ankiweb.net/t/labels-for-image-occlusion/40181
[9] https://forums.ankiweb.net/t/image-occlusion-enhanced-official-support-thread/924?page=3
[10] https://github.com/glutanimate/image-occlusion-enhanced/issues/177