import csv
from datetime import date,timedelta,datetime
def num(nbr):
    nbr = str(nbr)
    liste = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    verif = 0
    
    for i in range (0, len(str(nbr))):
        for z in range (0, len(liste)):
            if nbr[i]== liste[z]:
                verif += 1
                break
    if verif == len(nbr):
        return True
    else:
        return False
def write_NBP(date,M,F,NDP):
    print("[INFO   ] [write_NBP   ] ",date, M, F, NDP)
    
   
    original = open("data_couv.csv", "r")
    reader = csv.reader(original)
    file_list = []
    done = False
    start = 0
    for row in reader:
        if start == 0:
            header = row
            start =1
        #print(row)


        print(date ,row[2] , row[4] , M , row[6],F)
        if done == False and date ==row[2] and row[4] == M and row[6]==F:
            #print(len(row))
            if len(row) >= 5:
                #print("1")
                row[8] = str(NDP)
            else:
                #print("2")
                row.append(str(NDP))
            done = True
        
        file_list.append(row)
   
    
    #print(file_list)
        
        

    original.close()
    print("[INFO   ] [MOI         ] ",file_list, done)

    new = open("data_couv.csv", "w")
    
    for i in file_list:

        print(','.join(i))
        new.write(','.join(i)+"\n")
   






def verif(nbr):
    
    liste = ["\\","/"]
    barre1= 0
    barre2= 0
    for i in range (0, len(nbr)):
        
        if num(nbr[i]) == False:
            if barre1==0:
                barre1=i
            else:
                barre2=i
    if barre1==0:
        return False
    
    if int(nbr[0:barre1])>31:
        return False
    if int(nbr[barre1+1:barre2])>12:
        return False
    
    for z in range(0,2):
        if nbr[barre1]==liste[z]:
            for z in range(0,2):
                if nbr[barre2]==liste[z]:
                    return True
    
    return False
def sommedate(date,temp):
    print(date,"+",temp)
    new_date = datetime(int(date[6:10]), int(date[3:5]), int(date[:2])) + timedelta(temp)
    dt_string = new_date.strftime("%d/%m/%Y")
    print(dt_string)
    return dt_string




def read(x,y):
    reponse="none"
    import csv

    f = open('data_couv.csv', 'r')

    reader = csv.reader(f)
        
    xx=0
    yy=0
    try:
        while True:
            for row in reader:
                yy+=1
                xx=0
                for e in row:
                    xx+=1
                    if yy == y:
                    
                        if xx == x:
                        
                            reponse = e
                            return reponse
    except:
        
        return reponse



def verifV():
    pass
    '''
    print("[INFO   ] [MOI         ] start")
    nbr = 0
    import csv

    #f = open('D:\pgOS\data_couv.csv', 'r')
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)
    print(reader)
    liste = []
    x=1
    for row in reader:

        if row[4] == 'V':
            liste.append(x)
        
        x+=1
  
    return liste



verifV()
'''


def testdict(dic,key):
    if key in dic:
        return True
    return False


def updatelist():
       
        try:        
                ff= open("Flist.txt","r+")
                fm=open("Mlist.txt","r+")
               
        except:
                fm= open("Mlist.txt","w+")
                ff= open("Flist.txt","w+")
               

       
        fmreader = fm.readlines()
        
        fmlist = eval(fmreader[0])
        
        ffreader = ff.readlines()

        fflist = eval(ffreader[0])
        return fflist, fmlist

def convertdict(dic):
    dic = str(dic)
    retur = ()
    x = 0
    while True:
        start = 0
        end = 0
        for i in range (0,len(dic)):
            
            if dic[i] == ",":
                start = i
                for z in range (i,len(dic)):
                
                    if dic[z] == ":":
                        
                        end = z
                        break
           
                retur = retur + (dic[int(start)+3:end-1],)
            if dic[i] == "{" :
                start = i
                for z in range (i,len(dic)):
                  
                    if dic[z] == ":":
                        
                        end = z
                        break
              
                retur = retur + (dic[int(start)+2:end-1],)
        
        break
    return retur


def dic_to_str(dic):
    
    rep=""
    print("[INFO   ] [MOI         ] ", dic)
    rep = dic["Date"]+","+dic["Dure"]+","+dic["Fin"]+","+dic["Valide"]+","+dic["M"]+","+dic["F"]+dic['NDP']+"\n"


    return rep



