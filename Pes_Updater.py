import requests
from bs4 import BeautifulSoup
from itertools import count

id = input("Bir id giriniz: ")
id_sorgu = requests.get('https://pesdb.net/pes2022/?id={0}'.format(id))
sonuc = BeautifulSoup(id_sorgu.content,"lxml")

isim = sonuc.find("th", text="Player Name:").next_sibling.text
yas = sonuc.find("th", text="Age:").next_sibling.text
takim = sonuc.find("th", text="Team Name:").next_sibling.text
no = sonuc.find("th", text="Squad Number:").next_sibling.text
boy = sonuc.find("th", text="Height:").next_sibling.text
kilo = sonuc.find("th", text="Weight:").next_sibling.text

oyuncu = [id, isim, yas, takim, no, boy, kilo]

for i in count():
    if i == 26:
        break
    else:
        oyuncu.append(sonuc.find('td', id='a{0}'.format(i)).text)
        #ozellik = sonuc.find('td', id='a{0}'.format(i)).text
        print(oyuncu)

"""isim = sonuc.xpath('//*[@id="table_0"]/tbody/tr[1]/td[1]/table/tbody/tr[1]/td')
yas = sonuc.xpath('//*[@id="table_0"]/tbody/tr[1]/td[1]/table/tbody/tr[9]/td')
#takim = sonuc.find("#table_0 > tbody > tr:nth-child(1) > td:nth-child(1) > table > tbody > tr:nth-child(3) > td > a").text()
no = sonuc.xpath('//*[@id="table_0"]/tbody/tr[1]/td[1]/table/tbody/tr[2]/td')

print(yas)"""
        
"""sven_harita = (svencoop.find("div",attrs={"id":"HTML_curr_map"}).text).strip()
        
cs_harita = (cs16.find("div",attrs={"id":"HTML_curr_map"}).text).strip()
cs_oyuncu_sayisi = (cs16.find("span",attrs={"id":"HTML_num_players"}).text).strip()
cs_durum = (cs16.find("a",attrs={"href":"/server_info/159.146.61.231:27015/manage/"}).text).strip()"""