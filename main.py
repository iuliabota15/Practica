from bs4 import BeautifulSoup
import requests

text=requests.get('https://www.olx.ro/').text
soup=BeautifulSoup(text,'lxml')

#pretul si denumirea
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

print("Anunturile sunt // denumire si pret:")
i=0
for ceva in denumiri:
    vector.append(denumire[i]+" are pretul de "+pret[i])
    if  vector[i]:
     print(vector[i])
     i+=1

print('\n\n\n')



#categorii principale
print("Categoriile principale sunt:")
categorii=soup.find_all('div',class_='item')
for course in categorii:
    cat=course.text.replace('\n','')
    cat2=cat.replace('\t','')
    print(cat2)
    print(',')

print('\n\n\n')
#functionalitati
print("Functionalitatile sunt:")
anunturi=soup.find_all('li',class_='block')
for course in anunturi:
    func=course.text.replace('\n','')
    print(func)
    print(',')


print('\n\n\n')
#link urile catre produse
print('Link-urile catre produse sunt:')
categorii=soup.find_all('div',class_='item')
for course in categorii:
    cat=course.a
    cat2=cat.get('href')
    print(cat2)

