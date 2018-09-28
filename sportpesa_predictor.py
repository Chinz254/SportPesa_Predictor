import random
import re
import sys
import csv

def xxx():
    def bounty_hunter():
        jackpot = []
        n = 0
        while n <= 12:
            def game_predictor():
                rng = random.Random()
                number = rng.randrange(1,4)
    
                if number == 1:
                    return "X"
                elif number == 2:
                    return "1"
                else:
                    return "2"
    
            predicted_no = game_predictor()
            jackpot += predicted_no
            n += 1
        return jackpot
    jp = bounty_hunter()
    
    
    draws = jp.count('X')
    home_wins = jp.count('1')
    away_wins = jp.count('2')
    
    def check_req():
        if draws <= 5 and draws >= 3 and home_wins >=2 and  home_wins <= 8 and away_wins <= 8 and away_wins >= 2:
            return True
        else:
            return False
    status = check_req()
    return status, jp, draws, home_wins, away_wins
    
def display_res():
    yn = xxx()
    checked = yn[0]
    result = yn[1]
    d = yn[2]
    h = yn[3]
    a = yn[4]
    
    return checked, "{} Draw(s), {} Home Win(s), {} Away Win(s)".format(d,h,a), result

         
def yyy():
    yx = xxx()
    count = 0
    for n in range(200):
        display_res()
        predictions = display_res()
        y = predictions[0]
        x = predictions[2]
        if y:
            print(x)
            count += 1
            with open('jackpotn11.csv','w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(x)          
    print(count)
yyy()

        
"""
def sortqualified():
    p = yyy()
    print(p)
    for n in str(p):
        if p[0] == 'F':
            print(n)

"""       

    
    
    #print(jp)
    #3 <= draws <= 5 and home_wins <= 8 and away_wins <= 8
#3 > draws > 5 and homewins > 8 and away_wins > 8:
#print("{} Draw(s), {} Home Win(s), {} Away Win(s)".format(draws, home_wins, away_wins))
#print(jp)        
