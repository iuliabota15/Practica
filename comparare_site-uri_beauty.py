from bs4 import BeautifulSoup
import requests

print('Introduceti numele produsului pe care il cautati')
produs=input()
produs_replaced=produs.replace(" ","+")
vector=[]
i=0
for ceva in range(30):
    vector.append(produs_replaced[i])
    i+=1
link_douglas='https://www.douglas.ro/search?sSearch='
i=0
for ceva in range(30):
    link_douglas=link_douglas+vector[i]
    i+=1
print("Link-ul catre produs pe site-ul Douglas este: ",link_douglas)

link_notino='https://www.notino.ro/search.asp?exps='+produs.replace(" ","%20")
print("Link-ul catre produs pe site-ul Notino este: ",link_notino)

text=requests.get(link_notino).text
soup=BeautifulSoup(text,'lxml')
pret=soup.find('p',class_='price')
vector1=[]
for course in pret:
    a=course.text
    a=a.split()[2]
    vector1.append(a)

vector2=[]
text=requests.get(link_douglas).text
soup=BeautifulSoup(text,'lxml')
pret2=soup.find('span',class_='price--default is--nowrap is--discount')
for course in pret2:
    a=course.text
    a.replace("\n","")
    a=a.split(" ")[0]
    a=a.split(",")[0]
    vector2.append(a)
print("Pretul produsului pe site-ul Notino: ")
print(vector1[0])
vector2[0]=vector2[0].replace("\n","")
print("Pretul produsului pe site-ul Douglas: ")
print(vector2[0])
if(int(vector1[0])<int(vector2[0])):
    print("Pretul pentru produs este mai ieftin pe site ul Notino ~ ",vector1[0])
elif(int(vector1[0])==int(vector2[0])):
    print("Pretul pentru produs este acelasi pentru ambele site-uri ~ ",vector1[0])
else:
    print("Pretul pentru produs este mai ieftin pe site ul Douglas ~ ",vector2[0])