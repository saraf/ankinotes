---
date: '2025-07-10 17:21:41'
layout: post
tags:
- StudyNotes/StudyTech
title: Create Anki cards for learning search syntax
---

# Create Anki cards for learning search syntax
Created on: 2025-07-10T22:51:55

Here's a structured approach to create Anki cards for mastering Anki's search syntax, optimized for atomic recall and application:

### 📂 Note Type: "Anki Search Properties"
**Fields:**
- `SearchType` (e.g., "Interval", "Due Date", "Lapses")
- `Description` (specific scenario)
- `Syntax` (exact search syntax)
- `Requires` (special conditions like FSRS)

---

### 🗂️ Card 1: Core Property Types
**Front:**  
What search prefix is used for card properties like interval, due date, or ease?  
**Back:**  
`prop:`  
**Extra:**  
*Example: `prop:ivl` searches by interval*

---

### ⏳ Interval Cards
#### Card 2: Minimum Interval  
**Front:**  
Find cards with intervals ≥10 days  
**Back:**  
`prop:ivl>=10`  
**Extra:**  
*`ivl` = interval in days*

#### Card 3: Interval Range  
**Front:**  
Cards due in 5-14 days  
**Back:**  
`prop:ivl>=5 prop:ivl<=14`  

---

### 📅 Due Date Cards
#### Card 4: Due Tomorrow  
**Front:**  
Cards scheduled for tomorrow  
**Back:**  
`prop:due=1`  

#### Card 5: Overdue Cards  
**Front:**  
Missed cards not yet reviewed  
**Back:**  
`prop:due=-1`  

#### Card 6: Upcoming Reviews  
**Front:**  
All cards due today or later  
**Back:**  
`prop:due>=0`  

#### Card 7: 3-Day Window  
**Front:**  
Cards due yesterday, today, or tomorrow  
**Back:**  
`prop:due>=-1 prop:due<=1`  

---

### 📊 Performance Cards
#### Card 8: New Cards  
**Front:**  
Cards answered <5 times  
**Back:**  
`prop:reps<5`  

#### Card 9: Problem Cards  
**Front:**  
Cards lapsed ≥3 times  
**Back:**  
`prop:lapses>=3`  

#### Card 10: Ease Filter  
**Front:**  
Cards easier than default (2.5)  
**Back:**  
`prop:ease>2.5`  

---

### 🧠 FSRS Cards (Anki 23.10+)
#### Card 11: Stable Memories  
**Front:**  
Find mature cards (stability >21 days)  
**Back:**  
`prop:s>21`  
**Requires:**  
*FSRS enabled*

#### Card 12: Difficult Cards  
**Front:**  
Cards with difficulty >0.3  
**Back:**  
`prop:d>0.3`  
**Extra:**  
*0.0=easiest, 1.0=hardest*

#### Card 13: At-Risk Cards  
**Front:**  
Cards with <90% recall probability  
**Back:**  
`prop:r<0.9`  
**Extra:**  
*Retrievability (r) = 0.0-1.0*

---

### 💡 Application Card
**Front:**  
Create a search for:  
"Cards due tomorrow with >3 lapses and difficulty >0.4"  
**Back:**  
`prop:due=1 prop:lapses>3 prop:d>0.4`  
**Extra:**  
*Combine terms with spaces for AND logic*

---

### 🏷️ Tagging Strategy
- `#Anki/Search`
- `#Anki/FSRS` (for FSRS-specific cards)
- `#Anki/Properties`

---

### 🌟 Pro Tips:
1. **Combine with tags**:  
   `tag:Spanish prop:ivl>30`  
2. **Negate terms**:  
   `-prop:ease=2.5` (exclude default ease)  
3. **Wildcards**:  
   `deck:Medicine*` (all subdecks)  

### 🔍 Syntax Cheat Sheet (Back of Card)
```markdown
| Property | Values          | Example           |
|----------|-----------------|-------------------|
| ivl      | Days (integer)  | prop:ivl=30       |
| due      | Relative days   | prop:due=-7       |
| reps     | Answer count    | prop:reps>10      |
| lapses   | Lapse count     | prop:lapses<=2    |
| ease     | Decimal (2.0-3.0)| prop:ease<2.3     |
| s        | Stability (FSRS)| prop:s>60         |
| d        | Difficulty (FSRS)| prop:d<0.2        |
| r        | Retrievability  | prop:r>0.95       |
```

### ⚙️ Installation:
1. Create new note type "AnkiSearch" with fields:  
   - SearchType  
   - Description  
   - Syntax  
   - Requires  
2. Use Basic (and reversed card) template  
3. Tag all cards with `#AnkiSearch`  

