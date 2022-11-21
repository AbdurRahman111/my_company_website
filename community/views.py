from django.shortcuts import render, redirect
from .models import news_table, news_category, news_comments, help_and_advice_table, organisation_table, events_table, projects_table, report_table, Job_vacancies_table, NEWSLETTER, videos_table, User_Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage
# Create your views here.

def index(request):
    all_help_and_advice = help_and_advice_table.objects.all()

    try:
        last_news = news_table.objects.last()
    except:
        last_news = None

    try:
        var_events = events_table.objects.filter(active=True).last()
    except:
        var_events=None

    get_last_three_news = news_table.objects.all().order_by('-id')[:3]

    last_video = videos_table.objects.all().last()

    context = {'all_help_and_advice':all_help_and_advice, 'last_news':last_news, 'var_events':var_events, 'get_last_three_news':get_last_three_news, 'last_video':last_video}
    return render(request, 'index.html', context)



def member_login(request):
    if request.method == "POST":
        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')

        # this is for authenticate username and password for login
        user = authenticate(username=login_email, password=login_password)

        # erorr_message_2 = ""

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            # erorr_message_2 = "Invalid Credentials, Please Try Again !!"
            value_func2 = {'login_email': login_email}
            messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'member_login.html', value_func2)
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, "member_login.html")


def func_logout(request):
    # this is for logout from user id
    logout(request)
    return redirect('member_login')


def post_newsletter(request):
    newsletter_first_name = request.POST.get('newsletter_first_name')
    newsletter_last_name = request.POST.get('newsletter_last_name')
    newsletter_email = request.POST.get('newsletter_email')

    var_NEWSLETTER = NEWSLETTER(first_name=newsletter_first_name,
                                last_name=newsletter_last_name,
                                email_address=newsletter_email)
    var_NEWSLETTER.save()
    messages.success(request, "Successfully Subscribe to NEWSLETTER!")
    return redirect('index')


def help_and_advice(request):
    all_help_and_advice = help_and_advice_table.objects.all()
    context = {'all_help_and_advice':all_help_and_advice}
    return render(request, 'help_and_advice.html', context)


def details_help_advice(request, slug):
    if help_and_advice_table.objects.filter(slug=slug):
        get_help_and_advice = help_and_advice_table.objects.get(slug=slug)
        filter_org = organisation_table.objects.filter(category = get_help_and_advice)
        context = {'get_help_and_advice':get_help_and_advice, 'filter_org':filter_org}
        return render(request, 'details_help_advice.html', context)
    else:
        return render(request, '404_page.html')




def news(request):
    all_news = news_table.objects.all().order_by('-id')

    # pagination
    p = Paginator(all_news, 12)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(list)
    context = {'all_news':page, 'list':list, 'page_num':int(page_num)}
    return render(request, 'news.html', context)


def news_details(request, slug):
    if request.method == "POST":
        comment_name = request.POST.get('comment_name')
        var_news_slug = request.POST.get('var_news_slug')
        get_news = news_table.objects.get(slug=var_news_slug)
        var_com = news_comments(user=request.user, news=get_news, comment=comment_name)
        var_com.save()

        # messages.success(request, "")
        return redirect('news_details', var_news_slug)
    else:
        if news_table.objects.filter(slug=slug):
            get_news = news_table.objects.get(slug=slug)
            all_news_categories = news_category.objects.all()
            all_comments = news_comments.objects.filter(news = get_news)

            recent_news = news_table.objects.all().order_by('-id')[:5]

            context = {'get_news':get_news, 'all_news_categories':all_news_categories, 'all_comments':all_comments, 'recent_news':recent_news}
            return render(request, 'news_details.html', context)
        else:
            return render(request, '404_page.html')



def events_and_training(request):
    all_events = events_table.objects.filter(active=True)
    context = {'all_events':all_events}
    return render(request, 'events_and_training.html', context)



def event_details(request, slug):
    if events_table.objects.filter(active=True, slug=slug):
        get_events = events_table.objects.get(active=True, slug=slug)
        context = {'get_events':get_events}
        return render(request, 'event_details.html', context)
    else:
        return render(request, '404_page.html')


def all_news_category(request, slug):
    if news_category.objects.get(slug=slug):
        get_cat = news_category.objects.get(slug=slug)
        all_news = news_table.objects.filter(Category=get_cat).order_by('-id')
        context = {'all_news': all_news}
        return render(request, 'news.html', context)
    else:
        return render(request, '404_page.html')



def our_members(request):
    all_members = organisation_table.objects.all()
    context = {'all_members':all_members}
    return render(request, 'our_members.html', context)


def organization_details(request, slug):
    if organisation_table.objects.filter(slug=slug):
        get_org = organisation_table.objects.get(slug=slug)
        context = {'get_org': get_org}
        return render(request, 'organization_details.html', context)
    else:
        return render(request, '404_page.html')



def who_we_are(request):
    return render(request, 'who_we_are.html')


def what_we_do(request):
    return render(request, 'what_we_do.html')


def our_vision(request):
    return render(request, 'our_vision.html')


def join_the_BSYV(request):
    return render(request, 'join_the_BSYV.html')



