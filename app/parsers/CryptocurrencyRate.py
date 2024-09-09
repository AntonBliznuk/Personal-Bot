import requests
from bs4 import BeautifulSoup

def crypto_parser(task_list):
    final_dict = {}

    for i in task_list:
        # Send a GET request to the CoinMarketCap page for the given cryptocurrency
        page = requests.get(f"https://coinmarketcap.com/currencies/{i}/")
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(page.text, 'lxml')

        # Find the HTML tag that contains the cryptocurrency price
        price_tag = soup.find('span', class_='sc-65e7f566-0 clvjgF base-text')

        # Extract the price text and convert it to a float value (e.g., "$1,000.00" to 1000.00)
        final_dict[i] = (price_tag.text, float(price_tag.text.replace(',', '').replace('$', '')))

    return final_dict

def main():
    # Call the crypto_parser function with a list of cryptocurrency names
    res = crypto_parser(['bitcoin', 'toncoin', 'ethereum', 'notcoin'])
    # Print the result for each cryptocurrency
    for k, v in res.items():
        print(f'{k}: {v}')

if __name__ == '__main__':
    main()
