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

products = []
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

for p in products:
	print(p[0], '的價格是', p[1])

"""
1. 字串可以做 + 跟 *
2. 寫到檔案的程式碼
3. 改成存csv格式
4. with解釋複習t

"""
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #字串以 + 合併為1個大字串 
		                                  # csv檔以逗點區隔
		                                  
