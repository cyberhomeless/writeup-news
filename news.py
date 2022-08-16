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