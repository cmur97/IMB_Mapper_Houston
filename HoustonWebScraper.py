import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# Scraped data will be added to these dictionaries
names = []
phone_numbers = []
addresses = []

# Page range
pages = range(1, 51)

# Loop through each page
for num in pages:

    page = requests.get("https://www.rubmaps.ch/houston-massage-parlors-tx-" + str(num) + "#rubmaps")
    soup = BeautifulSoup(page.text, 'html.parser')
    IMB_address_list = soup.find_all('div', class_='rows')

    for container in IMB_address_list:
        name = container.find('a', class_='th-a').text
        names.append(name)

        phone_num = container.find('i', class_='phonenumberrow').text
        phone_numbers.append(phone_num)

        address = container.br.next_element.strip()
        full_address = address + " Houston, TX"
        addresses.append(full_address)

# Create a Pandas DataFrame populated with relevant info
IMB_List = pd.DataFrame({
    'Name': names,
    'Phone Numbers': phone_numbers,
    'Address': addresses
})

# Save to .csv file
IMB_List.to_csv('IMB_list_Houston.csv', index=False)

# Only addresses for map
only_addresses = IMB_List['Address']
only_addresses.to_csv('IMB_Addresses.csv', index=False)

# Find duplicates of phone numbers and addresses 

# Phone Numbers
def getDuplicatesWithCount(phone_numbers):
    dictofElems = dict()
    for elem in phone_numbers:
        if elem in dictofElems:
            dictofElems[elem] += 1
        else:
            dictofElems[elem] = 1

    dictofElems = {key: value for key, value in dictofElems.items() if value > 1}
    return dictofElems


dictofElems = getDuplicatesWithCount(phone_numbers)
for key, value in dictofElems.items():
    print(key, ' :: ', value)

# Addresses
def getDuplicatesWithCount(addresses):
    dictofElems = dict()
    for elem in addresses:
        if elem in dictofElems:
            dictofElems[elem] += 1
        else:
            dictofElems[elem] = 1

    dictofElems = {key: value for key, value in dictofElems.items() if value > 1}
    return dictofElems


dictofElems = getDuplicatesWithCount(addresses)
for key, value in dictofElems.items():
    print(key, ' :: ', value)










