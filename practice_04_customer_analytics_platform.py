
#Excerise Level 1 Collections
Prog_Langs = ["C","Python","SQL"]

Prog_Langs.insert(4,"R")
Prog_Langs.remove("C")
Prog_Langs.sort()
Prog_Langs.sort(reverse=True)
len(Prog_Langs)
print(Prog_Langs)
print("Python" in Prog_Langs)
Prog_Langs[1] = "PySpark"
print(Prog_Langs)




#Customer Analytics Platform

customers = [
    {
        "customer_id": 101,
        "name": "Anuraag",
        "city": "Ludhiana",
        "contract": "fixed",
        "smart_meter": True,
        "bills": [
            {"month": "jan", "amount": 200},
            {"month": "feb", "amount": 300},
            {"month": "mar", "amount": 400}
        ],
        "payments": [
            {"month": "jan", "amount": 400},
            {"month": "feb", "amount": 200},
            {"month": "mar", "amount": 100}
        ],
        "meter_read_type": "estimated"
    },
    {
        "customer_id": 102,
        "name": "Sanya",
        "city": "Pune",
        "contract": "vpp",
        "smart_meter": True,
        "bills": [
            {"month": "jan", "amount": 100},
            {"month": "feb", "amount": 500},
            {"month": "mar", "amount": 200}
        ],
        "payments": [
            {"month": "jan", "amount": 200},
            {"month": "feb", "amount": 600},
            {"month": "mar", "amount": 50}
        ],
        "meter_read_type": "actual"
    },
    {
        "customer_id": 103,
        "name": "Arshiya",
        "city": "Gurgaon",
        "contract": "fixed",
        "smart_meter": False,
        "bills": [
            {"month": "jan", "amount": 50},
            {"month": "feb", "amount": 60},
            {"month": "mar", "amount": 80}
        ],
        "payments": [
            {"month": "jan", "amount": 100},
            {"month": "feb", "amount": 20},
            {"month": "mar", "amount": 30}
        ],
        "meter_read_type": "actual"
    },
    {
        "customer_id": 104,
        "name": "Muneer",
        "city": "Gurgaon",
        "contract": "out_of_contract",
        "smart_meter": False,
        "bills": [
            {"month": "jan", "amount": 190},
            {"month": "feb", "amount": 260},
            {"month": "mar", "amount": 80}
        ],
        "payments": [
            {"month": "jan", "amount": 390},
            {"month": "feb", "amount": 120},
            {"month": "mar", "amount": 20}
        ],
        "meter_read_type": "estimated"
    }
]

#Chapter 5 : If else

#Level 1

if customers[0]["smart_meter"] :
    print(f"Smart meter installed ")
else :
    print(f"Smart meter not installed")


if customers[1]["city"] in ["Pune"] :
    print(f"Lives in Pune ")
else :
    print(f"Doesnt live in Pune")

if customers[2]["contract"] in ["fixed"] :
    print(f"{customers[2]['name']} Has fixed contract")
else :
    print(f"Doesnt have fixed contract")


#Level 2

if customers[1]["bills"][1]["amount"] >= 300 :
   bill_status = "Very High"
elif customers[1]["bills"][1]["amount"] >= 150 :
   bill_status = "High"    
elif customers[1]["bills"][1]["amount"] >= 75 :
   bill_status = "medium"    
else : 
    bill_status = "low"

print(bill_status)


if customers[3]["contract"] == "out_of_contract" :
   contract_status = "Retention required"
elif customers[3]["contract"] in (["fixed","vpp"]) :
     contract_status = "active"
else : 
    contract_status = "unkown"       

print(contract_status)


cutomer_1_total_bill = (
    customers[0]["bills"][0]["amount"]+
    customers[0]["bills"][1]["amount"]+
    customers[0]["bills"][2]["amount"]
)

cutomer_1_total_payment = (
    customers[0]["payments"][0]["amount"]+
    customers[0]["payments"][1]["amount"]+
    customers[0]["payments"][2]["amount"]
)

customer_1_total_balance = (cutomer_1_total_bill - cutomer_1_total_payment)


if customer_1_total_balance > 0 :
    print(f"{customers[0]['name']} is in debt")
elif customer_1_total_balance < 0 :
    print(f"{customers[0]['name']} is in credit")
else :
    print(f"{customers[0]['name']} is settled")



#Level 3

#Identify premium digital customers

fixed_vpp_contract_type = customers[0]["contract"] in ["fixed","vpp"]
actual_meter_read = customers[0]["meter_read_type"] in ["actual"]
smart_meter = customers[0]["smart_meter"] 

if (
    fixed_vpp_contract_type and actual_meter_read and smart_meter
) :
    print(f"Premium digital customer")
