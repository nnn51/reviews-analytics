data = []
word = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1      # count = count + 1
		if count % 1000 == 0:    # %用來求餘數，例如 7 % 3 = 1    15 % 5 = 0
			print(len(data))
print('檔案讀取完成，總共有', len(data), '筆資料')

sum_len = 0
for d in data:  # d是每一筆留言  len(d) = 每一筆留言的長度
	sum_len = sum_len + len(d)   
	# 求留言的總長度:每一次讀取，把該次留言的長度，加上舊總數，成為新總數

print('留言的平均長度為', sum_len/len(data))


print('----------------------------------------')
print('')
while True:
	num = input('請輸入想查看的留言編號:')
	num = int(num)	
	if num > 0 and num < 1000001:
		num = num - 1
		print(data[num])
		break
	else:
		print('請輸入1-1000000範圍內整數')	
		print('')
		print('')
 