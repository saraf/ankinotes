---
date: '2025-06-19 14:36:48'
layout: post
tags:
- StudyNotes/StudyTech
title: Hints in Anki Cards - Custom Note Type
---

# Hints in Anki Cards - Custom Note Type 

In Anki, if you want **global behavior across all cards of a particular note type**, you should place your custom **CSS** and **JavaScript** into the **card template** for that note type.

Here's how to do it cleanly:

---

## ✅ Where to Put the Custom CSS and JavaScript

### 📍 Step-by-step:

1. **Go to** `Browse` in Anki.
2. Select a card that uses the note type you want to modify.
3. Click `Cards…` to open the **Card Template Editor**.
4. You'll see three main sections:

   * **Front Template**
   * **Back Template**
   * **Styling**

---

### 🎨 Put the CSS in the "Styling" Section

Paste this into the **Styling** section:

```css
.hint {
  color: gray;
  font-size: 90%;
  display: none;
}
```

This makes all `.hint` class elements hidden by default and styled appropriately.

---

### ⚙️ Put the JavaScript in the "Front Template" (or "Back Template")

At the bottom of the **Front Template**, add this script:

```html
<script>
  let i = 0;
  document.addEventListener("keydown", function (event) {
    if (event.key.toLowerCase() === "h") {
      const hints = document.querySelectorAll(".hint");
      if (i < hints.length) {
        hints[i].style.display = "inline";
        i++;
      }
    }
  });
</script>
```

This lets you reveal hints one at a time by pressing the **`H`** key.

---

### ✅ Now, for every card you add of this note type:

You can simply include hints like this in the **Front or Back** field:

```html
<a class="hint" href="#">Hint 1: Greek letter</a><br>
<a class="hint" href="#">Hint 2: Used in serverless</a><br>
<a class="hint" href="#">Hint 3: Starts with L</a>
```

No need to repeat the CSS or script again!

---

## 🧠 Tip: Create a Custom Note Type for Hint-Enhanced Cards

To avoid affecting unrelated cards:

* Duplicate an existing note type and name it something like:

  > `Basic (with Hints)`
* Then modify that version’s card template with the CSS and script.
* Use this note type for all cards that benefit from hint-based scaffolding.

---
# Note - improvement in the above

I am using the following in the Front Template of card to enable hints in Anki:
The hint has display style set to 'none', and each hint is revealed on every successive 'h' key press.

{{Front}}
<script>
  let i = 0;
  document.addEventListener("keydown", function (event) {
    if (event.key.toLowerCase() === "h") {
      const hints = document.querySelectorAll(".hint");
      if (i < hints.length) {
        hints[i].style.display = "inline";
        i++;
      }
    }
  });
</script>

The problem is - the hints display fine when reviewing a card for the first time, but say - if I can't guess the answer and schedule the card 'again', the next time I am shown the same card - the hints are hidden and 'h' key does not show the hints anymore. How can I fix this?

The issue you're facing arises because **Anki reuses the card's review window** without reloading the HTML or re-attaching event listeners. When you press "Again", Anki shows the card again immediately—but your `keydown` listener is not re-attached, or your `i` counter is not reset.

Here’s a robust fix that works consistently across repeated reviews and card flips:

---

## ✅ Full Working Version with Reset Behavior

### 🔧 Key fixes:

* Reset the hint index `i` on each card load.
* Ensure the script is re-executed even when Anki re-shows the same card (use a self-invoking function).
* Hints should always start hidden, even on repeated card views.

### ✅ Use this in your **Front Template**:

```html
{{Front}}

<script>
(function() {
  let i = 0;

  // Hide all hints when card is shown
  const resetHints = () => {
    const hints = document.querySelectorAll(".hint");
    hints.forEach(h => h.style.display = "none");
    i = 0;
  };

  // Reveal hints one at a time when pressing "h"
  const handleKey = (event) => {
    if (event.key.toLowerCase() === "h") {
      const hints = document.querySelectorAll(".hint");
      if (i < hints.length) {
        hints[i].style.display = "inline";
        i++;
      }
    }
  };

  // Run reset on initial display
  resetHints();

  // Rebind event listener to avoid multiple bindings
  document.removeEventListener("keydown", handleKey);
  document.addEventListener("keydown", handleKey);
})();
</script>
```

---

## 📝 How to Use It

In your **card content**, you can include multiple hints like:

```html
This is a question. <a href="#" class="hint">Hint 1</a> <a href="#" class="hint">Hint 2</a>
```

Each time you press the `h` key, the next hint will be revealed.

---

## 🧠 Why This Works

* `resetHints()` ensures every review starts fresh.
* Wrapping everything in `(() => { ... })()` ensures the script re-executes when the card is loaded again.
* `removeEventListener` prevents multiple bindings if the script is run multiple times (common in Anki).

---

Let me know if you also want to include this setup as part of your **custom Anki card type** so that you and your team can reuse it seamlessly.