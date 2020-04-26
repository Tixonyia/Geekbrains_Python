from sys import argv

script_name, production, rate, prize = argv


def salary(production_def, rate_def, prize_def):
    try:
        float(production_def), float(rate_def), float(prize_def)
        if float(production_def) >= 0 and float(rate_def) >= 0:
            if float(prize_def) > 0:
                result = float(production_def) * float(rate_def) + float(prize_def)
                return f"ЗП = {result}"
            elif float(prize_def) == 0:
                result = float(production_def) * float(rate_def)
                return f"Накосячил, премии не получил. ЗП = {result}"
            elif float(prize_def) < 0:
                result = float(production_def) * float(rate_def) + float(prize_def)
                return f"Штрафанули... ЗП = {result}"
            elif float(production_def) == 0 or float(rate_def) == 0:
                return "Не работал - не получил ЗП."
        else:
            return "Время и ставка не может быть меньше нуля."
    except:
        return "Введите числовые значения."


print(salary(production, rate, prize))
