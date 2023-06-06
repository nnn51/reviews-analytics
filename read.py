data = []
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

new = []
for d in data:  # 每個d是一則留言，data是裝著一百萬筆留言的清單
	if len(d) < 100:
		new.append(d)
	# 如果d的長度小於100，就把d裝進new這個新清單中
print('一共有', len(new), '筆留言長度小於100')	

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '則留言包含good')			


# 文字計數

wc = {}  # word count
for d in data:  # d 是每筆留言
	words = d.split()   #每筆留言以空白鍵分割成清單
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1	

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('請輸入想查詢的字:')		
	if word == 'q':
		break
	if word in wc:	
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒有出現過喔')

print('感謝使用本查詢功能')



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
 