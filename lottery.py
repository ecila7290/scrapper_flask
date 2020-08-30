from random import randint
import time




def create_numbers():
    numbers=list(range(1,46))
    choice=[]
    
    for _ in range(7):
        num=randint(0,len(numbers)-1)
        choice.append(numbers[num])
        numbers.pop(num)
    choice.sort()
    #print("Your numbers are ",end='')

    return choice
        
        
    #print("\r")
    #print("Good luck!")


def to_win(num):
    
    choice=num
    choice.sort()
    
    cnt=0
    money=0
    #print("This will take some time.. please wait")
    while True:
        atari=[]
        numbers=list(range(1,46))
        for _ in range(7):
            num=randint(0,len(numbers)-1)
            atari.append(numbers[num])
            numbers.pop(num)
        
        #atari_bonus=atari[-1]
        atari.pop(-1)
        atari.sort()
        
        set_choice=set(choice)
        set_atari=set(atari)
        difference=set_choice - set_atari
        if len(difference)==1:
            choice.pop(choice.index(list(difference)[0]))
        
        cnt+=1
        money+=1000
        
        print(f"\rBuying {cnt} lotteries", end='')
        if choice==atari:
            print('\r')
            #print("You have to spend " + "{:,}".format(money) + " Won to win!")
            
            return cnt
            
        else:
            continue
    
    
'''        
while True:
    print("What do you want to play?")
    print("1. prediction")
    print("2. how much you have to buy to win")

    n=int(input("I want to play: "))
    if n==1:
        create_numbers()
        
        m=int(input("Want to play again? (1=Yes 2=No): "))
        if m==1:
            create_numbers()
        elif m==2:
            print("Bye!")
            break
        else:
            print("======input 1 or 2 only======")
    elif n==2:
        to_win()
        m=int(input("Want to play again? (1=Yes 2=No): "))
        if m==1:
            to_win()
        elif m==2:
            print("Bye!")
            break
        else:
            print("======input 1 or 2 only======")
    else:
        print("======input 1 or 2 only======")
'''