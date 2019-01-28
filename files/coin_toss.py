from random import random
d = int(input("Please enter the distance between lines (in mm):"))
r = int(input("Please enter the “reward” if the customer wins (in $):"))

win = 0

for i in range(1000): # loop 1000 times
	#find the coordinate (x,y) of the center of the coin
	x = d*random() #a random number between 0 and r
	y = d*random() #a random number between 0 and r
	if(x - 14 > 0 and x + 14 < d and y - 14 > 0 and y + 14 < d):
		#14 is the radius of the coin
		win = win + 1

gain = 1000 * 2 - win * 4
if(gain >= 0):
	print("For the simulation of 1000 toonie tosses, you get $%d"%(gain))
else:
	print("For the simulation of 1000 toonie tosses, you lose $%d"%(-gain))

#For the discussion question
#The good option for the owner is when
#2000 - (r - 2)* ((d - 28)/d)^2 > 0