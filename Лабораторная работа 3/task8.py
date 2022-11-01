money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
all_month = range(0, 12)
spend_all = spend + spend * increase
all_capital = money_capital + salary

month = 0

for i in all_month:
    spend_all = spend_all + spend_all * increase
    all_capital = all_capital + salary - spend_all
    if all_capital - spend_all > 0:
        month += 1
print(month)