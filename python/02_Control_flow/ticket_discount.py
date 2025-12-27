import pandas as pd
from datetime import datetime
start_time = 21
end_time = 22


for i in range(500000):

    current_hour = datetime.now().hour
    if not (start_time <= current_hour < end_time):
        print("Ticket booking is allowed only between 6 AM to 6 PM.")
        break


    names = []
    ages = []
    prices = []

    n = int(input("Enter the number of people: "))

    for j in range(n):   # inner loop for people
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        is_student = input("Are you a student ? (yes/no): ").strip().lower()

        price = 1000

        if age < 12:
            price = price / 2
        elif 12 <= age < 18 and is_student == "yes":
            price = price * 3 / 4
        elif age >= 65:
            price = price / 2

        names.append(name)
        ages.append(age)
        prices.append(price)

    print("\nTicket Summary:")
    print(names)
    print(ages)
    print(prices)

    df = pd.DataFrame({
        "Names": names,
        "Ages": ages,
        "Prices": prices
    })

    print(df)
    print("Total Price :- ", df["Prices"].sum())
