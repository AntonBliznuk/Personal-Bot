import requests
from bs4 import BeautifulSoup

def hryvnia():
    # Define cookies for the request
    cookies = {
        'HSID': 'AWiYvpZAAAFKBH7Wo',
        'SSID': 'AO9b2F41SXsdhAr2H',
        'APISID': 'D2_KYMpHqf0lgvS1/A397bhMOvJ8vGrlk4',
        'SAPISID': 'LB4VeBeTYxDvgidJ/ARl-M3KsMhw_zwWn_',
        '__Secure-1PAPISID': 'LB4VeBeTYxDvgidJ/ARl-M3KsMhw_zwWn_',
        '__Secure-3PAPISID': 'LB4VeBeTYxDvgidJ/ARl-M3KsMhw_zwWn_',
        'SID': 'g.a000lQjTgpy3lPAwNQ2yg3fmi1cnEkp1NnJaX9tKVw89As5-ptT-03p8rFqc1XK6RSDZdgzRqgACgYKATQSARISFQHGX2Mi_6i4JQ59Mdg9LIQPntLGcBoVAUF8yKrEV8ZUzqDqpuJLElZhpoQw0076',
        '__Secure-1PSID': 'g.a000lQjTgpy3lPAwNQ2yg3fmi1cnEkp1NnJaX9tKVw89As5-ptT--HZXmz8IMSmz3B7MTqEx5gACgYKAVESARISFQHGX2MiEmttWdkRJ6YOxRSLl616fBoVAUF8yKroYvjHMiLdOUmV_mPG5PC00076',
        '__Secure-3PSID': 'g.a000lQjTgpy3lPAwNQ2yg3fmi1cnEkp1NnJaX9tKVw89As5-ptT-gBAxygl73IiuAkcJayX43gACgYKAdYSARISFQHGX2MioEjjzYASj4pNiuVE6tTT9RoVAUF8yKo_TDHadxg4fGQ_RA44sKVQ0076',
        'AEC': 'AVYB7cpXhgIQkgg9rGBadW2HIPcL6oiGc6g8crsh9tmzKmQe0OQDi9hPAg',
        'NID': '515=qoIbIZyDyTJV5RA_o4vorqdp3ApwLDnHyoa_HAPmJjlU-pA-8ZhR1cgH2s7RmJs06Vk12XOyr9j_vm_9OWJhMg7JgnTE1Kj5dWWPN3kV_C6LE0CqC_hDK7ow-ayi-Dd0eHG9qJHm6C4ztjiUM7tms1QHHoER5HIUIF1pUOZPzW7HptyXYsAj-YJVlNFBBVWEk7oPe8Q2mPHK_3QBXEDXoo-m9WDVtiQ7iAFTXOKcohGHY3qpMThna47V7Jo0CSK3o0WZz0Vc0J03ysKCHyH0t-OtPkLAF8oaN38ctte0Q2tbZ7l6WuK2hYL-5JAMl5JwIoU39l-dg0Wy3uUlWkBHtoj_dQW6DQTIxM6P4pUcIi9k-0WSwRt1OPystZSEqR7QTboRIUBNxSpz0xugoDF-pcqvjCoVAdg',
        'SEARCH_SAMESITE': 'CgQIy5sB',
        'DV': 'E0icvrStCcCNACJ-bZgLX559rKc3CplHdzweT9XjKQIAACAcuD9TMkTrkAAAAPA12Tp0snLFTwAAAGy871Dv-DMjFgAAgBajok77cqidlKACELt8hEqnbj1SJagAKIWroCxOgwacCSoA',
        '__Secure-ENID': '20.SE=jV1MadxRMP1PPvA_dywg5elqXjS01OBTMpjzAZdhISLAI3fhRPZGptmtvZJIn__295zI759yygcELBFT-5STyk5MB99TrItLFr1kFIh7ZzvMYH_SZq2sK3dksEvqq8he7MtjeCNod0QT0FQ7_qa7sW-6e_b5crEfLWLzqqiBYpPFWhR0bO2QzXhmNvJ2SEXQ1KgoTS_RzDCEttcR4UL57yxKKXUst3xv4mo-sBW6c4o0KEHj-NhLnGIYd1g3HxkKgJFmkwkjyT7jXorBxr9IhfcES87mJxbjqnujOJB9cDvVWR9xxVQV1qYhD1iIT8DXKCngylYPZBncUzigYaUs5_UbQseHyANc0bhYNGWAS2nH-L3HSU4pRyDpo9PBTwEy_Fw',
        '__Secure-1PSIDTS': 'sidts-CjEB4E2dkXlRNjh9zuJY7ovQ_sWMZ1kTD-0Af6g6jNiwRODpWmnSsS_Qrj-TiITsSlvVEAA',
        '__Secure-3PSIDTS': 'sidts-CjEB4E2dkXlRNjh9zuJY7ovQ_sWMZ1kTD-0Af6g6jNiwRODpWmnSsS_Qrj-TiITsSlvVEAA',
        'SIDCC': 'AKEyXzXOGcibighFa_wHXSSKQkrVyTe7ZD7rEnCPcp_xeyG_Tz7NfW-ioLNncY73mRHeXg5egQ',
        '__Secure-1PSIDCC': 'AKEyXzVmdjMzFWuOchDXW2ubnCIBCTUHDmmhpTb6lp0Qzbk0D98YAw2Hz1ZarHcEgO0jTkyql_0',
        '__Secure-3PSIDCC': 'AKEyXzURiRRam60FOMRjJYP9ftIoCgDqmghlv-LGtLbZomhVhRkeMPMUEbxBx8ar9N01AJsdOQ',
    }

    # Define headers for the request
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '...';  # Cookies are provided separately above
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-arch': '"arm"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"126.0.6478.127"',
        'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"macOS"',
        'sec-ch-ua-platform-version': '"14.5.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-client-data': 'CIm2yQEIpLbJAQipncoBCMrqygEIk6HLAQj7mM0BCIagzQEIw4XOAQiSh84BCLOXzgEIsZ7OAQinos4BCOOnzgEImqjOAQj9qs4BCISszgEInqzOARihnc4B',
    }

    # Define query parameters for the request
    params = {
        'q': 'долар к гривне',  # Search query: "dollar to hryvnia"
        'oq': 'ljkfh r uh',     # Query (part of the original query that is not used)
        'gs_lcrp': 'EgZjaHJvbWUqCQgBEAAYChiABDIGCAAQRRg5MgkIARAAGAoYgAQyCQgCEAAYChiABDIICAMQABgWGB4yCAgEEAAYFhge0gEINDE4N2owajeoAgCwAgA',
        'sourceid': 'chrome',
        'ie': 'UTF-8',
    }

    # Send the GET request to Google Search
    response = requests.get('https://www.google.com/search', params=params, cookies=cookies, headers=headers)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'lxml')

    # Extract and return the exchange rate value
    return float(soup.find('span', class_='DFlfde SwHCTb').text.replace(',', '.'))

def main():
    print(hryvnia())  # Print the current exchange rate

if __name__ == '__main__':
    main()
