import requests
import json
import time
class GetCurrency():
    def __init__(self,currency):
        self.currency = currency
    def get_url(self):
        url = requests.get(f'https://api.exchangeratesapi.io/latest?base={self.currency}')
        if url.status_code == 200:
            return url.json()
        else:
            return None
        
    def compare_rates(self,find_currency):
        time1 = time.monotonic()
        print(f'Comparing {self.currency} and {find_currency}....')
        url = self.get_url()
        if url != None:
               try:
                    rate = url['rates'][find_currency]            
                    time2 = time.monotonic()
                    return f'${time2 - time1} One {self.currency} is equal to {round(rate,2)} {find_currency}'
                    
               except Exception:
                   return f'The currency you want to compare with {self.currency} could not be found'
        else:
            return 'The currency you entered doesn\'t exist'               
                

        
    def get_all_rates(self):
        url = self.get_url()
        if url != None:
            print(('Getting all currencies...'))
            for currency,rate in url['rates'].items():
                print(time2 - time1)
                print( f"One {self.currency} is equal to {round(rate,2)} {currency}")
                print(time2 - time1)
USD = GetCurrency('USD')

print(USD.compare_rates('INR'))
