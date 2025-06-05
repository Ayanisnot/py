def total_calc(bill_amount, tip_perc=10):
    total = bill_amount + 0.01*tip_perc*bill_amount
    total = round(total , 2)
    print(f"please pay ${total}")


total_calc(150)
total_calc(150, 20)