import pyautogui as p
import time
import random

print()
print()
print('**************************************************************************')
print('A Script By Gautham Kanagraj')
print('**************************************************************************')
print()
print()
timers = int(input('Enter the duration for which you want to move your mouse in minutes '))
counts = 0
width, height = p.size()
while counts <= timers*60:
	x = random.randint(0, width)
	y = random.randint(0, height)
	p.moveTo(x, y, duration=1)
	time.sleep(1)
	counts += 2
