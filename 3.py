x = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
print('сколько выходных дней вы хотите')
amount = int(input())
weekends = x[-amount:]
workday = x[:len(x) - amount]
print("Ваши выходные дни: ", *weekends, "\nВаши рабочие дни: ", *workday)