else :
    print(f"Not premium digital customer")    


#Level 5

#Priority Scoring

if customers[3]["contract"] == "out_of_contract" :
   out_of_contract_score = 3
else : 
   out_of_contract_score = 0

if not customers[3]["smart_meter"] :
   smart_score = 2
else : 
    smart_score = 0

print(smart_score)

if (customers[3]["bills"][0]["amount"] > 250 
    or customers[3]["bills"][1]["amount"] > 250 
    or customers[3]["bills"][2]["amount"] > 250 
    ) :
   bill_score = 2
else : 
   bill_score = 0

print(bill_score)  

criticality_score = (bill_score+smart_score+out_of_contract_score)

print(criticality_score)


#Challenge 3



cutomer_1_total_bill = (
    customers[0]["bills"][0]["amount"]+
    customers[0]["bills"][1]["amount"]+
    customers[0]["bills"][2]["amount"]
)

cutomer_1_total_payment = (
    customers[0]["payments"][0]["amount"]+
    customers[0]["payments"][1]["amount"]+
    customers[0]["payments"][2]["amount"]
)

customer_1_total_balance = (cutomer_1_total_bill - cutomer_1_total_payment)


if customer_1_total_balance > 0 :
    in_debt = True
else :
    in_debt = False 

in_debt

out_of_contract = customers[0]["contract"] == "out_of_contract"
no_smart_meter = not customers[0]["smart_meter"]

if (
    out_of_contract and in_debt 
   ) :
   print(f"urgent_retention_and_debt_support") 
elif (
    out_of_contract and not in_debt 
     ) :
    print(f"retention offer")
elif in_debt :
    print(f"payment support")
elif no_smart_meter :
    print(f"smart meter offer")
else :
    print(f"no action")       


#Chapter 6 : Loops

customer = customers[0]

for customer in customers:
    print(customer["name"])
    
for bill in customer["bills"] :
    print(bill["amount"])


for customer in customers :
    print (customer["name"])
    for bill in customer["bills"] :
        print( bill["amount"])


total = 0

for bill in customer["bills"] :
    total = total + bill["amount"]

print(total)


for customer in customers :
    print (customer["name"])
    total = 0
    for bill in customer["bills"] :
        total = total + bill["amount"]
        print(total)


#Level 1    

#Print everything
for cust in customers :
    print (cust["name"])
    print (cust["city"])
    print (cust["contract"])
    print (cust["meter_read_type"]) 

#Count Number of customers
count = 0

for count in range(len(customers)) :
    count = count + 1

print (count)    


#Level 2

#Print every bill & payment amount
for customer in customers  :
    print(customer["name"])
    for bill in customer["bills"] :
        print (bill["amount"])
    for pay in customer["payments"] :
        print (pay["amount"])

#Calculate total bill and payment for each customer
for customer in customers :
    print (customer["name"])  
    total_bill = 0
    total_payment = 0 
    for bill in customer["bills"] :
        total_bill = total_bill + bill["amount"]
    for pay in customer["payments"] :
        total_payment = total_payment + pay["amount"]
    print(f"Total bill : {total_bill}")
    print(f"Total payment : {total_payment}")
    balance = total_bill - total_payment
    print(f"Total balance : {balance}")
    if balance > 0 :
        print(f"The customer is in debt")
    else :
        print (f"The customer is not in debt")       


#Level 3

#Print with conditions
for cust in customers :
    if cust["smart_meter"] :    
        print(f"{cust["name"]} has a smart meter")
    else : 
        continue

#Print only customers in debt
for customer in customers :
    total_bill = 0
    total_payment = 0 
    for bill in customer["bills"] :
        total_bill = total_bill + bill["amount"]
    for pay in customer["payments"] :
        total_payment = total_payment + pay["amount"]
    balance = total_bill - total_payment
    if balance > 0 :
        print(f"{customer["name"]} is in debt")
    else :
        continue      


#Print premium digital customers
for customer in customers :
    fixed_vpp_contract_type = customer["contract"] in ["fixed","vpp"]
    actual_meter_read = customer["meter_read_type"] in ["actual"]
    smart_meter = customer["smart_meter"] 
    if (
    fixed_vpp_contract_type and actual_meter_read and smart_meter
    ) :
        print(f"{customer["name"]} is a premium digital customer")
    else :
        continue  

#Level 4

##Calculate customer with hightest total bill
highest_total_bill = 0
highest_bill_customer = ""

for customer in customers:
    total_bill = 0

    for bill in customer["bills"]:
        total_bill = total_bill + bill["amount"]

    if total_bill > highest_total_bill:
        highest_total_bill = total_bill
        highest_bill_customer = customer["name"]

