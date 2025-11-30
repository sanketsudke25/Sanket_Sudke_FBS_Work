exchange_rates = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.5,
    "GBP": 0.78,
    "JPY": 150.2
}

def currency_converter():
    print("=== Currency Converter ===")
    
    amount = float(input("Enter amount: "))
    from_currency = input("Enter input currency (USD, EUR, INR, GBP, JPY): ").upper()
    to_currency = input("Enter output currency (USD, EUR, INR, GBP, JPY): ").upper()
    
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print(" Invalid currency selection!")
        return
    
    usd_amount = amount / exchange_rates[from_currency]   
    converted_amount = usd_amount * exchange_rates[to_currency]
    
    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
currency_converter()