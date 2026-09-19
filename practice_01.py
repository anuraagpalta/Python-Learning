#Exercise 1
customer_name = "Raashiya Ltd"
customer_id = 888
monthly_bill = 8000
payment_method = "Direct Debit"
contract_length = 24

#Exercise 2
print(f"{customer_name} with {customer_id} has a monthly bill of {monthly_bill} and pays via {payment_method} and has a contract length of {contract_length} months")

#Exercise 4
annual_bill = (monthly_bill*12)
vat = 0.10
discount = 0.20

total_bill = ((1-discount)*annual_bill+annual_bill*vat)

print(f"The total bill is : {total_bill}")

#Exercise 5
myself = {
"name" : "Anuraag Palta",
"age" : 32,
"job" : "Analytics professional",
"company" : "EXL",
"years_experience" : 10

}

print(f"{myself}")

#Level 2

#Exercise 6
electricity_usage = 100000
gas_usage = 100000
standing_charge = 0.20
monthly_cost = ((standing_charge*30) +(electricity_usage+gas_usage)*0.20)
print(monthly_cost)

#Exercise 7
customer = 10
average_bill = 100
annual_revenue = (customer*average_bill*12)
print(annual_revenue)

#Exercise 8
a=100
b=200

temp = a
a=b
b=temp
print(a)
print(b)

#Exercise 9
customers = ["Anuraag","Arshiya","Babita","Anuradha","Muneer"]
print(f"My customers are : {customers}")

#Exercise 10
customer_1 = {
"name" : "Anuraag Palta",
"age" : 32,
}

#Exercise 11
customer_2 = {
"name" : "Arshiya Vij",
"bills" : [100,200,300,400],
"address" : "18, 3 Palmer Street, Reading",
"smart_meter" : "Yes",
"segment" : "SME"
}
print(f"{customer_2}")

#Exercise 12
customers = [
{
 "name" : "Anuraag",
 "bills" : [
    {"month" : "jan", "bill" : 200},
    {"month" : "feb", "bill" : 300},
    {"month" : "mar", "bill" : 400}
 ]
 },
{
 "name" : "Arshiya",
 "bills" : [100,200,300,400]
 },
{
 "name" : "Babita",
 "bills" : [100,200,300,400]
 },
{
 "name" : "Anuradha",
 "bills" : [100,200,300,400]
 },
{
 "name" : "Muneer",
 "bills" : [100,200,300,400]
 }
]

#Exercise 13
#Anuraag's Mar bill
anuraag_mar_bill = customers[0]["bills"][2]["bill"]
print(anuraag_mar_bill)

#Exercise 14
#Muneer's 4th bill
fourth_customers_bill = customers[3]["bills"][3]
print (fourth_customers_bill)

