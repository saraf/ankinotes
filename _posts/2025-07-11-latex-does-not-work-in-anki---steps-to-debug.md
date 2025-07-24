---
date: '2025-07-11 11:18:39'
layout: post
tags:
- StudyNotes/StudyTech
title: LaTeX does not work in Anki - steps to debug
---

# LaTeX does not work in Anki - steps to debug
Created on: 2025-07-11T16:48:58


```
This is pdfTeX, Version 3.141592653-2.6-1.40.27 (MiKTeX 25.4) (preloaded format=latex.fmt)
 restricted \write18 enabled.
entering extended mode
(tmp.tex
LaTeX2e <2025-06-01> patch level 1
L3 programming layer <2025-05-26>
(C:\Program Files\MiKTeX\tex/latex/base\article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(C:\Program Files\MiKTeX\tex/latex/base\size12.clo))
(C:\Program Files\MiKTeX\tex/latex/base\inputenc.sty)
(C:\Program Files\MiKTeX\tex/latex/amsfonts\amssymb.sty
(C:\Program Files\MiKTeX\tex/latex/amsfonts\amsfonts.sty))
(C:\Program Files\MiKTeX\tex/latex/amsmath\amsmath.sty
For additional information on amsmath, use the `?' option.
(C:\Program Files\MiKTeX\tex/latex/amsmath\amstext.sty
(C:\Program Files\MiKTeX\tex/latex/amsmath\amsgen.sty))
(C:\Program Files\MiKTeX\tex/latex/amsmath\amsbsy.sty)
(C:\Program Files\MiKTeX\tex/latex/amsmath\amsopn.sty))
(C:\Program Files\MiKTeX\tex/latex/l3backend\l3backend-dvips.def)
No file tmp.aux.
(C:\Program Files\MiKTeX\tex/latex/amsfonts\umsa.fd)
(C:\Program Files\MiKTeX\tex/latex/amsfonts\umsb.fd)
! Too many }'s.
l.9 ...\\ 4 & 5 & 6 \\ 7 & 8 & 9 \\ \end{tabular}}
```

Assuming you're on Windows. Let me know and stop when the steps start to fail:

- Install LaTeX (I use https://miktex.org/, it can go up to a few GB, if you don't have the free space then just install the core libraries).

- (optional) (Windows Key + R) -> cmd -> Enter -> type in latex, see if the command executed successfully, then close the window.

- Open up c:\users\samua\appdata\local\temp\anki_temp\

- Shift+Right click in Windows Explorer. Either open Poweshell/Command Prompt in the current location.

- Delete all files in the folder aside from tmp.tex

- type in: latex tmp.tex

- if a .dvi file is created, run: dvipng -D 200 -T tight tmp.dvi -o tmp.png

- During one of these steps, a dialog box should appear (which is what caused Anki to fail). Handle the dialog box.

LaTeX should now work.