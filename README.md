# os-2026-ChirilMacari

Operating Systems labs · FCIM / FAF · UTM · 2026-2027
Chiril-Adam Macari, FAF-243

| Lab | Topic | Report | Code |
|---|---|---|---|
| [1](lab1/) | The OS as a Resource Manager (Linux) | [Lab1-2_ChirilMacari_FAF-243.docx](lab2/Lab1-2_ChirilMacari_FAF-243.docx) (Lab 1 section), [lab1/report.md](lab1/report.md) | – (commands only) |
| [2](lab2/) | Meet the OS You Will Build (xv6) | [Lab1-2_ChirilMacari_FAF-243.docx](lab2/Lab1-2_ChirilMacari_FAF-243.docx) (Lab 2 section), [lab2/notes.md](lab2/notes.md) | [user/sleep.c](lab2/user/sleep.c), [Makefile](lab2/Makefile) |
| [3](lab3/) | The Command Line: Shell, Pipes and Text Filters | [Lab3_ChirilMacari_FAF-243.docx](lab3/Lab3_ChirilMacari_FAF-243.docx) | [oneliners.sh](lab3/oneliners.sh), [report.sh](lab3/report.sh) |
| [4](lab4/) | The xv6 Shell from the Outside | [Lab4_ChirilMacari_FAF-243.docx](lab4/Lab4_ChirilMacari_FAF-243.docx) | [sleep.c](lab4/sleep.c), [args.c](lab4/args.c), [args_linux.c](lab4/args_linux.c), [Makefile](lab4/Makefile) |
| [5](lab5/) | The File System with Your Own Hands (Linux) | [Lab5-6_ChirilMacari_FAF-243.docx](lab6/Lab5-6_ChirilMacari_FAF-243.docx) (Lab 5 section) | – (commands only) |
| [6](lab6/) | Inside the xv6 File System | [Lab5-6_ChirilMacari_FAF-243.docx](lab6/Lab5-6_ChirilMacari_FAF-243.docx) (Lab 6 section) | [mystat.c](lab6/mystat.c), [find.c](lab6/find.c), [Makefile](lab6/Makefile) |
| [7](lab7/) | Three Small Programs: Processes, Redirection, a Pipe (Linux) | [Lab7-8_ChirilMacari_FAF-243.docx](lab8/Lab7-8_ChirilMacari_FAF-243.docx) (Lab 7 section) | [run.c](lab7/run.c), [zombie.c](lab7/zombie.c), [redirect.c](lab7/redirect.c), [pipeline.c](lab7/pipeline.c), [pipeline3.c](lab7/pipeline3.c) |
| [8](lab8/) | The Same Calls, Inside Your Own OS (xv6) | [Lab7-8_ChirilMacari_FAF-243.docx](lab8/Lab7-8_ChirilMacari_FAF-243.docx) (Lab 8 section) | [run.c](lab8/run.c), [pingpong.c](lab8/pingpong.c), [primes.c](lab8/primes.c), [Makefile](lab8/Makefile) |

Labs 1–2, 5–6 and 7–8 each have one combined Word report with a separate section for every lab.
The xv6 programs build on xv6-riscv revision `06aad25` (`make qemu`); `sleep.c` uses `pause()`.
