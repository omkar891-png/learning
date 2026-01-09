from datetime import datetime
from datetime import date

import pandas as pd 
import numpy as np 
print("Welcome to the yadav tour and travel")
set_price = 1000
start_time = 21
end_time = 22

current_hour = datetime.now().hour
while start_time<= current_hour<end_time:
    name = []
    age =  []
    price =[]
    type = []
    date_registration = []
    time_registration = []


    n = int(input("enter the number of the people :- "))
    
    if n > 0 :
        for i in range(n) :
            is_type = int (input ("press 1 :- student \n press 2 :- senior citizen \n press 3 :- normal \n"))
            if is_type == 1 :
                nm = input ("enter the name :- ")
                ag = int (input("enter the age :-"))
                p = set_price * 50/100
                dt = date.today()
                tm = datetime.now().time()
                name.append(nm)
                age.append(ag)
                price.append(p)
                type.append("student")
                date_registration.append(dt)
                time_registration.append(tm)
            elif is_type == 2 :
                nm = input ("enter the name :- ")
                ag = int (input("enter the age :-"))
                p = set_price * 75/100
                dt = date.today()
                tm = datetime.now().time()
                name.append(nm)
                age.append(ag)
                price.append(p)
                type.append("senior citizen")
                date_registration.append(dt)
                time_registration.append(tm)
            elif is_type == 3 :
                nm = input ("enter the name :- ")
                ag = int (input("enter the age :-"))
                p = set_price
                dt = date.today()
                tm = datetime.now().time()
                name.append(nm)
                age.append(ag)
                price.append(p)
                type.append("normal")
                date_registration.append(dt)
                time_registration.append(tm)
            else :
                print("invalid input")
        print("\n Ticket summary :- ")
        print(name)
        print(age)
        print(price)
    data_frame  = {
        "Names": name,
        "Ages": age,
        "Prices": price,
        "Types": type,
        "Date of Registration": date_registration,
        "Time of Registration": time_registration
    }

df = pd.DataFrame(data_frame)



    





