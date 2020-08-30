# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup




def get_restaurant(word):
    URL="https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query={word}"
    result=requests.get(URL)
    soup=BeautifulSoup(result.text, "html.parser")
    restaurants=soup.find("div", {"class": "list_area"}).find_all("a", {"class":"name"})
    lst=[]
    for i in restaurants:
        name=''
        link=''
        name=i["title"]
        link=i["href"]
        lst.append({"name": name, "link": link})
    
    return lst
get_restaurant("중국집")
        


