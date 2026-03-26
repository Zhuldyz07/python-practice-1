#variant-D Café Bill Zhuldyz Smagul BDA-2506
# a) Input & Variables
customer_name = input("Enter customer name: ")
item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1 (KZT): "))
item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2 (KZT): "))
people = int(input("Enter number of people: "))

# b) Calculations
subtotal = item1_price + item2_price
tip = subtotal * 0.10
total = subtotal + tip
per_person = total / people

# c) Formatted Output
print("=" * 30)
print("          CAFE BILL")
print("=" * 30)
print("Customer : "+ customer_name)
print(item1_name + " : " + str(item1_price) + " KZT")
print(item2_name + " : " + str(item2_price) + " KZT")
print("-" * 30)
print("Subtotal : " + str(subtotal) + " KZT")
print("Tip (10%) : " + str(tip) + " KZT")
print("Total : " + str(total) + " KZT")
print("Per people : " + str(per_person) + " KZT")
print("=" * 30)

# d) Comparison
print("Tip included: ", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
