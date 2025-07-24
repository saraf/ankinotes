---
date: '2025-07-22 10:11:15'
layout: post
tags:
- StudyNotes/StudyTech
title: Import order - show cards in the order in which they were imported
---

# Import order - show cards in the order in which they were imported
Created on: 2025-07-22T15:51:12

To make **Anki show cards in the order in which they were imported from a CSV file**, follow these steps:

1. **Order Your CSV File Correctly**
   - Make sure the rows in your CSV are ordered exactly as you want the cards to appear. Save the file after arranging the rows in Excel or a text editor[2].

2. **Import the CSV into Anki**
   - When you import your CSV into Anki, cards are initially assigned an "Added" timestamp in the order they are processed. By default, this usually matches the row order in the CSV file, so the **first row becomes the first card added**, and so forth[9][2].

3. **Display or Study Cards in the Same Order**
   - In the **Browse window**, click the header of the "Added" or "Created" column to sort cards by the order they were imported. This makes it easy to see or edit cards in import order[4][2].
   - When studying new cards, go to your deck settings and make sure the "New Cards" order is set to "in order added." This shows new cards in the order you imported them, not shuffled or random[3][9].

4. **If You Need to Reset or Reorder After Import:**
   - If the cards are not showing in your preferred order or if you added more cards later, you can use the **Reposition tool** in Anki:
     - In the Browse window, select the relevant cards.
     - Use the "Reposition" feature to assign new sequential positions to the cards, ensuring they will appear in the desired order when you study new cards[6][3].
     - You can also add a separate field (like "Index") in your CSV with increasing numbers, then sort and reposition cards by that field in Anki for full control over the order[3].

**Note:** If you reopen the deck and cards seem out of order, check both your sort criteria in the browser (sort by "Added" or your custom index field) and the deck's new card order setting.

**Summary Table: How to Show Cards in Import Order**

| Step                       | What to Do                                               |
|----------------------------|---------------------------------------------------------|
| Order CSV                  | Sort rows in intended order                             |
| Import                     | Use Anki's import tool, mapping fields correctly        |
| Adjust Deck Settings       | Set "new cards" order to "in order added"               |
| Sort in Browse             | Click "Added"/"Created" column to view import order     |
| Reposition (if needed)     | Select, sort, and use "Reposition" to enforce the order |

By following this procedure, Anki will display and study **new cards in the same order they appeared in your original CSV**[2][4][9].

[1] https://superuser.com/questions/1145775/anki-import-one-csv-create-mulitple-decks-and-import-into-them
[2] https://www.reddit.com/r/Anki/comments/1j2w3t7/conserving_card_order_in_browse/
[3] https://forums.ankiweb.net/t/display-order-with-learning-cards/46401
[4] https://forums.ankiweb.net/t/imported-deck-isnt-sorted-according-to-formation-date/45907
[5] https://www.reddit.com/r/Anki/comments/1dit7s8/how_to_set_the_order_that_new_cards_are_shown/
[6] https://www.youtube.com/watch?v=s5mStw-qLqU
[7] https://forums.ankiweb.net/t/update-deck-via-extended-csv-with-new-synonyms-avoiding-old-duplicates/41772
[8] https://forums.ankiweb.net/t/i-want-my-cards-to-be-shown-in-chronological-order-no-matter-what/13762
[9] https://www.reddit.com/r/Anki/comments/akbjxr/questions_about_due_order_when_importing_a_deck/
[10] https://docs.ankiweb.net/importing/text-files.html
[11] https://forum.lingq.com/t/randomizing-deck-for-anki-import/16149
[12] https://superuser.com/questions/698902/can-i-create-an-anki-deck-from-a-csv-file
[13] https://www.youtube.com/watch?v=w_gieyVnKXs