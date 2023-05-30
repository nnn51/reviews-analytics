data = []
word = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1      # count = count + 1
		    # %用來求餘數，例如 7 % 3 = 1    15 % 5 = 0
			

		for w in line:          # 每則留言是line，留言中的每個字設定為w
			word.append(w)	    # 把每個字w ，加入word清單
			
print('檔案讀取完成，總共有', len(data), '筆資料')
word_avg = len(word)  / len(data)   # word清單:所有留言的字，data清單:所有留言
print('平均留言長度為', word_avg)

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
