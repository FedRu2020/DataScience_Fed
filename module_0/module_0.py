# -*- coding: utf-8 -*-

import numpy as np

def game_core_v3(number):
    '''First set random number as predict and then call binary_search function.
      Function to get guess number and return amount of attempts '''
    count = 1
    predict = np.random.randint(1,101)
    count=binary_search(number,predict)
                   
    return(count) # loop exit, when guessed

def binary_search(number, predict):
    '''Binary search of coincident between predict and guess numbers. Gues number doesn't change.
       Function to get guess and predict numbers and returns amount of attempts'''
    high = 100
    count = 1
    
    while abs(number-predict) > 3: # 3 is the last high number after 5th loop
        high = high // 2 #slicing numbers of loops
        count += 1
        if abs(number-predict) > high:
            if number > predict:
                predict += high
            elif number < predict:
                predict -= high
    else:
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1 
            
    return(count) # loop exit, when guessed            

def score_game(game_core):
    '''Launch the game 1000 times to know how fast the game can find guess number'''
    count_ls = []
    np.random.seed(1)  # fixing RANDOM SEED to reproduce your test!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    
    return(score)
    
    
score_game(game_core_v3) #Launching the game 1000 times