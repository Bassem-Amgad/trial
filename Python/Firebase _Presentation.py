from time import gmtime, strftime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://trial-fc3c2.firebaseio.com/', None)

IP1_Temp_data =33 #36.5-->37.2
IP1_Heart_date=78 #72-->80
#IP1_o2_data=97    #95-->100
    
#strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
firebase.put('/IP_1',strftime("%d-%m-%Y %a %H:%M:%S", gmtime()),{'Temp': IP1_Temp_data,'Heart Rate': IP1_Heart_date})#,'O2': IP1_o2_data})#return everything
result = firebase.get('/', None)
print (result)
#return specifc child
result = firebase.get('/IP_1', None)
print (result)
