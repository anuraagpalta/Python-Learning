#Level 1 Strings
my_name = ["Anuraag"]

print(f"{my_name[0]}")

print(my_name[0])

print(my_name[len(my_name)-1])

print(my_name.upper())
print(my_name.lower())
print(len(my_name))

my_name = "Anuraag"
my_name1 = my_name.replace("raag"," palta")
print(my_name1.startswith("A"))
print(my_name1.endswith("a"))

print(f"Hello my name is {my_name1}")

print(id(my_name))
print(id(my_name1))

#Level 2 Numbers
monthly_bill = 100
annual_bill = (monthly_bill*12)
vat = 0.10
discount = 0.24
total_bill = round(((1-discount)*annual_bill+annual_bill*vat),2)
print(total_bill)

bill = [106,109,217,390,110,200,250]
print(max(bill))
print(min(bill))
print(sum(bill))
print(sum(bill)/len(bill))
print(125 % 12)

num1 = "100"
num2 = "200"
print(num1+num2)

#Explains why we need numpy;List is not numberic
bill = [106,109,217,390,110,200,250]
annual_bill = bill*12
print(annual_bill)

print([1,2,3] + [4,5])
print("Data" + "Bricks")
print([1,2] + [3] * 2)
print([10] * 5)



