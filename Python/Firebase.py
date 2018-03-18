from time import gmtime, strftime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://trial-fc3c2.firebaseio.com/', None)

#firebase.delete('/', None)
#delete everything
#firebase.delete('/parent', None)
#delete everything under this node
#firebase.delete('/parent', 'child_name')
#delete this specific child
firebase.delete('/Number', None)
#firebase.delete('/', None)

#firebase.post('/parent_name',data)
#create a random variable which is a child to parent and hold value of data
data=7
firebase.post('/Number', data)
data=6
firebase.post('/Number', {'one': data,'Two': data+1})

#firebase.put('/parent_name','child_name',data)
#create a child with specific name which is a child to parent and hold value of data
# it overwrites previous values for the same child_name
x=1
if x==1:
    data =5
    firebase.put('/IP_1','Three', data)
    data =4
    firebase.put('/IP_1','Four', {'Four_child': data})
    firebase.put('/IP_1',strftime("%Y-%m-%d %H:%M:%S", gmtime()),data-1)
    data =3
    firebase.put('/IP_2','Two',{'one': data-1,'Two': data+2})
    data =4
    firebase.put('/IP_2','One', data)
else:
    data =5
    firebase.put('/IP_2','Three', data)
    data =4
    firebase.put('/IP_2','Four', {'Four_child': data})
    data =3
    firebase.put('/IP_1','Two',{'one': data-1,'Two': data+2})
    data =4
    firebase.put('/IP_1','One', data)
#return everything
result = firebase.get('/', None)
print (result)
#return specic child
result = firebase.get('/IP_2', None)
print (result)
#return specic child child
result = firebase.get('/IP_1/Three', None)
print (result)
