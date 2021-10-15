"""
理想的function應該"只做一件事"，
所以refactor(重構程式)的核心概念，
就是把程式碼不斷地改寫，寫成越來越小的function，
讓funtion"盡量"只做一件事。

"""
# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 跳到下一回
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

# 使用者輸入
def user_input(products):
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
	return products

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #字串以 + 合併為1個大字串 
			                                  # csv檔以逗點區隔


def main():
	import os # operationg system -- 像是電腦的政府
	
	filename = 'products.csv'									
	if os.path.isfile(filename):
		print('yeah!,找到檔案了!')
		products = read_file(filename)
	else:
		print('找不到檔案.....')
		
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()