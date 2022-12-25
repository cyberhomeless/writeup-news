import requests
from bs4 import BeautifulSoup
import re
import os

# cat medium.html | grep -i 'div' | grep -i 'href' | grep -i '@' | sed 's/href=/\n\n/' | grep -i '@' | sed 's/>//' | sed 's/"//' | sed 's/"//' | sed 's/?/ /' | cut -d ' ' -f 1 | sort | uniq | grep -Ei '(/@[a-z0-9].*/)'

def getNews():

    os.system("echo 'Y3VybCBYR0VUIC1zIGh0dHBzOi8vcGVudGVzdGVyLmxhbmQvbGlzdC1vZi1idWctYm91bnR5LXdyaXRldXBzLmh0bWwgfCBncmVwICd0ZCcgfCBncmVwICc8YScgfCBzZWQgJ3MvaHJlZj0vXG5cbi8nIHwgc2VkICdzLz4vXG5cbi8nIHwgZ3JlcCAtaSAnaHR0cHMnIHwgZ3JlcCAtRXYgJyh0d2l0dGVyfGZhY2Vib29rfDxhfDxcL2EpJyB8IHNlZCAncy8iLy8nIHwgc2VkICdzLyIvLyc=' | base64 -d | bash >> trash.txt")
    inurl = 'https://infosecwriteups.com/tagged/bug-bounty'
    reqs = requests.get(inurl)
    soup = BeautifulSoup(reqs.text, 'lxml')
    for tag in soup.findAll('a', href=True):
        s = tag['href']
        os.system("echo '" + s + "' | grep -v 'https://medium.com' | grep -i 'infosec' | grep '?source=-' | grep -v '@' | grep -v 'com?' | grep -v 'medium.com' | sed 's/?/ /' | cut -d ' ' -f 1 >> infosec.txt")
    os.system("echo 'Y2F0IGluZm9zZWMudHh0IHwgc29ydCB8IHVuaXE=' | base64 -d  | bash >> trash.txt")
    os.remove("infosec.txt")
    
    medurl = 'https://medium.com/tag/bug-bounty/latest'
    press = requests.get(medurl).text
    source = BeautifulSoup(press, 'html.parser').prettify()
    m = re.findall(r'(/@[a-z0-9].*/.*\?)', source)
    filDump = (list(set(m)))
    for i in filDump:        
        i = i.replace('?', '')
        ns = "https://medium.com" + str(i)
        r = requests.get(ns, allow_redirects=True)
        os.system("echo '" + r.url + "' >> trash.txt")
getNews()

def excploit_db():
    url = 'https://www.exploit-db.com/?draw=2&columns%5B0%5D%5Bdata%5D=date_published&columns%5B0%5D%5Bname%5D=date_published&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=download&columns%5B1%5D%5Bname%5D=download&columns%5B1%5D%5Bsearchable%5D=false&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=application_md5&columns%5B2%5D%5Bname%5D=application_md5&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=verified&columns%5B3%5D%5Bname%5D=verified&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=description&columns%5B4%5D%5Bname%5D=description&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=type_id&columns%5B5%5D%5Bname%5D=type_id&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=platform_id&columns%5B6%5D%5Bname%5D=platform_id&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=author_id&columns%5B7%5D%5Bname%5D=author_id&columns%5B7%5D%5Bsearchable%5D=false&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=code&columns%5B8%5D%5Bname%5D=code.code&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=id&columns%5B9%5D%5Bname%5D=id&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=true&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=9&order%5B0%5D%5Bdir%5D=desc&start=0&length=15&search%5Bvalue%5D=&search%5Bregex%5D=false&author=&port=&type=&tag=&platform=&_=1671953653316'
    s = requests.Session()
    # proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
    headers = {"Host":"www.exploit-db.com",
        "Sec-Ch-Ua":'(Not(A:Brand";v="99", "Chromium";v="108", "Google Chrome";v="108"',
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "X-Requested-With":"XMLHttpRequest",
        "Sec-Ch-Ua-Mobile":"?0",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5371.152 Safari/537.36",
        "Sec-Ch-Ua-Platform":'"macOS"',
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Dest":"empty",
        "Referer":"https://www.exploit-db.com/",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"en-US,en;q=0.9"
    }
    r = s.get(url, headers=headers).text

    v = re.findall(r'(\"description\":[^\s]+)', r)
    for b in v:
        l = re.sub(r'\"description\":\[', '', b)
        o = l.split(",")[0]
        m = re.sub(r'\"', '', o)
        os.system("echo https://www.exploit-db.com/exploits/" + m + " >> trash.txt")
excploit_db()

def addDB():

    db = open("db.txt", 'r')
    db = db.readlines()
    trash  = open("trash.txt", 'r')
    trash = trash.readlines()
    RemDup = (list(set(trash)))
    for i in RemDup:
        if i not in db:
            i = i.strip()
            req = requests.get('https://api.telegram.org/bot5383715273:AAFUNmpfX84OjHIVpoBLXkPnRmGdAZELjZI/sendMessage?chat_id=-1001592949320&text='+str(i))            
            print(i)
            os.system("echo '" + i + "' >> db.txt")
    os.remove("trash.txt")
        
addDB()