def update_cvs_to_F(csv_name, y, valide):
    print("[INFO   ] [MOI         ] ",csv_name,y,valide)
    import csv
    y =y-1
    file = str(csv_name)+".csv"
    
    file_list=[]

    original = open(file, "r")
    reader = csv.DictReader(original , delimiter = ',')
    for row in reader:
        
        file_list.append(row)
   
    ################### edition
    new_file_list=[0]*len(file_list)
    for i in range(len(file_list)):
        
        if i==y:
            
            edit_dic = dict(file_list[i])
            edit_dic["Valide"]= valide
            new_file_list[i]=edit_dic
            
        else:
            new_file_list[i]=file_list[i]


    original.close()
    print("[INFO   ] [MOI         ] ",new_file_list)
    
    new_file = str(csv_name)+".csv"
    
    new = open(file, "w")
    fieldnames ="Date,Duré,Fin,Valide,M,F,NBP\n"
    
    
    new.write(fieldnames)
    for i in new_file_list:
        new.write(dic_to_str(dict(i)))









def update_csv(csv_name):
    pass
    """
    import csv
    file = str(csv_name)+".csv"
    
    file_list=[]

    original = open(file, "r")
    reader = csv.DictReader(original , delimiter = ',')
    for row in reader:
        
        file_list.append(row)
   
    ################### edition
    new_file_list=[]
    for i in range(len(file_list)):

        edit_dic = dict(file_list[i])
        valide= edit_dic["Valide"]
        #if valide=="V":    #supprimer les viellie info
        new_file_list.append(file_list[i])

            
    original.close()
    
    new_file = str(csv_name)+".csv"
    
    new = open(file, "w")
    fieldnames ="Date,Duré,Fin,Valide,M,F\n"
    
    
    new.write(fieldnames)
    for i in new_file_list:
        #print(i)
        new.write(dic_to_str(dict(i)))

#update_csv("Data_couv")

    """

def list_for_tabel():
    print("[INFO   ] [MOI         ] list_for_tabel run")
    #print(verifV())
    list_tabel =[]
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)

    for row in reader:
        #print(row)
        if row[3] == 'V':

            list_tabel.append([row[2],row[4],row[6],row[8],row[5], row[7] ])
    print("[INFO   ] [MOI         ] list_for_tabel finish")
    f.close()
    print(list_tabel)
    return list_tabel
print(list_for_tabel())
            
def temps_restant(date): 
    import datetime
    if verif(date) == True:
        str(date)
        anne=int(date[6:10])
        mois = int(date[3:5])
        jours = int(date[0:2])
        tday = datetime.date.today()
        day = datetime.date(anne, mois, jours)
        j_restant = str(day - tday)
        #print(j_restant)
        for i in range(len(j_restant)):
            #print(j_restant[i])
            if j_restant[i] == " ":
                #print("trye")
                indice = i
                
                return int(j_restant[0:indice])
        return 0


def CLE_Fin(ligne):
    return int( temps_restant(ligne['Fin']))

def ranger_csv(csv_name):
    print("ranger")
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)
    LD = []
    x = 0
    header = None
    for row in reader:
        if len(row) == 9:
            if x != 0:
                #print(row[2],int( temps_restant(row[2])))
                if int( temps_restant(row[2]))<=-7:
                    row[3] = 'F'
                LD.append({'time':row[2],'row':row})
            else:
                header = row
                x=1
    f.close()
    LD =  sorted(LD, key=lambda k: int( temps_restant(k['time'])))

    new = open('data_couv.csv', "w")
    new.write(','.join(header)+'\n')
    for i in LD:
        
        new.write(','.join(i['row'])+'\n')
    new.close()


#ranger_csv("D:\pgOS\data_couv")
def ranger_csv_sans_r(L):
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)
    LD = []
    x = 0
    header = None
    for row in reader:
        if len(row) == 9:
            if x != 0:
            
                LD.append({'time':row[2],'row':row})
            else:
                header = row
                x=1
    f.close()
    LD =  sorted(LD, key=lambda k: int( temps_restant(k['time'])))

    new = open('data_couv.csv', "w")
    new.write(','.join(header)+'\n')
    for i in LD:
        
        new.write(','.join(i['row'])+'\n')
    new.close()

