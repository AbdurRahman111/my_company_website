from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.member_login, name="member_login"),
    path('func_logout', views.func_logout, name="func_logout"),
    path('post_newsletter', views.post_newsletter, name="post_newsletter"),
    path('video', views.all_videos, name="all_videos"),
    path('help-and-advice', views.help_and_advice, name="help_and_advice"),
    path('help-and-advice/<str:slug>', views.details_help_advice, name="details_help_advice"),
    path('news', views.news, name="news"),
    path('news/<str:slug>', views.news_details, name="news_details"),
    path('news/news-category/<str:slug>', views.all_news_category, name="all_news_category"),
    path('events-and-training', views.events_and_training, name="events_and_training"),
    path('events-and-training/<str:slug>', views.event_details, name="event_details"),
    path('our-members', views.our_members, name="our_members"),
    path('our-members/<str:slug>', views.organization_details, name="organization_details"),
    path('who-we-are', views.who_we_are, name="who_we_are"),
    path('what-we-do', views.what_we_do, name="what_we_do"),
    path('our-vision', views.our_vision, name="our_vision"),
    path('join-the-BSYV', views.join_the_BSYV, name="join_the_BSYV"),
    path('join-the-BSYV/signup-now', views.signup_now, name="signup_now"),
    path('Newsletter-page', views.Newsletter_page, name="Newsletter_page"),
    path('our-projects', views.our_projects, name="our_projects"),
    path('our-projects/<str:slug>', views.project_details, name="project_details"),
    path('Research-and-Reports', views.Research_and_Reports, name="Research_and_Reports"),
    path('job-vacancies', views.job_vacancies, name="job_vacancies"),
    path('job-vacancies/<str:slug>', views.job_details, name="job_details"),
]