import requests as req

def standard_input():
    yield 'winamp'

def url():
    word = input("Enter your name : ") 

    url = 'https://steamcommunity.com/id/'
    url += word

    print(url)

    return(url)

def find():
    sitedata = req.get(url())

    result = sitedata.text.find('The specified profile could not be found.')

    print(f"Found at {result}")

    if(result != -1):
        print("AVAILABLE")
    else:
        print("NOT AVAILABLE")

find()