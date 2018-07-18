import datetime

my_weeks = (datetime.datetime.now()+datetime.timedelta(days=7*i) for i in range(10))

for week in my_weeks:
    if input(f"select {week}?").lower().startswith("y"):
        print(f"SELECTED {week}!")
        break
else:
    print("OK no date selected!")



lots_of_space = sum([x*x for x in range(50)])
no_space_used = sum((x*x for x in range(50)))




with open(__file__) as f:
    print(max((len(line) for line in f)))



