x=1
z=3
y=6
def ex():
    global x
    print(x)
    x+=5
    print(x)
    print(z)
    '''
   z+=5 will give error as it isn't global variable so u can't adjust
   it but somehow u can print it 
    '''
    globy=y
    print (globy)
    globy+=5
    print(globy)
    return globy
    

y=ex()
print (y)
