from time import gmtime, strftime
from firebase import firebase
firebase = firebase.FirebaseApplication('https://trial-fc3c2.firebaseio.com/', None)
#firebase = firebase.FirebaseApplication('https://my-unawesome-project.firebaseio.com/', None)
#firebase.delete('/', None)
x=1
if x==1:
    IP1_Temp_data =37 #36.5-->37.2
    IP1_Heart_date=79 #72-->80
    IP1_o2_data=97    #95-->100

    IP2_Temp_data =36.8
    IP2_Heart_date=77
    IP2_o2_data=96
else :
    IP1_Temp_data =36.7 #36.5-->37.2
    IP1_Heart_date=75 #72-->80
    IP1_o2_data=98    #95-->100

    IP2_Temp_data =37.1
    IP2_Heart_date=76
    IP2_o2_data=95
    
#strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
firebase.put('/IP_1',strftime("%a, %d-%m-%Y %H:%M:%S", gmtime()),{'Temp': IP1_Temp_data,'Heart Rate': IP1_Heart_date,'O2': IP1_o2_data})
firebase.put('/IP_2',strftime("%a, %d-%m-%Y %H:%M:%S", gmtime()),{'Temp': IP2_Temp_data,'Heart Rate': IP2_Heart_date,'O2': IP2_o2_data})

#return everything
result = firebase.get('/', None)
print (result)
#return specifc child
result = firebase.get('/IP_1', None)
print (result)
