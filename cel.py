from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt

text=requests.get('https://www.cel.ro/laptop-laptopuri/?gclid=Cj0KCQjw2MWVBhCQARIsAIjbwoO5glxWzjX6-0WZ0YNF_xvazUToALwtlFGH2kljl_vY-_PU8S0Os1kaAiyeEALw_wcB').text
soup=BeautifulSoup(text,'lxml')

denumire=[]
pret=[]
vector=[]
pret_float=[]
preturi=soup.find_all('span',class_='price')
for course in preturi:
    pret.append(course.text)
    pret_float.append(float(course.text))
denumiri=soup.find_all('h2',class_='productTitle')
for course in denumiri:
    denumire.append(course.text)

print("Anunturile sunt // denumire si pret:")
i=0
for ceva in denumiri:
    vector.append(denumire[i]+" are pretul de "+pret[i]+" lei")
    if  vector[i]:
     print(vector[i])
     i+=1

print('\n\n\n')
#sortare crescatoare
pret_float.sort()
print('Preturile sortate crescator: ',pret_float)
print('\n\n\n')
#sortare descrescatoare
pret_float.sort(reverse=True)
print('Preturile sortate descrescator: ',pret_float)

print('\n\n\n')
#denumiri dupa pretul crescator
denumiresorted = [x for _,x in sorted(zip(pret,denumire))]
print(denumiresorted)

#sortare descrescatoare completa //cu msj
print('\n\n\n')
vector_sorted=[]
i=0
nr=0
for ceva in denumiresorted:
    vector_sorted.append(denumiresorted[i]+" are pretul de "+str(pret_float[i])+" lei")
    if  vector_sorted[i]:
     print(vector_sorted[i])
     i+=1
     nr+=1


#grafic primele 7 cele mai scumpe laptop-uri
print('\n\n\n')
dev_x=[]
dev_y=[]
for i in range(7):
    dev_y.append(pret_float[i])
    dev_x.append(i+1)
plt.plot(dev_x,dev_y)
plt.xlabel('Contor')
plt.ylabel('Pret')
plt.title('Top 7 cele mai scumpe Laptop-uri')
plt.show()

#grafic primele 5 cele mai ieftine laptop-uri
print('\n\n\n')
dev_x=[]
dev_y=[]
for i in range(5):
    dev_y.append(pret_float[nr-i-1])
    dev_x.append(i+1)
plt.plot(dev_x,dev_y)
plt.xlabel('Contor')
plt.ylabel('Pret')
plt.title('Top 5 cele mai ieftine Laptop-uri')
plt.show()


#comparare 10 laptop-uri scumpe vs 10 ieftine
dev_x=[]
dev_y=[]
for i in range(10):
    dev_y.append(pret_float[i])
    dev_x.append(i+1)
plt.plot(dev_x,dev_y)

dev_x=[]
dev_y=[]
for i in range(10):
    dev_y.append(pret_float[nr-i-1])
    dev_x.append(i+1)
plt.plot(dev_x,dev_y)
plt.xlabel('Contor')
plt.ylabel('Pret')
plt.title('Top 10 cele mai scumpe vs top 10 cele mai ieftine Laptop-uri')
plt.show()
