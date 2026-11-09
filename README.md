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
| [9](lab9/) | Watching System Calls with strace (Linux) | [Lab9_ChirilMacari_FAF-243.docx](lab9/Lab9_ChirilMacari_FAF-243.docx), [lab9/report.md](lab9/report.md) | [syscalls.c](lab9/syscalls.c) |
| [10](lab10/) | Add Your Own System Call: trace (xv6) | [Lab10_ChirilMacari_FAF-243.docx](lab10/Lab10_ChirilMacari_FAF-243.docx), [lab10/report.md](lab10/report.md), [notes.txt](lab10/notes.txt) | full modified tree [xv6-riscv/](lab10/xv6-riscv/) ([trace.c](lab10/xv6-riscv/user/trace.c), [syscall.c](lab10/xv6-riscv/kernel/syscall.c), [sysproc.c](lab10/xv6-riscv/kernel/sysproc.c)) |
| [11](lab11/) | The Race and the Semaphore (Linux) | [Lab11_ChirilMacari_FAF-243.docx](lab11/Lab11_ChirilMacari_FAF-243.docx), [lab11/report.md](lab11/report.md) | [race.c](lab11/race.c), [mutex.c](lab11/mutex.c), [sem.c](lab11/sem.c), [order.c](lab11/order.c), [parking.c](lab11/parking.c), [atomic.c](lab11/atomic.c) (optional) |
| [12](lab12/) | Producer, Consumer and the Other Tools (Linux) | [Lab12_ChirilMacari_FAF-243.docx](lab12/Lab12_ChirilMacari_FAF-243.docx), [lab12/report.md](lab12/report.md) | [prodcons.c](lab12/prodcons.c), [condvar.c](lab12/condvar.c), [readers.c](lab12/readers.c), [deadlock.c](lab12/deadlock.c) (fixed) |
| [13](lab13/) | Semaphores in Your Own Kernel (xv6) | [Lab13_ChirilMacari_FAF-243.docx](lab13/Lab13_ChirilMacari_FAF-243.docx), [lab13/report.md](lab13/report.md), [notes.txt](lab13/notes.txt) | full modified tree [xv6-riscv/](lab13/xv6-riscv/) ([sem.c](lab13/xv6-riscv/kernel/sem.c), [syscall.c](lab13/xv6-riscv/kernel/syscall.c), [semtest.c](lab13/xv6-riscv/user/semtest.c), [mix.c](lab13/xv6-riscv/user/mix.c)) |

Labs 1–2, 5–6 and 7–8 each have one combined Word report with a separate section for every lab.
The xv6 programs build on xv6-riscv revision `06aad25` (`make qemu`); `sleep.c` uses `pause()`.
Lab 10 contains the whole modified xv6 tree (all programs from labs 2–10 plus the new `trace` system call, number 23).
Lab 13 contains the whole modified xv6 tree again (Lab 10 plus the kernel semaphores `sem_init`, `sem_down`, `sem_up`, numbers 24–26).
