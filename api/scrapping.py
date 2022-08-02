from types import NoneType
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

    try:
        # Try to look for userName span in html content. If not found, user doesnt exist
        soup.find('span', attrs={'class':'userName'}).text
    except:
        # the tag wasnt found, so user doesnt exist
        return {
            'status': False,
            'message': "user not found",
        }

    problemsSolved = int(soup.find('a', attrs={'href': '#problem-solved-div'}).text.split(':')[1].split()[0])

    profile = {
        "username": username,
        "platform": platform,
        "problems": problemsSolved,
        "status": True,
    }
    return profile



def getLeetCodeProfile(username, platform):
    # Retrieve LeetCode profile

    url = r'https://leetcode.com/graphql?query={matchedUser(username:%20%22{username}%22)%20{username%20submitStats:submitStatsGlobal%20{acSubmissionNum%20{difficulty%20count%20submissions}}}}'
    url = url.replace('{username}', username)
    
    r = requests.get(url=url, headers=headers)
    data = r.json()

    # check if user has been found or not
    if(type(data['data']['matchedUser'])==NoneType):
        return {
            'status': False,
            'message': "user not found",
        }

    problemsSolved = int(data['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count'])

    profile = {
        "username": username,
        "platform": platform,
        "problems": problemsSolved,
        "status": True,
    }
    return profile



def getCodeChefProfile(username, platform):
    # Retrieve CodeChef profile
    
    url = f'https://www.codechef.com/users/{username}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')


    try:
        # Try to look for m-username--link span in html content. If not found, user doesnt exist
        text = soup.find('span', attrs={'class':'m-username--link'}).text
        if(not text==username):
            # raise exception if not same as requested user
            raise ValueError()
    except:
        # exception raised, so user doesnt exist
        return {
            'status': False,
            'message': "user not found",
        }

    ### After addition of Provisional rating on 02-08-2022, rating scrapping changed
    # rating = int(soup.find('div', attrs={'class': 'rating-number'}).text)     ## old method
    rating = int(soup.find('div', attrs={'class': 'rating-number'}).text.split("?")[0])
    stars = len(soup.find('div', attrs={'class': 'rating-star'}).find_all('span'))
    icon = str(soup.find('div', attrs={'class': 'rating-star'}))

    profile = {
        "username": username,
        "platform": platform,
        "stars": stars,
        "rating": rating,
        "icon": icon,
        "status": True,
    }

    return profile
    


def getHackerRankProfile(username, platform):
    # Retrieve HackerRank profile
    
    url = f'https://www.hackerrank.com/{username}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')

    try:
        # Try to look for profile-username-heading p in html content. If not found, user doesnt exist
        soup.find('p', attrs={'class':'profile-username-heading'}).text
    except:
        # the tag wasnt found, so user doesnt exist
        return {
            'status': False,
            'message': "user not found",
        }

    badgesList = soup.find('div', attrs={'class': 'badges-list'}).find_all('div', attrs={'class': 'hacker-badge'})
    badgeData = []

    for badge in badgesList:
        name = badge.find('text', attrs={'class': 'badge-title'}).text
        stars = len(badge.find_all('svg', attrs={'class', 'badge-star'}))
        icon = str(badge.find('div', attrs={'class': 'ui-badge-wrap'}))
        data = {
            name: {
                'stars': stars,
                'icon': icon,
            }
        }
        badgeData.append(data)

    profile = {
        "username": username,
        "platform": platform,
        "badges": badgeData,
        "status": True,
    }
    return profile
