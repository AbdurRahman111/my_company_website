from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.


class User_Profile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profile'
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    Account_Active = models.BooleanField(default=False)
    organisation_name = models.CharField(max_length=255)
    address = models.TextField()
    location_ID = models.CharField(max_length=255)
    District_or_Borough_Help = models.CharField(max_length=255, blank=True, null=True)
    Contact_Name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    website_link = models.CharField(max_length=255, blank=True, null=True)
    Charity_Number = models.CharField(max_length=255, blank=True, null=True)
    Company_Registration_Number = models.CharField(max_length=255, blank=True, null=True)
    Role_in_Organisation = models.CharField(max_length=255)
    legal_advice = models.BooleanField(default=False)
    education_matters = models.BooleanField(default=False)
    health_wellbeing = models.BooleanField(default=False)
    employment_jobs = models.BooleanField(default=False)
    somali_mosques = models.BooleanField(default=False)
    Music_Culture_Arts = models.BooleanField(default=False)
    Sport_Recreation = models.BooleanField(default=False)
    Housing = models.BooleanField(default=False)
    Benefits_Debt = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        if self.Account_Active == True:
            print(self.User.is_active)
            self.User.is_active=True
            self.User.save()
        super(User_Profile, self).save(*args, **kwargs)




class news_category(models.Model):
    class Meta:
        verbose_name_plural = 'News Category'

    slug = models.SlugField(default="Auto-Generate", editable=False)
    name = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        # make random order ID
        my_slug = slugify(self.name)
        uniqe_confirm = news_category.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.name))+ "-" + str(count_num)
            if not news_category.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(news_category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def total_news(self):
        return news_table.objects.filter(Category=self).count()


class news_table(models.Model):
    class Meta:
        verbose_name_plural = 'News Table'
    Title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Category = models.ForeignKey(news_category, on_delete=models.CASCADE, blank=True, null=True)
    Author = models.CharField(max_length=255, default="Admin")
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    Short_Description = models.TextField(default="", blank=True, null=True)
    Description = RichTextField(blank=True, null=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        # make random order ID
        my_slug = slugify(self.Title)
        uniqe_confirm = news_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.Title))+ "-" + str(count_num)
            if not news_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(news_table, self).save(*args, **kwargs)


    def count_total_comments_on_news(self):
        return news_comments.objects.filter(news=self).count()



class news_comments(models.Model):
    class Meta:
        verbose_name_plural = 'News Comments'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(news_table, on_delete=models.CASCADE)
    comment = models.TextField()
    Time = models.DateTimeField(default=datetime.now(), blank=True)



class help_and_advice_table(models.Model):
    class Meta:
        verbose_name_plural = 'Help and Advice'
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    short_description = models.TextField()

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        my_slug = slugify(self.title)
        uniqe_confirm = help_and_advice_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.title))+ "-" + str(count_num)
            if not help_and_advice_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(help_and_advice_table, self).save(*args, **kwargs)




class organisation_table(models.Model):
    class Meta:
        verbose_name_plural = 'Organisation Table'
    name = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(help_and_advice_table, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='organisation_img/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    Long_description = RichTextField(blank=True, null=True)
    Get_in_touch_text = RichTextField(blank=True, null=True)
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        my_slug = slugify(self.name)
        uniqe_confirm = organisation_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.name))+ "-" + str(count_num)
            if not organisation_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(organisation_table, self).save(*args, **kwargs)


class events_table(models.Model):
    class Meta:
        verbose_name_plural = 'Event Table'
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    From_Time = models.DateTimeField()
    To_Time = models.DateTimeField()
    Via = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/', default=None, blank=True, null=True)
    Details = RichTextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        my_slug = slugify(self.title)
        uniqe_confirm = events_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.title))+ "-" + str(count_num)
            if not events_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(events_table, self).save(*args, **kwargs)



class projects_table(models.Model):
    class Meta:
        verbose_name_plural = 'Projects Table'
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    image = models.ImageField(upload_to='events/', default=None, blank=True, null=True)
    Details = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        my_slug = slugify(self.title)
        uniqe_confirm = projects_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.title))+ "-" + str(count_num)
            if not projects_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(projects_table, self).save(*args, **kwargs)





class report_table(models.Model):
    class Meta:
        verbose_name_plural = 'Report Table'
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Short_Description = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='events/', default=None, blank=True, null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        my_slug = slugify(self.title)
        uniqe_confirm = report_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.title))+ "-" + str(count_num)
            if not report_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(report_table, self).save(*args, **kwargs)





class Job_vacancies_table(models.Model):
    class Meta:
        verbose_name_plural = 'Job Vacancies Table'
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="Auto-Generate", editable=False)
    Description = RichTextField(blank=True, null=True)
    Last_date = models.DateField(default=datetime.now(), blank=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        my_slug = slugify(self.title)
        uniqe_confirm = Job_vacancies_table.objects.filter(slug=my_slug)
        count_num = 0
        while uniqe_confirm:
            count_num = count_num + 1
            my_slug = str(slugify(self.title))+ "-" + str(count_num)
            if not Job_vacancies_table.objects.filter(slug=my_slug):
                break
        self.slug = my_slug
        super(Job_vacancies_table, self).save(*args, **kwargs)



class NEWSLETTER(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.email_address



class videos_table(models.Model):
    class Meta:
        verbose_name_plural = 'videos Table'
    title = models.CharField(max_length=255)
    video_url_link = EmbedVideoField()
    short_description = models.TextField(blank=True, null=True)
    Time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering=['-added']



