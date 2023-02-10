import time
import os
i = 0

def  test():
	global i
	
	while i <= 50:
		#time.sleep(0.5)
		i += 1
		print(i)
		time.sleep(1)
		os.system('clear') 
		if i == 50:
			print('test end')



while i <= 100:
	test()
	i += 1
	time.sleep(0.5)
	print(i)
