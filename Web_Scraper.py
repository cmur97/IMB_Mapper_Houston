import requests
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import pandas as pd
import selenium

names = []
phone_numbers = []
addresses = []



def get_info_NYC():
    pages = np.arange(1, 15, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/new-york-city-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)

def get_info_Manhattan_below14th():
    pages = np.arange(1, 9, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/manhattan-below-14th-st-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)


def get_info_Manhattan_14th40th():
    pages = np.arange(1, 18, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/manhattan-14th-to-40th-street-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)


def get_info_Manhattan_40th72nd():
    pages = np.arange(1, 15, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/manhattan-40th-to-72nd-street-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)

def get_info_Manhattan_72ndAbove():
    pages = np.arange(1, 6, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/manhattan-72nd-street-and-above-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)


def get_info_Brooklyn():
    pages = np.arange(1, 21, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/brooklyn-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)





def get_info_Queens():
    pages = np.arange(1, 4, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/queens-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)


def get_info_Flushing():
    pages = np.arange(1, 17, 1)

    for page in pages:
        page = requests.get("https://www.rubmaps.ch/flushing-massage-parlors-ny" + "-" + str(page) + "#rubmaps")
        soup = BeautifulSoup(page.text, 'html.parser')
        IMB_Address_List = soup.find_all('div', class_='main-row')

        for container in IMB_Address_List:
            name = container.find('a', class_='th-a').text
            names.append(name)

            phone_number = container.i.text
            phone_numbers.append(phone_number)

            address1 = container.br
            address2 = address1.next_element
            address = address2.strip()

            addresses.append(address)

get_info_NYC()
get_info_Queens()
get_info_Brooklyn()
get_info_Flushing()
get_info_Manhattan_14th40th()
get_info_Manhattan_40th72nd()
get_info_Manhattan_72ndAbove()
get_info_Manhattan_below14th()


IMB_List = pd.DataFrame({
    'Name of IMB': names,
    'Phone Number': phone_numbers,
    'Address': addresses
})

print(IMB_List)
IMB_List.to_csv("IMB_LIST_NYC.csv", index=False)


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
