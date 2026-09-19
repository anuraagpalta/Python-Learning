#Level 1
x = 5
y = x

name = "Anuraag"
city = name

bill = 100
bill = 150

active = True
customer_active = active

#Level 2
numbers = [10, 20]
copy = numbers

copy.append(30)

print(numbers)
print(copy)

a = "Reading"
b = a

a = "London"

print(a)
print(b)

#Level 3
customer1 = {
    "name": "John",
    "bills": [100, 200]
}

customer2 = customer1

customer2["bills"].append(300)

print(customer1)