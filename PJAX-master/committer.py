import schedule
import time
import datetime
import github

import requests
import json
import random


content = requests.get('http://localhost:8080/api')
js = json.loads(content.text)








print(js)
for i in js:
    print(i['username'])
    times = random.randrange(13, 25)
    print(times) 
    g = github.Github(i['pat'])
    print('SIGNED WITH PAT')



    for x in range(times):
        try:
            repo = g.get_user().get_repo(random.choice(i['repos'])['name'])
            print('got REPO')
            print( 'REPO = ',repo)
            try:
                repo.create_file('commit.txt', 'created from pythonanywhere',"We did it !")
                print(repo,' == CREATED')
            except:
                file = repo.get_contents("commit.txt")
                repo.update_file("commit.txt", 'updated from pythonanywhere', f"{datetime.datetime.now()}", sha=file.sha)
                time.sleep(1)
                print(repo,' == UPDATED')
            else:
                pass
            print("====================", ' HayotbekAbdulazizov is done ')
            
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print(f"---------------------------- \n        COULD NOT COMMIT SOMETHING WENT WRONG !!! \n  ---------------------------------------")
            pass







# g = Github("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")
# repo = g.get_user()
# print(repo.get_repo('Repos3'))
# print( 'REPO = ',repo)
# try:
    # repo.create_file('commit.txt', 'created from pythonanywhere',"We did it !")
    # print(repo,' == CREATED')
# except:
    # file = repo.get_contents("commit.txt")
    # repo.update_file("commit.txt", 'updated from pythonanywhere', f"{datetime.datetime.now()}", sha=file.sha)
    # time.sleep(1)
    # print(repo,' == UPDATED')
    # print("====================", ' HayotbekAbdulazizov is done ')





















def sudo_placement():
    print("Get ready for Sudo Placement at Geeksforgeeks")

def good_luck():
    print("Good Luck for Test")

def work():
    print("Study and work hard")

def bedtime():
    print("It is bed time go rest")

def geeks():
    g = github.Github("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")
    repo = g.get_user().get_repo('Destry')
    print( 'REPO = ',repo)
    try:
        repo.create_file('commit.txt', 'created from pythonanywhere',"We did it !")
        print(repo,' == CREATED')
    except:
        file = repo.get_contents("commit.txt")
        repo.update_file("commit.txt", 'updated from pythonanywhere', f"{datetime.datetime.now()}", sha=file.sha)
        time.sleep(1)
        print(repo,' == UPDATED')
    print("====================", ' HayotbekAbdulazizov is done ')

    print("Shaurya says Geeksforgeeks")

# Task scheduling
# After every 10mins geeks() is called.
schedule.every(20).minutes.do(geeks)

# After every hour geeks() is called.
schedule.every().hour.do(geeks)

# Every day at 12am or 00:00 time bedtime() is called.
schedule.every().day.at("23:00").do(bedtime)

# After every 5 to 10mins in between run work()
schedule.every(5).to(10).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    schedule.run_pending()
    time.sleep(1)