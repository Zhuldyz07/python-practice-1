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
print(f"{'CAFE BILL':^30}")
print("=" * 30)
print(f"Customer : {customer_name}")
print(f"{item1_name} : {item1_price} KZT")
print(f"{item2_name} : {item2_price} KZT")
print("-" * 30)
print(f"Subtotal : {subtotal} KZT")
print(f"Tip (10%) : {tip} KZT")
print(f"Total : {total} KZT")
print(f"Per people : {per_person} KZT")
print("=" * 30)

# d) Comparison
print("Tip included: ", tip > 0)
print("Bill over 5000 KZT:", total > 5000)
