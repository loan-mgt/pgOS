

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
    mois_en_j=dict({"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31})
    z=date[3:5]
    if (int(date[6:10]))%4 == 0:
        mois_en_j=dict({"01":31,"02":29,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31})
    else:
        mois_en_j=dict({"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31})
        
    nbr_de_jour= mois_en_j[date[3:5]]
    j_total= temp+int(date[0:2])
    if j_total/nbr_de_jour <= 1:
        
        if j_total<10:
            j_total= "0"+str(j_total)
        ret= str(j_total)+str(date[2:10])
        return ret
    else:
        while int(j_total)/int(nbr_de_jour) > 1:
            if (int(date[6:10]))%4 == 0:
                mois_en_j=dict({"01":31,"02":29,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31})
            else:
                mois_en_j=dict({"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31})
        
            j_total= j_total-int(nbr_de_jour)
            
            if j_total<10:
                j_total="0"+str(j_total)
            mois= str(int(date[3:5])+1)
            if int(mois)<10:
                mois= "0"+str(mois[len(mois)-1])
            date=str(j_total)+"/"+mois+date[5:10]
            if int(date[3:5]) > int(12):
                innt=int(date[6:10])+1
                date= str(date[0:3])+"01/"+str(innt)

        return date




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
    nbr = 0
    import csv

    #f = open('D:\pgOS\data_couv.csv', 'r')
    f = open('data_couv.csv', 'r')
    
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            nbr += 1
    nbr= nbr/6
    liste = []
    y = 2
    B = True
    while y < nbr+1:
        try:
            if read(4,y) == "V":
                liste.append(y)
        except:
            B = False
        y += 1
    return liste







def testdict(dic,key):
    if key in dic:
        return True
    return False
d={'a':1,'b':2,'c':3}

def updatelist(fflist,fmlist):
        #import os
        #global fflist
        #global fmlist
        try:
                        
                ff= open("Flist.txt","r+")
                fm=open("Mlist.txt","r+")
               
        except:
                fm= open("Mlist.txt","w+")
                ff= open("Flist.txt","w+")
               

        #if os.stat("Flist.txt").st_size == 0:
         #       ff.write('{"none":"none"}')
          #      ff.close()
           #     ff= open("Flist.txt","r+")
        #if os.stat("Mlist.txt").st_size == 0:
         #       fm.write('{"none":"none"}')
          #      fm.close()
           #     fm=open("Mlist.txt","r+")
        fmreader = fm.readlines()
        for row in fmreader:
                fmlist = row
        fmlist = eval(fmlist)
        
        ffreader = ff.readlines()
        for row in ffreader:
                fflist = row
        fflist = eval(fflist)
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
    import csv
    rep=""
    rep = dic["Date"]+","+dic["Dure"]+","+dic["Fin"]+","+dic["Valide"]+","+dic["M"]+","+dic["F"]+"\n"


    return rep



def update_cvs_to_F(csv_name, y, valide):
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
    
    new_file = str(csv_name)+".csv"
    
    new = open(file, "w")
    fieldnames ="Date,Duré,Fin,Valide,M,F\n"
    
    
    new.write(fieldnames)
    for i in new_file_list:
        new.write(dic_to_str(dict(i)))









def update_csv(csv_name):
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



def list_for_tabel():
    #print(verifV())
    list_tabel =[]
    list_verif = verifV()
    #tableaucouv.insert_row([read(3,liste[z-1]),read(5,liste[z-1]),read(6,liste[z-1])])
    z =1
    for i in list_verif:
       
        list_tabel.append([read(3,i),read(5,i),read(6,i)])
        
    return list_tabel
            
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
    import csv
    file = str(csv_name)+".csv"
    
    file_list=[]

    original = open(file, "r")
    reader = csv.DictReader(original , delimiter = ',')
    for row in reader:
        
        file_list.append(row)
    original.close()
    ################### edition
    new_file_list=[]
   
    ordre= {}

    for i in range(len(file_list)):
        file_listi=file_list[i]
       
        if temps_restant(file_listi["Fin"]) > -8:
            up = {i:temps_restant(file_listi["Fin"])}
            ordre.update(up)
           
    for i in ordre:
        new_file_list.append(file_list[i])
   
    new_file_list = sorted(new_file_list, key=CLE_Fin, reverse = False)
  
    
            
            
    
    ##########réecriture
    new_file = str(csv_name)+".csv"
    
    new = open(file, "w")
    fieldnames ="Date,Dure,Fin,Valide,M,F\n"
    
    
    new.write(fieldnames)
    for i in new_file_list:
        
        new.write(dic_to_str(dict(i)))

#ranger_csv("D:\pgOS\data_couv")
def cleandate(indate):
    
    dateclean = str(indate)[8:10]+"/"+str(indate)[5:7]+"/"+str(indate)[0:4]

    return dateclean

def write_csv(indate,M,F):

    from datetime import date

    #today = date.today()
    today = indate
    #print(str(indate))
    dateclean = cleandate(indate)

    file = open("data_couv.csv", "a")

    file.write(str(cleandate(today))+","+str(18)+","+sommedate((dateclean),int(18))+","+"V"+','+str(M)+","+str(F)+"\n")
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
def list_write(M_F, name, num):
    if M_F == "M":
        file = open("Mlist.txt", "r")
        reader = file.readlines()
        try:
            save = reader[0]
            #print(save)
        except:
            save = {}
        file.close()
        #print(save)
        save = eval(save)
        #print(save, type(save), "save")
        save[name] = num
        
        file = open("Mlist.txt", "w")
        file.write(str(save))
        file.close
    if M_F == "F":
        file = open("Flist.txt", "r")
        reader = file.readlines()
        try:
            save = reader[0]
            #print(save)
        except:
            save = {}
        file.close()
        #print(save)
        save = eval(save)
        #print(save, type(save), "save")
        save[name] = num
        
        file = open("Flist.txt", "w")
        file.write(str(save))
        file.close
def list_remove(M_F, name, num):
    if M_F == "M":
        file = open("Mlist.txt", "r")
        reader = file.readlines()
        try:
            save = reader[0]
            #print(save)
        except:
            save = {}
        file.close()
        #print(save)
        save = eval(save)
        #print(save, type(save), "save")
        del save[name]
        
        file = open("Mlist.txt", "w")
        file.write(str(save))
        file.close
    if M_F == "F":
        file = open("Flist.txt", "r")
        reader = file.readlines()
        try:
            save = reader[0]
            #print(save)
        except:
            save = {}
        file.close()
        #print(save)
        save = eval(save)
        #print(save, type(save), "save")
        del save[name]
        
        file = open("Flist.txt", "w")
        file.write(str(save))
        file.close






