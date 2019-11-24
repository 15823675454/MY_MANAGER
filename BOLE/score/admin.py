from django.contrib import admin
from .models import *
# Register your models here.


# 学生成绩
class StudentScoreAdmin(admin.ModelAdmin):
    list_display = ['student', 'chinese', 'math', 'english', 'physical', 'chemistry', 'biological', 'political',
                    'history', 'geography', 'sports', 'art','isActive']
    list_display_links = ['student']
    list_editable = ['chinese', 'math', 'english', 'physical', 'chemistry', 'biological', 'political', 'history',
                     'geography', 'sports', 'art']
    list_filter = ['student']
    search_fields = ['student']


# 作品
class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ['student', 'img', 'score']
    list_display_links = ['student']
    list_editable = ['score']
    list_filter = ['student']
    search_fields = ['student', 'score']


admin.site.register(ArtWork, ArtWorkAdmin)
admin.site.register(StudentScore, StudentScoreAdmin)







