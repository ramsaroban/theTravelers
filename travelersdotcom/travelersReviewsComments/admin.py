from django.contrib import admin
from .models import (
    TravelersVisitingPlaceReviewsComment
)

class TravelersVisitingPlaceReviewsCommentAdmin(admin.ModelAdmin):
    list_display = ['id','user','place','rating','created_at','updated_at']
    search_filed = ['user','place']



admin.site.register(TravelersVisitingPlaceReviewsComment, TravelersVisitingPlaceReviewsCommentAdmin)
