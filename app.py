# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
from lottery import create_numbers, to_win
from check import get_number, get_bonus, get_date, get_money, get_rank
from menu import get_restaurant
import time
from random import randint

app = Flask(__name__) 

db={}


@app.route('/') 
def home(): 
    return render_template("index.html")

@app.route('/report')
def report():
    keyword=request.args.get('keyword')
    if keyword:
        keyword=keyword.lower()
        existingJobs=db.get(keyword)
        if existingJobs:
            jobs=existingJobs
        else:
            jobs=get_jobs(keyword)
            db[keyword]=jobs
    else:
        return redirect('/')
    return render_template("report.html", searchingBy=keyword, resultsNumber=len(jobs), jobs=jobs)

@app.route('/lottery_num')
def lottery_num():
    amount=request.args.get('amount')
    amount=int(amount)
    numbers=[]
    for _ in range(amount):
        result=create_numbers()
        result=[str(intg) for intg in result]
        result='  '.join(result)
        numbers.append(result)

    return render_template("lottery_num.html", numbers=numbers)


@app.route('/lottery_to_win')
def lottery_to_win():
    
    choice = request.args.getlist('input_num', type=int)
    choice.sort()
    choice_new=choice
    choice_new=[str(intg) for intg in choice_new]
    choice_new=' '.join(choice_new)
    
    result = to_win(choice)


    return render_template("lottery_to_win.html", choice=choice_new, cnt=result)

@app.route('/lottery_check')
def lottery_check():
    your_num = request.args.getlist('input_num', type=int)
    your_num.sort()

    win_num=get_number()
    win_num=[str(intg) for intg in win_num]
    win_num=' '.join(win_num)

    bonus_num=get_bonus()

    date=get_date()

    rank=get_rank(your_num)

    money_list=get_money()
    
    if rank==1:
        money=money_list[0]
    elif rank==2:
        money=money_list[1]
    elif rank==3:
        money=money_list[2]
    elif rank==4:
        money=money_list[3]
    elif rank==5:
        money=money_list[4]
    else:
        money='0원'

    
    your_num=[str(intg) for intg in your_num]
    your_num=' '.join(your_num)
    
    return render_template("lottery_check.html", your_num=your_num, win_num=win_num, bonus_num=bonus_num, date=date, rank=rank, money=money)

@app.route('/menu')
def lunch_menu():
    menu_list=["닭갈비", "쌈밥", "비빔밥", "생선구이", "게장", "떡갈비", "김치찌개", "순두부찌개", "된장찌개", "부대찌개", "동태찌개", "갈비탕", "삼계탕", "중국집", "짜장면", "짬뽕", "탕수육", "마파두부", "고추잡채", "초밥", "라멘", "덮밥", "우동", "돈까스", "스파게티", "스테이크", "피자", "햄버거", "콩나물국밥", "순대국", "해장국", "감자탕", "냉면", "서브웨이", "김밥", "떡볶이", "쌀국수", "인도카레", "칼국수", "닭갈비", "월남쌈"]
    rand=randint(0,40)
    rst_info=get_restaurant(menu_list[rand])
    return render_template("menu.html", info=rst_info)

if __name__ == '__main__':
    app.run()
    