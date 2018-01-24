import pyautogui as pg
import time

points = 0

answer= pg.prompt(
"""
Which would you rather do?

a)Go to Jail for life
b)Tell everyone you are the Flash

"""

)

pg.alert("you chose " + answer)

if answer == "a" or answer == "A":
    points += 1
elif answer == "b" or answer == "B":
    points += 5

  