def signup_now(request):
    if request.method == "POST":
        organisation_name = request.POST.get('organisation_name')
        address = request.POST.get('address')
        location_ID = request.POST.get('location_ID')
        District_or_Borough_Help = request.POST.get('District_or_Borough_Help')
        Contact_Name = request.POST.get('Contact_Name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number')
        website_link = request.POST.get('website_link')
        Charity_Number = request.POST.get('Charity_Number')
        Company_Registration_Number = request.POST.get('Company_Registration_Number')
        Your_first_Name = request.POST.get('Your_first_Name')
        Your_last_Name = request.POST.get('Your_last_Name')
        your_email = request.POST.get('your_email')
        your_password = request.POST.get('your_password')
        Role_in_Organisation = request.POST.get('Role_in_Organisation')

        legal_advice = request.POST.get('legal_advice')
        if legal_advice == 'on':
            legal_advice=True
        else:
            legal_advice = False
        education_matters = request.POST.get('education_matters')
        if education_matters == 'on':
            education_matters=True
        else:
            education_matters = False
        health_wellbeing = request.POST.get('health_wellbeing')
        if health_wellbeing == 'on':
            health_wellbeing=True
        else:
            health_wellbeing = False
        employment_jobs = request.POST.get('employment_jobs')
        if employment_jobs == 'on':
            employment_jobs=True
        else:
            employment_jobs = False
        somali_mosques = request.POST.get('somali_mosques')
        if somali_mosques == 'on':
            somali_mosques=True
        else:
            somali_mosques = False
        Music_Culture_Arts = request.POST.get('Music_Culture_Arts')
        if Music_Culture_Arts == 'on':
            Music_Culture_Arts=True
        else:
            Music_Culture_Arts = False
        Sport_Recreation = request.POST.get('Sport_Recreation')
        if Sport_Recreation == 'on':
            Sport_Recreation=True
        else:
            Sport_Recreation = False
        Housing = request.POST.get('Housing')
        if Housing == 'on':
            Housing=True
        else:
            Housing = False
        Benefits_Debt = request.POST.get('Benefits_Debt')
        if Benefits_Debt == 'on':
            Benefits_Debt=True
        else:
            Benefits_Debt = False

        # create user
        myuser = User.objects.create_user(your_email, your_email, your_password)
        myuser.first_name = Your_first_Name
        myuser.last_name = Your_last_Name
        myuser.is_active = False
        myuser.save()

        var_User_Profile = User_Profile(
            User=myuser,
            Name=Your_first_Name + " "+ Your_last_Name,
            email = your_email,
            password = make_password(your_password),
            organisation_name = organisation_name,
            address = address,
            location_ID = location_ID,
            District_or_Borough_Help = District_or_Borough_Help,
            Contact_Name = Contact_Name,
            email_address = email_address,
            phone_number = phone_number,
            website_link = website_link,
            Charity_Number = Charity_Number,
            Company_Registration_Number = Company_Registration_Number,
            Role_in_Organisation = Role_in_Organisation,
            legal_advice = legal_advice,
            education_matters = education_matters,
            health_wellbeing = health_wellbeing,
            employment_jobs = employment_jobs,
            somali_mosques = somali_mosques,
            Music_Culture_Arts = Music_Culture_Arts,
            Sport_Recreation = Sport_Recreation,
            Housing = Housing,
            Benefits_Debt = Benefits_Debt,
        )
        var_User_Profile.save()

        messages.success(request, "Submitted! Your Account is under review. In 24 hours you will get account confirmation email. Thanks")


    return render(request, 'signup_now.html')


def Newsletter_page(request):
    return render(request, 'Newsletter_page.html')


def our_projects(request):
    all_projects = projects_table.objects.all()
    # pagination
    p = Paginator(all_projects, 12)
    # print(p.num_pages)
    number_of_pages = p.num_pages

    # show list of pages
    number_of_pages_1 = p.num_pages + 1
    list = []
    for i in range(1, number_of_pages_1):
        list.append(i)

    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    print(list)
    context = {'all_projects': page, 'list': list, 'page_num': int(page_num)}
    return render(request, 'our_projects.html', context)


def project_details(request, slug):
    if projects_table.objects.filter(slug=slug):
        get_projects = projects_table.objects.get(slug=slug)
        context = {'get_projects':get_projects}
        return render(request, 'project_details.html', context)
    else:
        return render(request, '404_page.html')

def Research_and_Reports(request):
    all_report = report_table.objects.all()
    context = {'all_report':all_report}
    return render(request, 'Research_and_Reports.html', context)


def job_vacancies(request):
    all_jobs = Job_vacancies_table.objects.all()
    context = {'all_jobs':all_jobs}
    return render(request, 'job_vacancies.html', context)


def job_details(request, slug):
    if Job_vacancies_table.objects.filter(slug=slug):
        get_jobs = Job_vacancies_table.objects.get(slug=slug)
        context = {'get_jobs':get_jobs}
        return render(request, 'job_details.html', context)
    else:
        return render(request, '404_page.html')




def all_videos(request):
    all_videos_var = videos_table.objects.all()
    context = {'all_videos_var':all_videos_var}
    return render(request, 'all_videos.html', context)


