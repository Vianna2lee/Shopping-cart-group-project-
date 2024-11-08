def how_to_pay():
    while True:
        try:
            choose=int(input("Enter 1 if you want to pay with Visa. Enter 2 if you want to pay with Mastercard : "))
            if choose!=1 or choose !=2:
                raise TypeError
        except TypeError:
            print("Please enter only 1 or 2 :")
        else:
            if choose==1:
                print("You chose to pay with Visa")
            else:
                print("You chose to pay with Mastercard ")
        break

        
def currency_dict():
    currency={
        "USD": 1,
        "AED": 3.67,
        "AFN": 67.06,
        "ALL": 90.62,
        "AMD": 387.6,
        "ANG": 1.79,
        "AOA": 924.4,
        "ARS": 990.75,
        "AUD": 1.52,
        "AWG": 1.79,
        "AZN": 1.7,
        "BAM": 1.8,
        "BBD": 2,
        "BDT": 119.47,
        "BGN": 1.8,
        "BHD": 0.376,
        "BIF": 2911.79,
        "BMD": 1,
        "BND": 1.32,
        "BOB": 6.92,
        "BRL": 5.76,
        "BSD": 1,
        "BTN": 84.11,
        "BWP": 13.39,
        "BYN": 3.29,
        "BZD": 2,
        "CAD": 1.39,
        "CDF": 2843.47,
        "CHF": 0.864,
        "CLP": 962.04,
        "CNY": 7.12,
        "COP": 4420.36,
        "CRC": 512.59,
        "CUP": 24,
        "CVE": 101.4,
        "CZK": 23.29,
        "DJF": 177.72,
        "DKK": 6.86,
        "DOP": 60.23,
        "DZD": 133.41,
        "EGP": 48.94,
        "ERN": 15,
        "ETB": 121.27,
        "EUR": 0.92,
        "FJD": 2.24,
        "FKP": 0.774,
        "FOK": 6.86,
        "GBP": 0.774,
        "GEL": 2.74,
        "GGP": 0.774,
        "GHS": 16.52,
        "GIP": 0.774,
        "GMD": 71.55,
        "GNF": 8671.71,
        "GTQ": 7.73,
        "GYD": 209.38,
        "HKD": 7.77,
        "HNL": 25.21,
        "HRK": 6.93,
        "HTG": 131.7,
        "HUF": 375.52,
        "IDR": 15696.52,
        "ILS": 3.73,
        "IMP": 0.774,
        "INR": 84.11,
        "IQD": 1310.95,
        "IRR": 42100.55,
        "ISK": 136.98,
        "JEP": 0.774,
        "JMD": 158.11,
        "JOD": 0.709,
        "JPY": 152.16,
        "KES": 128.9,
        "KGS": 85.49,
        "KHR": 4079.33,
        "KID": 1.52,
        "KMF": 452.41,
        "KRW": 1376.21,
        "KWD": 0.307,
        "KYD": 0.833,
        "KZT": 488.23,
        "LAK": 21923.8,
        "LBP": 89500,
        "LKR": 292.85,
        "LRD": 192,
        "LSL": 17.62,
        "LYD": 4.83,
        "MAD": 9.85,
        "MDL": 17.92,
        "MGA": 4585.81,
        "MKD": 56.9,
        "MMK": 2099.66,
        "MNT": 3430.42,
        "MOP": 8.01,
        "MRU": 39.92,
        "MUR": 46.03,
        "MVR": 15.46,
        "MWK": 1741.4,
        "MXN": 20.04,
        "MYR": 4.38,
        "MZN": 63.96,
        "NAD": 17.62,
        "NGN": 1645.14,
        "NIO": 36.8,
        "NOK": 11,
        "NPR": 134.58,
        "NZD": 1.67,
        "OMR": 0.384,
        "PAB": 1,
        "PEN": 3.77,
        "PGK": 3.99,
        "PHP": 58.27,
        "PKR": 277.92,
        "PLN": 4,
        "PYG": 7924.9,
        "QAR": 3.64,
        "RON": 4.58,
        "RSD": 107.75,
        "RUB": 97.25,
        "RWF": 1370.45,
        "SAR": 3.75,
        "SBD": 8.36,
        "SCR": 13.9,
        "SDG": 512.78,
        "SEK": 10.67,
        "SGD": 1.32,
        "SHP": 0.774,
        "SLE": 22.75,
        "SLL": 22750.89,
        "SOS": 572.13,
        "SRD": 34.77,
        "SSP": 3280.19,
        "STN": 22.53,
        "SYP": 12920.38,
        "SZL": 17.62,
        "THB": 33.78,
        "TJS": 10.64,
        "TMT": 3.5,
        "TND": 3.1,
        "TOP": 2.35,
        "TRY": 34.29,
        "TTD": 6.77,
        "TVD": 1.52,
        "TWD": 31.9,
        "TZS": 2706,
        "UAH": 41.23,
        "UGX": 3660.42,
        "UYU": 41.06,
        "UZS": 12783.52,
        "VES": 42.71,
        "VND": 25289.35,
        "VUV": 120.74,
        "WST": 2.76,
        "XAF": 603.22,
        "XCD": 2.7,
        "XDR": 0.75,
        "XOF": 603.22,
        "XPF": 109.74,
        "YER": 250.2,
        "ZAR": 17.62,
        "ZMW": 26.72,
        "ZWL": 28.68,
    }
    return currency



def choose_currency(chosen_currency,currency,):
    while True:
        try:
            chosen_currency=input("Choose the currency you want to pay with ")
            chosen_currency=chosen_currency.upper()
            if chosen_currency not in currency:
                raise TypeError
        except TypeError:
            print("Please only type in the currency in the list")
        else:
            break
    return chosen_currency


def currency_exchange(chosen_currency,total_price,currency_dict):
    
    FP = float(total_price)* currency_dict[chosen_currency]
    FP = round(FP,3)
    print(f"your total price is {FP} {chosen_currency}")

    return FP # price for all in desire currrency
        

