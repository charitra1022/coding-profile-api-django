import requests
from bs4 import BeautifulSoup



headers = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36"
    }


def getGFGProfile(username, platform):
    # Retrieve GFG profile
    
    url = f'https://auth.geeksforgeeks.org/user/{username}/practice'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    problemsSolved = soup.find('a', attrs={'href': '#problem-solved-div'}).text.split(':')[1].split()[0]

    profile = {
        "username": username,
        "platform": platform,
        "problems": int(problemsSolved),
    }
    return profile

