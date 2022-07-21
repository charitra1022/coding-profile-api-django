from django.db import models

class GFGProfile(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    platform = models.CharField(max_length=20)
    problems = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        msg = f"{self.platform}:{self.username}"
        return msg


class CodeChefProfile(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    platform = models.CharField(max_length=20)
    stars = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        msg = f"{self.platform}:{self.username}"
        return msg


class LeetCodeProfile(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    platform = models.CharField(max_length=20)
    problems = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        msg = f"{self.platform}:{self.username}"
        return msg


class HackerRankProfile(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    platform = models.CharField(max_length=20)
    badges = models.JSONField(default=list)

    def __str__(self) -> str:
        msg = f"{self.platform}:{self.username}"
        return msg
