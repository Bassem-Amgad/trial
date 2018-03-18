'''
Identifiers:
\ used to escape a character
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character except a new line
\. actually a period
\b whitespace around words

Modifiers:
{1,3} we're expecting 1-3 e.g \d(1-3}
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ match the beginning of a string
| matches either or e.g. \d{1-3}|\w{5-6}
[] Match range or "variance" e.g. [A-Za-z] or [1-5a-qA-Z]
{x} expecting "x" amount

White Space Characters:
\n new line
\s space
\t tab
\e escape (rare)
\f form feed (rare)
\r return

DON'T FORGET!:
. + * ? [ ] $ ^ ( ) { } \ |﻿

'''
import re
ex='''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 47, his grandfather , Oscar,is 102.
'''
ages=re.findall(r'\d{1,3}',ex)
names=re.findall(r'[A-Z][a-z]*',ex)
print(ages)
print(names)

i=0
dict={}
for eachname in names:
    dict[eachname]=ages[i]
    i+=1
print (dict)
