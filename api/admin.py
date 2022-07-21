from django.contrib import admin
from .models import CodeChefProfile, LeetCodeProfile, HackerRankProfile, GFGProfile

admin.site.register(GFGProfile)
admin.site.register(CodeChefProfile)
admin.site.register(LeetCodeProfile)
admin.site.register(HackerRankProfile)
