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