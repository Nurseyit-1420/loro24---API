import requests
from peewee import *
import datetime

db = PostgresqlDatabase(
    'data_db',
    host = 'localhost',
    port = '5432',
    user = 'data',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class MyUser(BaseModel):
    username = CharField(max_length=255, null=False, unique=True)
    email = CharField(max_length=255)
    age = IntegerField()

class Kanie(BaseModel):
    title = CharField()
    slova = CharField()
    simvol = CharField()
    countglas = CharField()
    countsoglas = CharField()
    countsym = CharField ()
    point1 = CharField()
    point3 = CharField()
    #date = DateField(default=datetime.datetime.now)

db.create_tables([Kanie])

i = 0

sym = "!@#$%^*()_-+=/*+][}\ {',.?`~..."
sym2 = "!@#$%^*()_-+=/*+][}\ {,.?`~..."
glas = 'aeiouyAEIOUY'
soglas = 'qwrtpsdfghjklmnbvcxzQWRTPSDFGHJKLZXCVBNM'
allletter = 'aeiouyAEIOUYqwrtpsdfghjklmnbvcxzQWRTPSDFGHJKLZXCVBNM'
count = 0
quete = []
dli = []
dlina = []
dlib = []
dlinab =[]
a = []
b = " ',?...#%."
withoutsym = []
k=0
maxall = []
while i < 10:
    res = requests.get('https://api.kanye.rest/')

    a = res.json()
    for key, value in a.items():
        if value not in quete:
            quete.append(value)
            dlinasym = len(value)
            dli = (list(value.split()))            
            dlina = len(dli)
            
            countglas=0
            countsoglas=0
            countsym = 0
            
            # while k < 3:
            #     s = value.split()
            #     max =max(s ,key=len)
            #     maxall.append(max)
            #     value.replace(max,'')                
            # print(maxall)


            for j in value:
                # while k < 3:
                #     maxx =max(j ,key=len)
                #     maxall.append(maxx)
                #     maxx.remove()
                # print(maxall)
                
                if j in glas: # счет гласных
                    countglas+=1                    
                    #del j
                elif j in soglas: # счет согласных
                    countsoglas+=1
                elif j in sym:    # счет символов
                    countsym +=1  
                    del j
                
            countallletter=[]
            # print(countglas)
            # print(countsoglas)
            # print(countsym)
            # print(dli)  
            # print(value)
            # for k in dli:
            #     if k == '...':
            #         dli.remove('...')
            #         print('------------------------------------------------------------------------------------------------------------')
            #     if k in allletter:
            #         count+=1
            #         countallletter.append(count)
                    
            # print(count)
            # print(countallletter)
            # print(value)

                    
                    #dli.replace('...','')
                    
                    
                    # print(dli)
            
           
            

            i += 1
            Kanie.create(
                title = value,
                slova = dlina,
                simvol = dlinasym,
                countglas = countglas,
                countsoglas = countsoglas,
                countsym = countsym ,
                point1 = countglas + countsoglas,
                point3 = (countglas + countsoglas) / dlina,
            )


db.close()