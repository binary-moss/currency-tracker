import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_rates(rates):
    print("==============================")
    print("   КУРС ВАЛЮТ (USD/EUR/CNY)")
    print("==============================\n")

    target_currencies = ["USD", "EUR", "CNY"]

    for code in target_currencies:
        if code in rates:
            valute = rates[code]

            valute_name = valute['Name']
            valute_rate = valute['Value']
            valute_prev = valute['Previous']

            diff = round(valute_rate - valute_prev, 2)

            print(f"{valute_name} ({code}): {valute_rate:.2f} руб. (изменение: {diff:+0.2f})")

def conversion_options():
    print("\nВыберите направление конвертации:")
    print("1. Рубли (RUB) -> Иностранная валюта (USD/EUR/CNY)")
    print("2. Иностранная валюта (USD/EUR/CNY) -> Рубли (RUB)")

    return input("\nВаш выбор (1-2): ")

def choose_currency():
    choice = input("\nВведите код валюты (USD/EUR/CNY): ").strip().upper()
    return choice
