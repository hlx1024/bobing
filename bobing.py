from random import randint
j = 0
def check(result):
	for i in (1,2,3,5,6):
		if result.count(i)>=5:
			return 'ZhuangYuan'
		if result.count(i)==4:
			return 'SiJin'
	if result == [1,2,3,4,5,6]:
		return 'DuiTang'
	num4 = result.count(4)
	if num4 >= 4:
		return 'ZhuangYuan'
	if num4 == 3:
		return 'SanHong'		
	if num4 == 2:
		return 'ErJu'
	if num4 == 1:
		return 'YiXiu'
	return 'None'
while True:
	j+=1
	result =[]
	input('ROLL')
	for i in range (6):
		result.append(randint(1,6))
	print(result, end ='')
	re = check(result)
	print('  '+re)
	if re == 'ZhuangYuan':
		print('Congratulations. You have rolled %d times to get ZhuangYuan.' %j) 
		quit()
