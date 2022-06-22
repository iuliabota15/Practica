from tkinter import X
from bs4 import BeautifulSoup
import requests

text=requests.get('https://www.olx.ro/').text
soup=BeautifulSoup(text,'lxml')

print('Alege o functionalitate:\n1.Pretul si denumirea tururor produselor de pe pagina principala\n2.Afisare link-uri catre produsele de pe pagina principala\n3.Afisare categorii principale\n4.Afisare link-uri catre categoriile principale\n5.Afisare functionalitati\n6.Cautare anunturi dupa cuvinte cheie introduse\n7.Iesire din meniu\n')

denumire=[]
pret=[]
vector=[]
preturi=soup.find_all('div',class_='price')
for course in preturi:
    course_pret=course.text.replace('\t','')
    course_pret2=course_pret.replace('\n','')
    pret.append(course_pret2)

denumiri=soup.find_all('h4',class_='normal')
for course in denumiri:
    den=course.a.text
    den2=den.replace('\n','')
    denumire.append(den2)

i=0
for ceva in denumiri:
    vector.append(denumire[i]+" are pretul de "+pret[i])
    i+=1

link=[]
categorii=soup.find_all('div',class_='mheight tcenter')
nr=0
for course in categorii:
    cat=course.a
    cat2=cat.get('href')
    link.append(cat2)
    nr+=1

link2=[]
categorii2=soup.find_all('div',class_='item')
nr2=0
for course in categorii2:
    cat31=course.a
    cat3=cat31.get('href')
    link2.append(cat3)
    nr2+=1





ok=0
while(ok==0):
    a = input()
    b=int(a)
    #pretul si denumirea
    if (b==1):
        print('Denumirea si pretul produselor sunt:\n')
        i=0
        for ceva in denumiri:
            print(vector[i])
            i+=1
        print('\n\n\n')

    #categorii principale
    elif(b==3):
        print("Categoriile principale sunt:")
        categorii=soup.find_all('div',class_='item')
        for course in categorii:
            cat=course.text.replace('\n','')
            cat2=cat.replace('\t','')
            print(cat2)
            print(',')
        print('\n\n\n')
    #functionalitati
    elif(b==5):
        print("Functionalitatile sunt:")
        anunturi=soup.find_all('li',class_='block')
        for course in anunturi:
            func=course.text.replace('\n','')
            print(func)
            print(',')
        print('\n\n\n')

    #link urile catre categorii
    elif(b==4):
        print('Link-urile catre categorii sunt:')
        categorii=soup.find_all('div',class_='item')
        for course in categorii:
            cat=course.a
            cat2=cat.get('href')
            print(cat2)
        print('\n\n\n')

    #link urile catre produse
    elif(b==2):
        print('Link-urile catre produse sunt:')
        categorii=soup.find_all('div',class_='mheight tcenter')
        nr=0
        for course in categorii:
            cat=course.a
            cat2=cat.get('href')
            print(cat2)
            nr+=1
    #cautare dupa cuvinte cheie
    elif(b==6):
        print('Introduceti cuvantul cheie:')
        cuvinte_cheie=input()
        cuvinte_cheie.replace(" ","-")
        link_cheie='https://www.olx.ro/d/oferte/q-'+cuvinte_cheie+"/"
        text=requests.get(link_cheie).text
        soup=BeautifulSoup(text,'lxml')
        print('Cate produse am gasit?')
        produse=soup.find_all('h3',class_='css-pqvw3x-Text eu5v0x0')
        for course in produse:
            print(course.text)
        
        denumire_cuv_cheie=[]
        pret_cuv_cheie=[]
        vector_cuv_cheie=[]
        preturi=soup.find_all('p',class_='css-wpfvmn-Text eu5v0x0')
        for course in preturi:
            course_pret=course.text.replace('\t','')
            course_pret2=course_pret.replace('\n','')
            pret_cuv_cheie.append(course_pret2)

        denumiri=soup.find_all('h6',class_='css-v3vynn-Text eu5v0x0')
        for course in denumiri:
            den=course.text
            den2=den.replace('\n','')
            denumire_cuv_cheie.append(den2)

        i=0
        
        for ceva in range(10):
            j=i+1
            vector_cuv_cheie.append(str(j)+". "+denumire_cuv_cheie[i]+" are pretul de "+pret_cuv_cheie[i])
            print(vector_cuv_cheie[i])
            i+=1

        
    #iesire din meniu
    elif(b==7):
        ok+=1

    else:
        print('!!ERROR!!\nNumarul citit de la tastatura nu se regaseste in optiuni..')



print('Intrare in pagina unui anunt\n')
print('Alege un numar de la 1 la ',nr)

input_a = input()
input_b=int(input_a)
print('Link ul catre produs este: ',link[input_b-1])

link[input_b-1]=link[input_b-1].replace('\n','')

text=requests.get(link[input_b-1]).text
soup=BeautifulSoup(text,'lxml')

#pretul si denumirea
denumire1=[]
pret1=[]
vector1=[]

preturi=soup.find_all('h3',class_='css-okktvh-Text eu5v0x0')
for course in preturi:
    pret1.append(course.text)

denumiri=soup.find_all('h1',class_='css-r9zjja-Text eu5v0x0')
for course in denumiri:
    den=course.text
    denumire1.append(den)

i=0
for ceva in denumiri:
    vector1.append("Denumirea produsului este " +denumire1[i]+" cu pretul de "+pret1[i])
    if  vector1[i]:
        print(vector1[i])
        i+=1
print('\n\n\n')

print('1.Detalii produs\n2.Descrierea produsului\n3.Numele vanzatorului\n4.De cand este vanatorul pe olx?\n5.Este online vanzatorul?\n6.Iesire din meniu\n')
print('Alege o functionalitate:')
ok=0
while(ok==0):
    input_c = input()
    input_d=int(input_c)

    #detalii produs
    if(input_d==1):
        print('Detaliile produsului:')
        detalii=soup.find_all('p',class_='css-xl6fe0-Text eu5v0x0')
        for course in detalii:
            print(course.text)

    #descrierea produsului
    elif(input_d==2):
        print('Descrierea produsului este: ')
        descriere=soup.find_all('div',class_='css-g5mtbi-Text')
        for course in descriere:
            print(course.text)



    #nume vanzator
    elif(input_d==3):
        print('Numele vanzatorului este: ')
        vanzator=soup.find_all('h4',class_='css-1rbjef7-Text eu5v0x0')
        for course in vanzator:
            print(course.text)
    #de cand este utilizatorul pe olx?
    elif(input_d==4):
        print('Data de cand este utilizatorul inscris pe aplicatie:')
        data=soup.find_all('div',class_='css-1we7nzp-Text eu5v0x0')
        for course in data:
            print(course.text)

    #e online ?
    elif(input_d==5):
        print('Este disponibil vanzatorul?')

        online=soup.find_all('div',class_='css-1bafgv4-Text eu5v0x0')

        for course in online:
            print(course.text)
    #iesire din meniu1
    elif(input_d==6):
        ok+=1
    else:
        print('!!ERROR!!\nNumarul citit de la tastatura nu se regaseste in optiuni..')





