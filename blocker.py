import time
from datetime import datetime as dt

# path_host=r"C:\Windows\System32\drivers\etc\hosts"
temp_path='hosts'
redirect="127.0.0.1"
blocking_website_list=["twitter.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,18):
        with open(temp_path,'r+') as file:
            content=file.read()
            for website in blocking_website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(temp_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocking_website_list):
                    file.write(line)
            file.truncate()
        
        