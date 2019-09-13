from random import randint
j = 0
while True:
	j+=1
	result =[]
	input('ROLL')
	for i in range (6):
		result.append(randint(1,6))
	print(result)
	if result.count(4)>=4:
		print('ZhuangYuan. You have rolled %d times.' %j) 
		quit()
	else:
		for i in (1,2,3,5,6):
			if result.count(i)>=5:
				print('ZhuangYuan. You have rolled %d times.' %j) 
				quit()
