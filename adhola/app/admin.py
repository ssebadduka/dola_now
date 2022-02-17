from django.contrib import admin
from .models import Pray_tb,Comment



# admin.site.register(Pray_tb)
@admin.register(Pray_tb)
class UserAdmin(admin.ModelAdmin):
    # pass
    list_display=('id','Date_Created','Adhola_Prayer','English_Prayer','Book','img','Posted_by','daily_prayer_detail','slug')
    prepopulated_fields = {'slug':('daily_prayer_detail',),}

@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','comment','comment_date')


# Register your models here.
