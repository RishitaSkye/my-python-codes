def func(price):
    if (price>250):
        return True
    else:
        return False
price=[250,360,4,547,56,650]
new_price=filter(func,price)  #filter() is a func which checks and filter all the elements
print(list(new_price))
