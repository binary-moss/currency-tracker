from api import fetch_rates
from converter import convert_currency_to_rub, convert_rub_to_currency
from ui import show_rates, choose_currency, clear_screen, conversion_options

rates = fetch_rates()

while True:
    clear_screen()
    show_rates(rates)
    direction = conversion_options()
    currency_code = choose_currency()
    currency = rates[currency_code]
    rate = currency["Value"]
    amount = float(input("\nВведите сумму: "))

    if direction == "1":
        result = convert_rub_to_currency(amount, rate)

        print(
            f"\n{amount:.2f} RUB = "
            f"{result:.2f} {currency_code}"
        )

    elif direction == "2":
        result = convert_currency_to_rub(amount, rate)

        print(
            f"\n{amount:.2f} {currency_code} = "
            f"{result:.2f} RUB"
        )

    else:
        print("\nНеверный выбор направления.")

    input("\nНажмите Enter, чтобы продолжить...")
