'''find the highest and lowest price from 10 products'''
list1 = []
list2 = []
num = print("Enter the number of products")

for x in range(10):
    print("Enter the product name : ")
    pro = input()
    list1.append(pro)
    
    pri = float(input("Enter the price of the product(Rs) :"))
    list2.append(pri)
print("--------------------------------------")

product = tuple(list1)
price = tuple(list2)
print("product name : ",product,"product price in Rs",price)
print("--------------------------------------")
# print(price)
print("highest product price :",max(price))
print("lowest product price :",min(price))
