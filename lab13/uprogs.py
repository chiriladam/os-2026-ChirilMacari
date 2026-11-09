# uprogs.py - Lab 13, Part 1.6: put semtest and mix in UPROGS, after _zombie (lines start with a TAB).
BS = chr(92)  # backslash
p = 'Makefile'
s = open(p).read()
z = '\t$U/_zombie' + BS + '\n'
if z not in s:
    raise SystemExit('Makefile: _zombie line not found')
if '_semtest' in s:
    print('already Makefile (UPROGS)')
else:
    s = s.replace(z, z + '\t$U/_semtest' + BS + '\n\t$U/_mix' + BS + '\n', 1)
    open(p, 'w').write(s)
    print('ok Makefile (UPROGS)')
