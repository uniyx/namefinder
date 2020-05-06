import requests as req

List = []
locate = 0

def read():
    with open('words.txt', 'r') as f:
        for line in f:
            line = line[:-1] #Removes newline char
            List.append(line)

    print(List)

def url():
    global locate
    url = 'https://steamcommunity.com/id/'
    url += List[locate]

    print(url)
    locate += 1

    return(url)

def find():
    sitedata = req.get(url())

    result = sitedata.text.find('The specified profile could not be found.')

    if(result != -1):
        print("AVAILABLE")
        print(f"Found at {result}")
    else:
        print("NOT AVAILABLE")

    print("")

read()
find()
find()