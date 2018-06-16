# user_name = input("Enter your name:")
# print("Hello, {name}".format(name=user_name))

principal = -1
while principal < 0:
    try:
        principal=float(input("Enter Loan Amount:"))
    except ValueError:
        print("Invalid Loan Amount")
        principal = -1

interest=12.99
periods=4
n_years=2
print(f"Entered:{principal}")
final_cost = principal * (1+interest/100.0/periods)**n_years

print("{cost:0.02f}".format(cost=final_cost))
print("Total Interest Paid: {interest:0.02f}".format(interest=final_cost-principal))
print("Monthly Payments: {payment:0.02f}".format(payment=final_cost/24))