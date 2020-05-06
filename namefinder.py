import requests as req
import os

List = []
locate = 0

def read():
    #finds path of wordlist
    script_dir = os.path.dirname(__file__)
    rel_path = "words.txt"
    path = os.path.join(script_dir, rel_path)

    with open(path, 'r') as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1] #Removes newline char "\n"
                List.append(line)
            else:
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
        write(List[locate-1])
    else:
        print("NOT AVAILABLE")

    print("")

def write(word):
    #finds path of output
    script_dir = os.path.dirname(__file__)
    rel_path = "output.txt"
    path = os.path.join(script_dir, rel_path)

    with open(path, 'a') as file:
        file.write(word + '\n')

def main():
    read()
    for i in range(len(List)):
        find()

if __name__ == "__main__":
    main()