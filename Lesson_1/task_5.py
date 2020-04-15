profit = float(input("Введите значение прибыли: "))
costs = float(input("Введите значение издержек: "))
if profit == costs:
    print("Вышли в ноль.")
elif profit < costs:
    print("Ушли в минус.")
else:
    print("Мы в плюсе.")
    profitability = profit / costs
    print(f"Рентабельность составляет: {profitability:.2f}")
    slaves = int(input("А сколько нас?: "))
    profitability_on_man = (profit - costs) / slaves
    print(f"Ура! По {profitability_on_man:.2f} каждому!")