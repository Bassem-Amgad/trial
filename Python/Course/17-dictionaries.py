ex ={'a':12,'b':17,'c':14,'d':32,'e':20}
print(ex)
print(ex['d'])
ex['f']=7
print(ex)
ex['f']=8
print(ex)
del ex['f']
print(ex)

ex ={'a':[12,'red'],'b':[17,'green'],'c':[14,'yellow'],'d':[32,'black'],'e':[20,'purple']}
print(ex['d'])
print(ex['e'][1])
