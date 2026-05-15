import requests

response = requests.get("https://open.er-api.com/v6/latest/USD")
data = response.json()
rates = data['rates']

while True:
    print("\n --- Currency Converter ---")
    amount = input("Enter amount (or type 'exit' to quit): ")
    if amount.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        amount = float(amount)
        from_currency = input("Convert from (e.g., USD): ").upper()
        to_currency = input("Convert to (e.g., EUR): ").upper()
        
        if from_currency in rates and to_currency in rates:
            result = amount / rates[from_currency] * rates[to_currency]
            print(f"{amount} {from_currency}: {result:.2f} {to_currency}")
        else:
            print("Currency not found!!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")
    except KeyError:
        print("Invalid Currency code. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")