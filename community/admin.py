from django.contrib import admin
from .models import news_table, news_category, news_comments, help_and_advice_table, organisation_table, events_table, projects_table, report_table, Job_vacancies_table, NEWSLETTER, videos_table, User_Profile
# Register your models here.


admin.site.register(news_table)
admin.site.register(news_category)
admin.site.register(help_and_advice_table)
admin.site.register(report_table)
admin.site.register(Job_vacancies_table)

class show_organisation(admin.ModelAdmin):
    list_display = ['name', 'title', 'facebook_link', 'twitter_link']
admin.site.register(organisation_table, show_organisation)


class show_comments(admin.ModelAdmin):
    list_display = ['user', 'news', 'comment', 'Time']
admin.site.register(news_comments, show_comments)


class show_NEWSLETTER(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address', 'Time']
admin.site.register(NEWSLETTER, show_NEWSLETTER)


class show_events_table(admin.ModelAdmin):
    list_display = ['title', 'From_Time', 'To_Time', 'Via', 'active']
admin.site.register(events_table, show_events_table)



class show_projects_table(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(projects_table, show_projects_table)


class show_post_youtube_video(admin.ModelAdmin):
    list_display = ['title', 'video_url_link', 'Time']
admin.site.register(videos_table, show_post_youtube_video)


class show_User_Profile(admin.ModelAdmin):
    list_display = ['Name', 'email', 'Account_Active', 'Role_in_Organisation', 'organisation_name', 'location_ID', 'Contact_Name', 'email_address']
    readonly_fields = ['password']
admin.site.register(User_Profile, show_User_Profile)