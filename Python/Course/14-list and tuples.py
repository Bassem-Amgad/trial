# tuples can't be changed
x= 2,4,5,4
x=(2,3,4,1)
print(x[1])
def ex(): # sequence unpacking
    return 15,7
x,y=ex()
print(x)
print(y)

#Lists can be changed
y=[3,4,6,3,5]
print(y[2])
print(y[2:])
print(y[-1])
print(y.index(4))# get index value of the num
print(y.count(3))# get value of repetition of this element
x=[2,3,3,2]
x.append(4) # put element in the list
print(x)
x.insert(1,7)# (insert in position,value)
print(x)
x.remove(x[3])
print(x)
x.sort() # arrange list ascending order
print(x)
y=['samer','waleed','youssef','omar','ahmed','hesham','hatem']
y.sort()
print(y)
y=['roaa','essraa','fatma','sarah','lina','salma']
y.sort()
print(y)
#multi dimension lists
y=[[3,4],[2,4],[6,7],[2,3],[5,7]]
print(y[2])
print(y[2][1])
print(y[-1][0])
