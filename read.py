data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1   # count = count + 1
		if count % 10000 ==0:     # % 求餘數 若count=1001 餘數=1
			print(len(data))	
print(len(data))
print(data[0])
print('----------------------------------------')
num = input('請輸入想查看的評論編號:')
num = int(num)	
print(data[num-1])	