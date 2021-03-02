import requests
from bs4 import BeautifulSoup

def arrange(unscrambled, scrambled):
    a = sorted(unscrambled)
    b = sorted(scrambled)
    a_string = "".join(a)
    b_string = "".join(b)
    if a_string == b_string:
        return True
    else:
        return False

cookies = {"HackThisSite": "38aj1dqbj36mr6uv5cuitth3q1"}	
url = "https://www.hackthissite.org/missions/prog/1/"
r = requests.get(url, cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')

list_tags = soup.find_all('li')
word_list = []
for item in list_tags[-10:]:
    word_list.append(item.string)   #scrambled words stored in word_list   

print(word_list)

unscrambled = []
with open("wordlist.txt", "r") as reader:   
    line = reader.readline()
    while line:
        unscrambled.append(line)
        line = reader.readline()      

unscrambled_new = []
for i in unscrambled:
    unscrambled_new.append(i.strip())

solutions = []

for word in word_list:
    index = 0
    solution = arrange(unscrambled_new[index], word)
    while solution == False:
        index += 1
        solution = arrange(unscrambled_new[index], word)        
    if solution:
        solutions.append(unscrambled_new[index])                #unscrambled words stored in solutions

string = ", ".join(solutions)

payload = {"solution": string}
headers = {
    "Host": "www.hackthissite.org",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.hackthissite.org/missions/prog/2/index.php",
    "Connection": "keep-alive",
    "Cookie": "HackThisSite=38aj1dqbj36mr6uv5cuitth3q1",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Origin": "https://www.hackthissite.org",
}

post_url = "https://www.hackthissite.org/missions/prog/1/index.php"
r2 = requests.post(post_url, headers=headers, data=payload, cookies=cookies)
#soup2 = BeautifulSoup(r2.text, 'html.parser')

#print(soup2.body.prettify())