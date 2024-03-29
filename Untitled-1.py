rent = int(input("enter rent per month:"))

loan = int(input("enter loan repayment per month:"))

childcare = int(input("enter childcare per month:"))

total_outgoings = rent + loan + childcare

print (f"the total outgoings for the month is £{total_outgoings}")

monthly_wage = int(input("enter wage per month:"))

amount_remaining = monthly_wage - total_outgoings

print(f"the amount remaining for the month is £{amount_remaining}")