# uthread_mk.py - Lab 18, Part 1.3: put _uthread in UPROGS (after _mix, a TAB line)
# and add the rule for _uthread (uthread.o + uthread_switch.o) at the end of the Makefile.
BS = chr(92)  # backslash
p = 'Makefile'
s = open(p).read()
m = '\t$U/_mix' + BS + '\n'
if m not in s:
    raise SystemExit('Makefile: _mix line not found, nothing changed')
rule = ('\n$U/_uthread: $U/uthread.o $U/uthread_switch.o $(ULIB) $U/user.ld\n'
        '\t$(LD) $(LDFLAGS) -T $U/user.ld -o $U/_uthread $U/uthread.o $U/uthread_switch.o $(ULIB)\n'
        '\t$(OBJDUMP) -S $U/_uthread > $U/uthread.asm\n')
if '_uthread' + BS in s:
    print('already Makefile (UPROGS)')
else:
    s = s.replace(m, m + '\t$U/_uthread' + BS + '\n', 1)
    print('ok Makefile (UPROGS)')
if '$U/_uthread:' in s:
    print('already Makefile (rule)')
else:
    s = s.rstrip('\n') + '\n' + rule
    print('ok Makefile (rule)')
open(p, 'w').write(s)
