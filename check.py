import requests
from bs4 import BeautifulSoup


def get_number():
    url="https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1"

    result=requests.get(url)
    soup=BeautifulSoup(result.text, 'html.parser')
    numbers=soup.find("div", {"class": "win"}).find("p").get_text().strip('\n')
    numbers=numbers.replace('\n', ' ')
    win_num=[]
    num=''
    
    for i in range(len(numbers)):
        
        if numbers[i]!= ' ':
            num+=numbers[i]
            
        else:
            
            win_num.append(int(num))
            num=''
    win_num.append(int(num))
    return win_num

def get_bonus():
    url="https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1"

    result=requests.get(url)
    soup=BeautifulSoup(result.text, 'html.parser')
    bonus=soup.find("div", {"class": "bonus"}).find("p").get_text().strip('\n')

    return int(bonus)


def get_date():
    url="https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1"

    result=requests.get(url)
    soup=BeautifulSoup(result.text, 'html.parser')
    date=soup.find("div", {"class": "win_result"}).find("p").get_text()
    return date

def get_rank(my_num):
    win_num=get_number()
    bonus_num=get_bonus()
    win_num.append(bonus_num)
    all_num=win_num

    difference=set(all_num)-set(my_num)
    difference=len(list(difference))
    if difference==0 :
        return 1
    elif ((bonus_num not in my_num) and difference==1):
        return 1
    elif bonus_num in my_num and difference==1:
        return 2
    elif difference==2:
        return 3
    elif difference==3:
        return 4
    elif difference==4:
        return 5
    else:
        return '꼴'
    
def get_money():
    url="https://www.dhlottery.co.kr/gameResult.do?method=byWin&wiselog=C_A_1_1"

    result=requests.get(url)
    soup=BeautifulSoup(result.text, 'html.parser')

    money_list=[]
    for p in soup.find("tbody").find_all("td", {"class": "tar"}):
        if p.find(class_="color_key1"):
            continue
        else:
            money_list.append(p.get_text())
    
    return money_list



    

