#variant-D Café Bill Zhuldyz Smagul BDA-2506
# D1)
customer_name = input("Enter customer name: ")
subtotal = 0.0
item_count = 0
item_name = input("Enter item name (or 'done' to finish): ")

while item_name != 'done':
    price = float(input("Enter price: "))
    subtotal += price
    item_count = item_count + 1
    item_name = input("Enter item name (or 'done' to finish): ")

print("Customer :" + customer_name.upper())
print("Item :"+ str(item_count))
print("Subtotal :"+ str(subtotal) + " KZT")

# D2)
hour = int(input("Enter current hour(0-23): "))
print("-"*30)

if hour>=6 and hour<12:
    discount = subtotal * 0.10
    discounted = subtotal - discount
    tip = discounted * 0.10
    total = discounted + tip
    print("Time period : Morning discount")
    print("Discount : " + str(discount)+ " KZT")
    print("Tip : " + str(tip)+ " KZT")
    print("Total : " + str(total) + " KZT")
elif hour>=12 and hour<17:
    discount = 0.0
    tip = subtotal * 0.10
    total = subtotal + tip
    print("Time period : No discount")
    print("Discount : " + str(discount)+ " KZT")
    print("Tip : " + str(tip)+ " KZT")
    print("Total : " + str(total) + " KZT")
elif hour>=17 and hour<22:
    discount = subtotal * 0.05
    discounted = subtotal - discount
    tip = discounted * 0.10
    total = discounted + tip
    print("Time period : Evening discount")
    print("Discount : " + str(discount)+ " KZT")
    print("Tip : " + str(tip)+ " KZT")
    print("Total : " + str(total) + " KZT")
else:
    print("Closed")
print("-"*30)

#D3
print("Name uppercase: ", customer_name.upper())
print("Name lowercase: ", customer_name.lower())
print("Name length: ", str(len(customer_name)))

if customer_name[0].upper() == "A" or customer_name[0].upper() == "S" :
    print("VIP customer")
else:
    print("Regular customer")
