# kernel_edits.py - Lab 13, Part 2: sem.o in OBJS and the three calls in the syscall table.
# Stops with an error if a place is not found, so nothing is applied half.
BS = chr(92)  # backslash


def edit(path, after, new):
    s = open(path).read()
    if new in s:
        print('already', path)
        return
    if after not in s:
        raise SystemExit(path + ': not found: ' + after.strip())
    s = s.replace(after, after + new, 1)
    open(path, 'w').write(s)
    print('ok', path)


# 2.2 Makefile: compile sem.c into the kernel (lines start with two spaces)
edit('Makefile', '  $K/sysproc.o ' + BS + '\n', '  $K/sem.o ' + BS + '\n')

# 2.3 kernel/syscall.c: the declarations ...
edit('kernel/syscall.c', 'extern uint64 sys_trace(void); // new\n',
     'extern uint64 sys_sem_init(void);   // new\n'
     'extern uint64 sys_sem_down(void);   // new\n'
     'extern uint64 sys_sem_up(void);     // new\n')
# ... and the table
edit('kernel/syscall.c', '[SYS_trace] = sys_trace, // new\n',
     '[SYS_sem_init] = sys_sem_init,   // new\n'
     '[SYS_sem_down] = sys_sem_down,   // new\n'
     '[SYS_sem_up]   = sys_sem_up,     // new\n')
