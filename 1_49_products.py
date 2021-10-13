"""
1. import os (作業系統模組)
2. 使用os.path.isfile()來檢查檔案在不在

"""
"""
1. 增加讀取檔案程式碼
2. 用.split(',')來用逗點做分割 
3. 用.strip()來除掉換行符號(\n)
4. 加上encoding='utf-8'來讀取
5. 解釋split完會變清單
6. 把讀到的內容裝進清單

"""
"""
1. continue教學
2. 重點整理，解釋continue通常都是寫在迴圈中很高的位置
3. 建立版本上傳GitHub

"""

import os # operationg system -- 像是電腦的政府

products = []
products1 = []

if os.path.isfile('products.csv'):
	print('yeah!,找到檔案了!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳到下一回
			name, price = line.strip().split(',')
			products.append([name, price])

			s = line.strip().split(',')
			products1.append(s)
else:
	print('找不到檔案.....')

print(products)
print(products1)

"""

1. GitHub建立專案
2. 基本程式碼
3. 二維清單介紹
4. 寫進程式碼
5. 練習存取二維清單
6. 建立版本上傳
7. for loop搞清楚每個東西是甚麼
8. 建立版本上傳
""" 
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	p = [name, price]
    #p.append(name)
    #p.append(price) # 不知道為何無法用append
	products.append(p) # products.append([name, price])
print(products)

print(products[0][0])

# 讀取每一筆資料
for p in products:
	print(p[0], '的價格是', p[1])

"""
1. 字串可以做 + 跟 *
2. 寫到檔案的程式碼
3. 改成存csv格式
4. with解釋複習t

"""
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #字串以 + 合併為1個大字串 
		                                  # csv檔以逗點區隔

