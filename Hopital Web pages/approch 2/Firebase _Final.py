from time import gmtime, strftime, localtime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://registration-7cc3f.firebaseio.com/', None)
#firebase = firebase.FirebaseApplication('https://my-unawesome-project.firebaseio.com/', None)
#firebase.delete('/', None)

Tag_1='0x01'
Name_1='Fatma'
Age_1='23'
Address_1='Alexandria'
Blood_1='A+'
Allergy_1='None'
Comments_1='None again'
firebase.put('/List',Tag_1,{'Name':Name_1,'Age': Age_1,'Address': Address_1,'Blood_Type': Blood_1,'Allergy': Allergy_1,'Comment': Comments_1})

Tag_2='0x02'
Name_2='Bassem'
Age_2='23'
Address_2='Alexandria'
Blood_2='A-'
Allergy_2='None'
Comments_2='None again'
firebase.put('/List',Tag_2,{'Name':Name_2,'Age': Age_2,'Address': Address_2,'Blood_Type': Blood_2,'Allergy': Allergy_2,'Comment': Comments_2})

Tag_3='0x03'
Name_3='Mariam'
Age_3='22'
Address_3='Alexandria'
Blood_3='B'
Allergy_3='None'
Comments_3='None again'
firebase.put('/List',Tag_3,{'Name':Name_3,'Age': Age_3,'Address': Address_3,'Blood_Type': Blood_3,'Allergy': Allergy_3,'Comment': Comments_3})

Tag_4='0x04'
Name_4='Youssef'
Age_4='23'
Address_4='Alexandria'
Blood_4='o'
Allergy_4='None'
Comments_4='None again'
firebase.put('/List',Tag_4,{'Name':Name_4,'Age': Age_4,'Address': Address_4,'Blood_Type': Blood_4,'Allergy': Allergy_4,'Comment': Comments_4})

Tag_5='0x05'
Name_5='Sara Youssif'
Age_5='22'
Address_5='Alexandria'
Blood_5='A+'
Allergy_5='None'
Comments_5='None again'
firebase.put('/List',Tag_5,{'Name':Name_5,'Age': Age_5,'Address': Address_5,'Blood_Type': Blood_5,'Allergy': Allergy_5,'Comment': Comments_5})

Tag_6='0x06'
Name_6='Sara Hamdy'
Age_6='23'
Address_6='Alexandria'
Blood_6='B'
Allergy_6='None'
Comments_6='None again'
firebase.put('/List',Tag_6,{'Name':Name_6,'Age': Age_6,'Address': Address_6,'Blood_Type': Blood_6,'Allergy': Allergy_6,'Comment': Comments_6})

Tag_7='0x07'
Name_7='Menna Rostom'
Age_7='22'
Address_7='Alexandria'
Blood_7='o-'
Allergy_7='None'
Comments_7='None again'
firebase.put('/List',Tag_7,{'Name':Name_7,'Age': Age_7,'Address': Address_7,'Blood_Type': Blood_7,'Allergy': Allergy_7,'Comment': Comments_7})

Tag_8='0x08'
Name_8='Menna Samir'
Age_8='22'
Address_8='Alexandria'
Blood_8='B'
Allergy_8='None'
Comments_8='None again'
firebase.put('/List',Tag_8,{'Name':Name_8,'Age': Age_8,'Address': Address_8,'Blood_Type': Blood_8,'Allergy': Allergy_8,'Comment': Comments_8})

Tag_9='0x09'
Name_9='Mohamed Eldemery'
Age_9='23'
Address_9='Alexandria'
Blood_9='B'
Allergy_9='None'
Comments_9='None again'
firebase.put('/List',Tag_9,{'Name':Name_9,'Age': Age_9,'Address': Address_9,'Blood_Type': Blood_9,'Allergy': Allergy_9,'Comment': Comments_9})

#return everything
result = firebase.get('/', None)
print (result)
#return specifc child
result = firebase.get(Tag_1, None)
print (result)
