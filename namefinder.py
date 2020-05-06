import requests as req
import os

List = []
locate = 0

def read():
    #finds path of wordlist
    script_dir = os.path.dirname(__file__)
    rel_path = "words.txt"
    path = os.path.join(script_dir, rel_path)

    with open(path, 'r') as f:
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

def main():
    read()
    for i in range(len(List)):
        find()

if __name__ == "__main__":
    main()