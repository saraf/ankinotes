---
date: '2025-07-07 15:22:18'
layout: post
tags:
- StudyNotes/StudyTech
title: Manual decoding of UTF8
---

# Manual decoding of UTF8
Created on: 2025-07-07T20:52:36

### How Hexdump and UTF-8 Decoding Work (with '։' Example)

#### 1. What Does `echo "։" | hexdump -C` Show?

When you run:
```
echo "։" | hexdump -C
```
You see the UTF-8 encoded bytes for the Armenian full stop character '։'.

**Output:**
```
d6 89
```
This means the character '։' is stored as two bytes: `d6` and `89` in hexadecimal.

#### 2. Step-by-Step: Decoding the Bytes

Let's break down how these bytes represent '։' in Unicode.

##### a. Convert Hex to Binary

- `d6` in hex = `11010110` in binary
- `89` in hex = `10001001` in binary

So the bytes are:
```
11010110 10001001
```

##### b. Recognize the UTF-8 Pattern

For characters outside basic ASCII, UTF-8 uses two or more bytes.  
A 2-byte UTF-8 character follows this pattern:
```
110xxxxx 10xxxxxx
```
- The `x` bits hold the actual character data.

##### c. Extract the Data Bits

Take only the `x` bits:
- From `11010110`: the last 5 bits → `10110`
- From `10001001`: the last 6 bits → `001001`

Join them:
```
10110 001001
```

##### d. Combine and Convert to Decimal

Put the bits together: `10110001001`

- In decimal:  
  `1×2^10 + 0×2^9 + 1×2^8 + 1×2^7 + 0×2^6 + 0×2^5 + 0×2^4 + 1×2^3 + 0×2^2 + 0×2^1 + 1×2^0`  
  = 1024 + 256 + 128 + 8 + 1 = **1417**

##### e. Find the Unicode Code Point

- 1417 in hexadecimal = **0x589**
- Unicode notation: **U+0589**

This matches the Unicode for '։' (Armenian full stop).

### Summary Table

| Character | Hex Bytes | Binary | Unicode Code Point |
|-----------|-----------|----------------------|---------------------|
| '։'       | d6 89     | 11010110 10001001    | U+0589              |

### In Short

- The `hexdump` command shows the raw bytes for a character.
- UTF-8 encodes '։' as two bytes: `d6 89`.
- By extracting and combining the data bits, you get the Unicode code point U+0589, which is the Armenian full stop[1][2].

This is how UTF-8 encoding and decoding works for any character!

[1] https://www.charset.org/utf-8
[2] https://en.wikipedia.org/wiki/UTF-8
[3] https://webextension.org/listing/hexdump.html
[4] http://who-t.blogspot.com/2019/03/using-hexdump-to-print-binary-protocols.html
[5] https://www.linuxquestions.org/questions/linux-newbie-8/hexdump-xxd-930016/
[6] https://www.slideteam.net/understanding-hex-dump-a-comprehensive-guide-ppt-presentation-st-ai.html
[7] https://github.com/csm10495/cHexdump
[8] https://learn.microsoft.com/en-us/dotnet/api/system.text.encoding.utf8?view=net-9.0
[9] https://www.reddit.com/r/Ubuntu/comments/1bazjis/why_does_reading_a_file_with_hexdump_change_finds/
[10] https://www.fileformat.info/info/charset/UTF-8/list.htm
[11] https://linux.codidact.com/posts/284583
[12] https://blog.hubspot.com/website/what-is-utf-8
[13] https://developer.mozilla.org/en-US/docs/Glossary/UTF-8
[14] https://www.stata.com/statalist/archive/2009-11/msg00744.html
[15] https://www.w3schools.com/charsets/ref_html_utf8.asp
[16] https://www.ibm.com/docs/en/db2-for-zos/12.0.0?topic=unicode-utfs
[17] https://unix.stackexchange.com/questions/38160/grep-ing-from-a-to-b-in-hexdumps-output
[18] https://www.freecodecamp.org/news/what-is-utf-8-character-encoding/
[19] https://lokalise.com/blog/what-is-character-encoding-exploring-unicode-utf-8-ascii-and-more/
[20] https://www.utf8-chartable.de