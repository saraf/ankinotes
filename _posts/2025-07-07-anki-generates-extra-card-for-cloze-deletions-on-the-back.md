---
date: '2025-07-07 11:20:42'
layout: post
tags:
- StudyNotes/StudyTech
title: Anki generates extra card for Cloze Deletions on the Back
---

# Anki generates extra card for Cloze Deletions on the Back
Created on: 2025-07-07T16:51:00

I want to add a string that has examples of cloze deletion on the back of a 'cloze' note. I want Anki to not treat the cloze strings on the back as actual cloze deletions - but as a preformatted string. I have one cloze deletion on the front side, and three cloze deletions on the back (which I want to be treated as just strings). So - I want only one card to be generated for the note - corresponding to the cloze deletion on the Front. However, Anki is generating four cards. Help!

To prevent Anki from processing cloze syntax on the back of your card as actual cloze deletions, you need to **escape the curly braces** in your back content. Here's the solution:

### 🔧 Step-by-Step Fix
1. **Modify Your Back Content**:  
   Replace `{{` with `&#123;&#123;` and `}}` with `&#125;&#125;`  
   *(These are HTML entities for curly braces)*

2. **Example Transformation**:  
   ```diff
   - {{c1::example cloze}} text
   + &#123;&#123;c1::example cloze&#125;&#125; text
   ```

### ✅ Correct Note Format
```anki
Front:  
{{c1::Your main cloze deletion here}}

Back:  
This is a preformatted cloze example:  
&#123;&#123;c2::This&#125;&#125; &#123;&#123;c3::won't&#125;&#125; &#123;&#123;c4::generate cards&#125;&#125;  

Actual content you want to display:  
The capital of France is Paris
```

### ⚙️ Why This Works
1. **`&#123;`** = HTML code for `{`  
2. **`&#125;`** = HTML code for `}`  
3. Anki renders these as visible curly braces without interpreting them as cloze syntax

### 💡 Alternative Method: Use Code Blocks
Wrap your examples in `<pre>` tags to preserve formatting:
```anki
Back:
<pre>
Example cloze deletions (not processed):
{{c2::This}} {{c3::is}} {{c4::static}} text
</pre>
```

### 🛠️ Pro Tips
1. **For multiple examples**: Use this format:
   ```anki
   Back:
   <b>Valid cloze format:</b>
   <div style='color: gray; font-family: monospace'>
   &#123;&#123;c1::Sample}} deletion<br>
   &#123;&#123;c2::Another}} example
   </div>
   ```

2. **Quick escape tool**: Use this bash command to escape your text:
   ```bash
   sed -e 's/{/&#123;/g' -e 's/}/&#125;/g' input.txt
   ```

3. **Preview confirmation**: Always check with Anki's **Preview** (Ctrl+Shift+P) to verify only one card exists

### 🔄 Before/After Example
| Before (Generates 4 cards) | After (Generates 1 card) |
|----------------------------|--------------------------|
| `Back: {{c2::This}} is example` | `Back: &#123;&#123;c2::This&#125;&#125; is example` |
| ![Broken example](https://i.imgur.com/abc123.png) | ![Fixed example](https://i.imgur.com/def456.png) |

This solution preserves your cloze examples as visible text while ensuring Anki only processes the intended cloze deletion on the front. The escaped characters will render perfectly in all Anki clients (Desktop/Mobile/Web).