from platform import platform
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GFGProfile, CodeChefProfile, LeetCodeProfile, HackerRankProfile
from .serializers import GFGProfileSerializer, CodeChefProfileSerializer, LeetCodeProfileSerializer, HackerRankProfileSerializer


class GetDetails(APIView):
    def get(self, request):
        # Retrieve data from URL params
        username = str(request.GET['username'])
        platform = str(request.GET['platform']).lower()


        # data holder for details
        profileDetail = {}


        # Check for GeeksForGeeks profile, and create/update it in db
        if(platform=='gfg'):
            profileDetail = getGFGProfile(username=username, platform=platform)
            newProfile = GFGProfile(
                username=profileDetail['username'], 
                platform=profileDetail['platform'], 
                problems=profileDetail['problems'],
            )
            newProfile.save()

            # Get serialized data from the profile
            serializer = GFGProfileSerializer(newProfile)


        # Check for LeetCode profile, and create/update it in db
        elif(platform=='leetcode'):
            profileDetail = getLeetCodeProfile(username=username, platform=platform)
            newProfile = LeetCodeProfile(
                username=profileDetail['username'], 
                platform=profileDetail['platform'], 
                problems=profileDetail['problems'],
            )
            newProfile.save()
            
            # Get serialized data from the profile
            serializer = LeetCodeProfileSerializer(newProfile)


        # Check for CodeChef profile, and create/update it in db
        elif(platform=='codechef'):
            profileDetail = getCodeChefProfile(username=username, platform=platform)
            newProfile = CodeChefProfile(
                username=profileDetail['username'], 
                platform=profileDetail['platform'], 
                problems=profileDetail['problems'],
            )
            newProfile.save()
            
            # Get serialized data from the profile
            serializer = CodeChefProfileSerializer(newProfile)


        # Check for HackerRank profile, and create/update it in db
        elif(platform=='hackerrank'):
            profileDetail = getHackerRankProfile(username=username, platform=platform)
            newProfile = HackerRankProfile(
                username=profileDetail['username'], 
                platform=profileDetail['platform'], 
                problems=profileDetail['problems'],
            )
            newProfile.save()
            
            # Get serialized data from the profile
            serializer = HackerRankProfileSerializer(newProfile)


        # Return 404 in case of none above
        else:
            return Response({'status': '404'}, status=status.HTTP_404_NOT_FOUND)

        
        # Add status code to response
        data = serializer.data
        data['status'] = '200'

        # return the API response as json
        return Response(data)
        

        
def getGFGProfile(username, platform):
    # Retrieve GFG profile

    url = f'https://auth.geeksforgeeks.org/user/{username}/profile'
    profile = {
        "username": username,
        "platform": platform,
        "problems": 0,
    }
    return profile



def getLeetCodeProfile(username, platform):
    
    url = f'https://leetcode.com/{username}/'
    profile = {
        "username": username,
        "platform": platform,
        "problems": 0,
    }
    return profile



def getCodeChefProfile(username, platform):
    
    url = f'https://www.codechef.com/users/{username}'
    profile = {
        "username": username,
        "platform": platform,
        "problems": 0,
    }
    return profile



def getHackerRankProfile(username, platform):
    
    url = f'https://www.hackerrank.com/{username}'
    profile = {
        "username": username,
        "platform": platform,
        "problems": 0,
    }
    return profile


