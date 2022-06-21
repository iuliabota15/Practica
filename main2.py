from bs4 import BeautifulSoup
import requests

text=requests.get('https://www.olx.ro/d/oferta/nissan-qasqai-an-2012-2-litridiesel-150cp-tractiune-4x4-4x2-la-buton-IDfE7Hm.html').text
soup=BeautifulSoup(text,'lxml')
#alte anunturi ale vanzatorului
denumire_=[]
pret_=[]
vector_=[]
print('Vanzatorul mai vinde si:')
#<p class="css-1v0u9e8-Text eu5v0x0"><span>8 700 €</span></p>
denumiri_=soup.find_all('p',class_='css-1v0u9e8-Text eu5v0x0')
for course in denumiri_:
    denumire_.append(course.span.text)
    print(course.span.text)
    print('e')