def remove_csv(L):
    print('L', L)
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)
    LD = []
    x = 0
    header = None
    for row in reader:
        if len(row) == 9:
            if x != 0:
                #print(row[2],int( temps_restant(row[2])))
                #if int( temps_restant(row[2]))<=-7:
                    #row[3] = 'F'
                #else: 
                    #row[3] = 'V'

                LD.append({'time':row[2],'row':row})
            else:
                header = row
                x=1
    f.close()
    print('LD',LD)
    #LD =  sorted(LD, key=lambda k: int( temps_restant(k['time'])))
    for i in L:
        for z in range(len(LD)):
           
            w = LD[z]['row']
            if w[2] == i['D'] and w[4]==i['M'] and w[5]==i['NM'] and w[6]==i['F'] and w[7]==i['NF'] and w[3] == 'V':
                #print("\n","i founnnnnnnnnnd",w[2], i['D'] and w[4],i['M'] and w[5],i['NM'] and w[6],i['F'] and w[7],i['NF'])
                LD.pop(z)
                break

    LD =  sorted(LD, key=lambda k: int( temps_restant(k['time'])))
    #print(LD)
    new = open('data_couv.csv', "w")
    new.write(','.join(header)+'\n')
    for i in LD:
        
        new.write(','.join(i['row'])+'\n')
    new.close()
#remove_csv([])


def cleandate(indate):
    
    dateclean = str(indate)[8:10]+"/"+str(indate)[5:7]+"/"+str(indate)[0:4]

    return dateclean

def write_csv(indate,M,F,NM, NF):

    from datetime import date

    #today = date.today()
    today = indate
    #print(str(indate))
    dateclean = cleandate(indate)

    file = open("data_couv.csv", "a")

    file.write(str(cleandate(today))+","+str(18)+","+sommedate((dateclean),int(18))+","+"V"+','+str(M)+","+str(NM)+","+str(F)+","+str(NF)+','+''+"\n")
    file.flush()
    file.close()

def dic_to_list(dic):
    liste= []
    for i in dic:
        liste.append(i)
        
    return liste
def list_to_drop_down(liste):
    temp_list = [{'text':f'{i}'}for i in liste]
    return temp_list
def list_to_drop_down_zip(liste):
    retur = []
    for i in liste:
        retur.append({'text':i['name'][:len(i)-5]})

    return retur
def list_write(M_F, name, num, PF, PM, NBP=[]):
    print("[INFO   ] [MOI         ] ", M_F, name, num, PF, PM, NBP)
    if M_F == "M":
        file = open("Mlist.txt", "r")
        reader = file.readlines()
        save = reader[0]
        file.close()
        save = eval(save)
        xx = {'name':name, 'num':num, 'PF':PF, 'PM':PM, 'NBP':NBP}
        save = [xx]+save
    
        
        file = open("Mlist.txt", "w")
        file.write(str(save))
        file.close()
    if M_F == "F":
        file = open("Flist.txt", "r")
        reader = file.readlines()
        save = reader[0]
        file.close()
        save = eval(save)
        xx = {'name':name, 'num':num, 'PF':PF, 'PM':PM, 'NBP':NBP}
        save = [xx]+save
        
        file = open("Flist.txt", "w")
        file.write(str(save))
        file.close()
def list_remove(M_F, name, num):
    if M_F == "M":
        file = open("Mlist.txt", "r")
        reader = file.readlines()
        save = reader[0]
        file.close()
        save = eval(save)
        for i in save:
            if i['name'] == name and i['num'] == num:
                break
        save.remove(i)
        
        
        file = open("Mlist.txt", "w")
        file.write(str(save))
        file.close()
    if M_F == "F":
        file = open("Flist.txt", "r")
        reader = file.readlines()
        save = reader[0]
        file.close()
        save = eval(save)
        for i in save:
            if i['name'] == name and i['num'] == num:
                break
        save.remove(i)
        
        file = open("Flist.txt", "w")
        file.write(str(save))
        file.close()





#write_NBP('15/12/2020','Culbutant Rouge','Culbutant Jaune',0)
