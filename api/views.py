from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import GFGProfile, CodeChefProfile, LeetCodeProfile, HackerRankProfile
from .serializers import GFGProfileSerializer, CodeChefProfileSerializer, LeetCodeProfileSerializer, HackerRankProfileSerializer
from .scrapping import getCodeChefProfile, getHackerRankProfile, getGFGProfile, getLeetCodeProfile



def home(request):
    return render(request, 'api/home.html', {})





def GFGProfileOperation(username:str, platform:str):
    '''
    Gets scarpped profile details for GFG, performs db operations and returns serializer object for api

    param:  
        username -> username of the user to get details
        platfrom -> platform to get details from
    return:
        serializer -> API serializer object
    '''

    data = {}

    # Get GeeksForGeeks profile
    profileDetail = getGFGProfile(username=username, platform=platform)
    data['status'] = profileDetail['status']    # is user found?
    
    # if profile is not found, return http 404 with status as False
    if(not profileDetail['status']): 
        data['response'] = Response(profileDetail, status=status.HTTP_404_NOT_FOUND)
        return data

    # If profile is found, create/update it in db
    newProfile = GFGProfile(
        username=profileDetail['username'], 
        platform=profileDetail['platform'], 
        problems=profileDetail['problems'],
    )
    newProfile.save()

    # Get serialized data from the profile
    data['serializer'] = GFGProfileSerializer(newProfile)
    return data



def CodeChefProfileOperation(username:str, platform:str):
    '''
    Gets scarpped profile details for CodeChef, performs db operations and returns serializer object for api

    param:  
        username -> username of the user to get details
        platfrom -> platform to get details from
    return:
        serializer -> API serializer object
    '''

    data = {}

    # Get CodeChef profile
    profileDetail = getCodeChefProfile(username=username, platform=platform)
    data['status'] = profileDetail['status']    # is user found?
    
    # if profile is not found, return http 404 with status as False
    if(not profileDetail['status']): 
        data['response'] = Response(profileDetail, status=status.HTTP_404_NOT_FOUND)
        return data

    # If profile is found, create/update it in db
    newProfile = CodeChefProfile(
        username=profileDetail['username'], 
        platform=profileDetail['platform'], 
        stars=profileDetail['stars'],
        rating=profileDetail['rating'],
        icon=profileDetail['icon'],
    )
    newProfile.save()

    # Get serialized data from the profile
    data['serializer'] = CodeChefProfileSerializer(newProfile)
    return data


def LeetCodeProfileOperation(username:str, platform:str):
    '''
    Gets scarpped profile details for LeetCode, performs db operations and returns serializer object for api

    param:  
        username -> username of the user to get details
        platfrom -> platform to get details from
    return:
        serializer -> API serializer object
    '''

    data = {}

    # Get LeetCode profile
    profileDetail = getLeetCodeProfile(username=username, platform=platform)
    data['status'] = profileDetail['status']    # is user found?
    
    # if profile is not found, return http 404 with status as False
    if(not profileDetail['status']): 
        data['response'] = Response(profileDetail, status=status.HTTP_404_NOT_FOUND)
        return data

    # If profile is found, create/update it in db
    newProfile = LeetCodeProfile(
        username=profileDetail['username'], 
        platform=profileDetail['platform'], 
        problems=profileDetail['problems'],
    )
    newProfile.save()

    # Get serialized data from the profile
    data['serializer'] = LeetCodeProfileSerializer(newProfile)
    return data


def HackerRankProfileOperation(username:str, platform:str):
    '''
    Gets scarpped profile details for HackerRank, performs db operations and returns serializer object for api

    param:  
        username -> username of the user to get details
        platfrom -> platform to get details from
    return:
        serializer -> API serializer object
    '''

    data = {}

    # Get HackerRank profile
    profileDetail = getHackerRankProfile(username=username, platform=platform)
    data['status'] = profileDetail['status']    # is user found?
    
    # if profile is not found, return http 404 with status as False
    if(not profileDetail['status']): 
        data['response'] = Response(profileDetail, status=status.HTTP_404_NOT_FOUND)
        return data

    # If profile is found, create/update it in db
    newProfile = HackerRankProfile(
        username=profileDetail['username'], 
        platform=profileDetail['platform'], 
        badges=profileDetail['badges'],
    )
    newProfile.save()

    # Get serialized data from the profile
    data['serializer'] = HackerRankProfileSerializer(newProfile)
    return data






class GetDetails(APIView):
    def get(self, request):
        # Retrieve data from URL params
        username = str(request.GET['username'])
        platform = str(request.GET['platform']).lower()


        # data holder for details
        profileDetail = {}


        # Check for GeeksForGeeks profile, and create/update it in db
        if(platform=='gfg'):
            data = GFGProfileOperation(username, platform)
            if(not data['status']): return data['response']
            
            # Get serialized data from the profile
            serializer = data['serializer']


        # Check for LeetCode profile, and create/update it in db
        elif(platform=='leetcode'):
            data = LeetCodeProfileOperation(username, platform)
            if(not data['status']): return data['response']
            
            # Get serialized data from the profile
            serializer = data['serializer']


        # Check for CodeChef profile, and create/update it in db
        elif(platform=='codechef'):
            data = CodeChefProfileOperation(username, platform)
            if(not data['status']): return data['response']
            
            # Get serialized data from the profile
            serializer = data['serializer']


        # Check for HackerRank profile, and create/update it in db
        elif(platform=='hackerrank'):
            data = HackerRankProfileOperation(username, platform)
            if(not data['status']): return data['response']
            
            # Get serialized data from the profile
            serializer = data['serializer']


        # Return 404 in case of none above
        else:
            return Response({
                'status': False,
                'message': "incorrect value of platform parameter",
                }, status=status.HTTP_404_NOT_FOUND)

        
        # Add status code to response
        data = serializer.data
        data['status'] = True

        # return the API response as json
        return Response(data, status=status.HTTP_302_FOUND)

