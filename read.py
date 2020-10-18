data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count %1000 == 0:
		    print(len(data))


sum_len = 0
for d in data:
 	sum_len = sum_len + len (d)
 	print(sum_len)
print('檔案讀取完了，總共有',len(data),'資料')
print('留言的平均長度是', sum_len/len(data))

#篩選
new =[]
for d in data:
#for loop 的意思就是把data內的一個一個拿出來
    if len(d) < 100:
    	new.append(d)
print ('一共有', len(new), '筆留言長度小於100')
#前面沒空格，不在for內，才不會一直print)
print(new[0])

good = []
for d in data:
    if 'good' in d:
    	good.append(d)
print('一共有 ', len(good), '筆留言提到good')
print(good[0])
