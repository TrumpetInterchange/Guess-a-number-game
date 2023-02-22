"""
A module for checking if user input is valid and comparing it with ANSWER
"""
from random import randint
ANSWER = randint(1,500)


def inputCheck(response:str):
    """
    Checks if the user input is fail safe. 
    Must use input() before using it.

    Args:
        response: the user input from input()
    
    Returns:
        0: When TypeError was raised or response is out of range(1,500)
        guess: the response given but now it's an integer
    """
    try:
        guess = int(response) #input() returns it in str
    except:
        return 0
    if guess < 501 and guess > 0:
        return guess
    else:
        return 0

def rangeCheck(guess:int):
    """
    Compares guess with ANSWER

    Args:
        guess: the user guess. Should be validated using inputCheck() before

    Returns:
        0: guess is greater than ANSWER. 
        1: guess is lower than ANSWER
        2: guess is the ANSWER
    """
    if guess > ANSWER:
        return 0
    elif guess < ANSWER:
        return 1
    elif guess == ANSWER:
        return 2