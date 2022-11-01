salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

all_spends = spend

for i in range(2, months + 1):
    spend = spend * 1.03
    all_spends = all_spends + spend

print(round(all_spends - salary * months))
