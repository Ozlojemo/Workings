#Currency converter
def converter (amount, original_currency):
    if original_currency == "usd":
        print(amount*112.5)
    elif original_currency == "EUR":
        print(amount*132.45)
    else: 
        print ("The currency is not usd or eur")
converter(10,"usd") # calling the function and passing in the argument
converter(20,"usd")
converter(10,"EUR")
converter(10,"KES")