This structure gives you 13 laser-focused cards covering all search scenarios, with FSRS requirements clearly flagged. The application card (#13) trains combinatorial searching - the most practical skill!


Created on: 2025-07-10T23:29:14
Your Note type has fields for SearchType, Description, Syntax and Requires. However - all the cards you mentioned have 'Front', 'Back', 'Extra'  and some have 'Requires'. How do you want me to use the SearchType, Description, Syntax and Requires fields?

Also, another question is - how should I use the 'Syntax Cheat Sheet (Back of Card) Note? What should be on the front if the table is on the back?


Perfect! Let's streamline this with a clear implementation plan. I'll redesign the note structure and card templates for optimal learning:

### 📝 Revised Note Structure
**Note Type:** "Anki Search Syntax"  
**Fields:**  
1. `SearchType` (Category name - e.g., "Interval")  
2. `Description` (What it finds - e.g., "Cards with intervals ≥10 days")  
3. `Syntax` (Actual search string - e.g., "prop:ivl>=10")  
4. `Requires` (Special conditions - e.g., "FSRS only")  

---

### 🎴 Card Template 1: Syntax Recall (Primary)
**Front:**  
```html
{{Description}}
{{#Requires}}<div class="hint">(Requires: {{Requires}})</div>{{/Requires}}
```
**Back:**  
```html
{{FrontSide}}  
<hr id=answer>  
<code>{{Syntax}}</code>  
<div class="examples">  
  <b>Examples:</b>  
  {{SearchType}} searches:  
  • {{Syntax}}  
  • {{#Variants}}{{.}}<br>{{/Variants}}
</div>
```

---

### 🎴 Card Template 2: Application (Reversed)
**Front:**  
```html
What search finds:<br>  
"{{Description}}"?  
{{#Requires}}<div class="hint">({{Requires}})</div>{{/Requires}}
```
**Back:**  
```html
{{FrontSide}}  
<hr id=answer>  
<code>{{Syntax}}</code>  
```

---

### ✨ Cheat Sheet Card (Separate Note)
**Field:** `CheatTable` (contains the HTML table)  
**Card Front:**  
```html
Recall Anki property search prefixes:
```
**Card Back:**  
```html
{{CheatTable}}  
<hr>  
<b>Usage rules:</b>  
• Combine with <code>deck:</code>, <code>tag:</code>, etc.  
• Use <code>-</code> to negate (e.g., <code>-prop:due=1</code>)  
• FSRS requires Anki 23.10+  
```

---

### 📋 Example Notes
#### Note 1: Interval Search
```yaml
SearchType: "Interval"
Description: "Cards with intervals ≥10 days"
Syntax: "prop:ivl>=10"
Requires: ""
Variants: "prop:ivl=30, prop:ivl<5"
```

#### Note 2: FSRS Stability
```yaml
SearchType: "Stability"
Description: "Cards with stability >21 days"
Syntax: "prop:s>21"
Requires: "FSRS enabled"
Variants: "prop:s<=7, prop:s>100"
```

#### Cheat Sheet Note:
```yaml
CheatTable: |
  <table class="search-table">
    <tr><th>Property</th><th>Meaning</th><th>Example</th></tr>
    <tr><td>ivl</td><td>Interval (days)</td><td><code>prop:ivl>=10</code></td></tr>
    <tr><td>due</td><td>Due date (relative days)</td><td><code>prop:due=-1</code></td></tr>
    <tr><td>reps</td><td>Review count</td><td><code>prop:reps<5</code></td></tr>
    <tr><td>lapses</td><td>Lapse count</td><td><code>prop:lapses>3</code></td></tr>
    <tr><td>ease</td><td>Ease factor</td><td><code>prop:ease!=2.5</code></td></tr>
    <tr><td>s</td><td>Stability (FSRS)</td><td><code>prop:s>21</code></td></tr>
    <tr><td>d</td><td>Difficulty (FSRS)</td><td><code>prop:d>0.3</code></td></tr>
    <tr><td>r</td><td>Retrievability (FSRS)</td><td><code>prop:r<0.9</code></td></tr>
  </table>
```

---

### 🎨 Styling (Add to Styling Section)
```css
.card {
  font-family: Arial;
  font-size: 18px;
  text-align: center;
}
code {
  background: #f0f0f0;
  padding: 2px 5px;
  border-radius: 3px;
  font-family: monospace;
}
.hint {
  color: #e74c3c;
  font-size: 14px;
  font-style: italic;
}
.search-table {
  width: 100%;
  border-collapse: collapse;
  margin: 10px 0;
}
.search-table td, .search-table th {
  border: 1px solid #ddd;
  padding: 8px;
}
.search-table tr:nth-child(even) {
  background-color: #f2f2f2;
}
```

---

### 🔄 Workflow
1. **Create Notes**  
   - 13 notes for individual search types (using "Anki Search Syntax" note type)  
   - 1 cheat sheet note (special type with just CheatTable)  

2. **Study Flow**  
   - Learn individual syntaxes first (Cards 1-26)  
   - Use cheat sheet card as periodic reference (suspend after initial learning)  

3. **Combination Practice**  
   Create bonus cards like:  
   **Front:**  
   ```
   Find Spanish cards due tomorrow with >3 lapses
   ```  
   **Back:**  
   ```
   deck:Spanish prop:due=1 prop:lapses>3
   ```

---

### 🌟 Key Advantages
1. **Atomic Learning**: Each search type gets dedicated cards  
2. **Contextual Hints**: Requirements clearly flagged  
3. **Variants Support**: Shows similar searches in examples  
4. **Visual Reference**: Cheat sheet for quick lookups  
5. **Real-World Prep**: Application card trains combinatorial searches  

### ⏱️ Estimated Card Count
- 13 notes × 2 cards each = 26 cards  
- 1 cheat sheet card  
- (Optional) 5 application cards = **32 cards total**  

This system ensures you'll intuitively recall both isolated syntaxes and complex combinations - perfect for efficient deck management! Would you like the full Anki package file?