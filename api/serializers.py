from dataclasses import field, fields
from rest_framework import serializers
from .models import CodeChefProfile, LeetCodeProfile, HackerRankProfile, GFGProfile


class GFGProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GFGProfile
        fields = ('username', 'platform', 'problems')


class CodeChefProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeChefProfile
        fields = ('username', 'platform', 'stars', 'rating')


class LeetCodeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeetCodeProfile
        fields = ('username', 'platform', 'problems')


class HackerRankProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackerRankProfile
        fields = ('username', 'platform', 'badges')