print(f"{highest_bill_customer} has the highest total bill: £{highest_total_bill}")
    

##Calculate average bill of all customers
for customer in customers :
    total_bill_amount = 0
    total_bills = 0
    for bill in customer["bills"] :
        total_bill_amount = total_bill_amount + bill["amount"]
        total_bills = total_bills + 1
        average_bill = (total_bill_amount/total_bills)
    print(f"{customer["name"]} has an average bill of : {average_bill}")

##Calculate how many customers have smart meter
smart_meter = 0
for customer in customers :
    if customer["smart_meter"] :
        smart_meter = smart_meter + 1
    else :
        continue
print(smart_meter)


#Chapter 7 : Functions

#Function for total bill
def calculate_total_bill(bills) :
    total_bill = 0
    for bill in bills :
        total_bill= total_bill +bill["amount"]
    return total_bill

customer = customers[0]

Total_1_customer_bill = calculate_total_bill(customer["bills"])
print (Total_1_customer_bill)

for customer in customers :
    total_bill = calculate_total_bill(customer["bills"])
    print(f"{customer["name"]} has a total bill of {total_bill}")

#Function for total paymet
def calculate_total_payment(payments) :
    total_pay = 0
    for pay in payments :
        total_pay= total_pay +pay["amount"]
    return total_pay

customer = customers[0]

Total_1_customer_payment = calculate_total_payment(customer["payments"])
print (Total_1_customer_payment)

for customer in customers :
    total_payment= calculate_total_payment(customer["payments"])
    print(f"{customer["name"]} has a total payment of {total_payment}")

#Function for total balance

def cal_balance(customer) :
    bill = calculate_total_bill(customer["bills"])
    payment = calculate_total_payment(customer["payments"])
    balance = (bill-payment)
    return balance

for customer in customers :
    balance = cal_balance(customer)
    print(f"{customer["name"]} has a balance of : {balance}")


#Level 1

def greet_customer(customer) :
        print (f"Hello {customer["name"]}")

for customer in customers :
    greet_customer(customer)
       
#Calculate annual bill
def calculate_annual_bill(monthly_bill) :
    annual_bill = monthly_bill * 12
    return annual_bill


annual_bill_value = calculate_annual_bill(monthly_bill = 100)
print(annual_bill_value)


#Calculate discount 
def calculate_discount(amount, discount_rate) :
    discount = amount * discount_rate
    return discount

discount_amount = calculate_discount(100,0.20)
print (discount_amount)


#Level 2

#Has smart meter
def has_smart_meter(customer) :
    if customer["smart_meter"] :
        print(f"{customer["name"]} has smart meter")
    else :
        print(f"{customer["name"]} does not have smart meter")    

for customer in customers :
    has_smart_meter(customer) 


#Premimum digital customer

def premium_digital_customer(customer) :
        fixed_vpp_contract_type = customer["contract"] in ["fixed","vpp"]
        actual_meter_read = customer["meter_read_type"] in ["actual"]
        smart_meter = customer["smart_meter"] 
        if (
            fixed_vpp_contract_type and actual_meter_read and smart_meter
        ) :
            print(f"{customer["name"]} is a premium digital customer")
        else :
             print(f"{customer["name"]} is not a premium digital customer")     

for customer in customers :
    premium_digital_customer(customer)

#Level 3

#Calculate total_bills

def calculate_total_bill(bills) :
    total_bill = 0
    for x in bills :
        total_bill = total_bill + x["amount"]
    return total_bill

for customer in customers :
    customer_total_bill = calculate_total_bill(customer["bills"])
    print(f"{customer["name"]} has a total bill of £{customer_total_bill}")

#Challenges

#Highest bill customer

def highest_bill_customer(customer) :
    highest_bill = 0
    name = ""
    for customer in customers :
        customer_total_bill = calculate_total_bill(customer["bills"])

        if customer_total_bill > highest_bill :
            highest_bill =  customer_total_bill
            name = customer["name"]
    return       {
        "highest_bill" : highest_bill,
        "name" : name
    }

highest_bill_dic = highest_bill_customer(customers)
print(highest_bill_dic)

#Find customer by name

def find_customer_by_name(customers, customer_name) :
    for customer in customers :
        if customer_name == customer["name"] :
            print("Customer found")
        break

find_customer_by_name(customers, customer_name = "Mummy")

             
#Get all out of contract customers

def get_out_of_contract_customers(customers) :
    for customer in customers :
        if customer["contract"] == "out_of_contract" :
            print(f"{customer["name"]}")
        else :
            continue

get_out_of_contract_customers(customers)