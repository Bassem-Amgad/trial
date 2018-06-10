from time import gmtime, strftime, localtime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://reception-ef20c.firebaseio.com/', None)
#firebase.delete('/', None)

Tag=[]
Name=[]
Age=[]
Address=[]
Blood=[]
Allergy=[]
Comments=[]

Tag.append('0x01')
Name.append('Fatma')
Age.append('23')
Address.append('Alexandria')
Blood.append('A+')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x02')
Name.append('Bassem')
Age.append('23')
Address.append('Alexandria')
Blood.append('A-')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x03')
Name.append('Mariam')
Age.append('22')
Address.append('Alexandria')
Blood.append('B')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x04')
Name.append('Youssef')
Age.append('23')
Address.append('Alexandria')
Blood.append('o')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x05')
Name.append('Sara Youssif')
Age.append('22')
Address.append('Alexandria')
Blood.append('A+')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x06')
Name.append('Sara Hamdy')
Age.append('23')
Address.append('Alexandria')
Blood.append('B')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x07')
Name.append('Menna Rostom')
Age.append('22')
Address.append('Alexandria')
Blood.append('o-')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x08')
Name.append('Menna Samir')
Age.append('22')
Address.append('Alexandria')
Blood.append('B')
Allergy.append('None')
Comments.append('None again')

Tag.append('0x09')
Name.append('Mohamed Eldemery')
Age.append('23')
Address.append('Alexandria')
Blood.append('B')
Allergy.append('None')
Comments.append('None again')

for i in range(0, 8):
    firebase.put(Tag[i],'Name',Name[i])
    firebase.put(Tag[i],'Age',Age[i])
    firebase.put(Tag[i],'Address', Address[i])
    firebase.put(Tag[i],'Blood_Type',Blood[i])
    firebase.put(Tag[i],'Allergy',Allergy[i])
    firebase.put(Tag[i],'Comment', Comments[i])

#return everything
result = firebase.get('/', None)
print (result)
#return specifc child
result = firebase.get(Tag[0], None)
print (result)
