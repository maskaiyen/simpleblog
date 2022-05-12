from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # bio = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    # website_url = models.CharField(max_length=255, null=True, blank=True)
    # facebook_url = models.CharField(max_length=255, null=True, blank=True)
    # twitter_url = models.CharField(max_length=255, null=True, blank=True)
    # instagram_url = models.CharField(max_length=255, null=True, blank=True)
#     pinterest_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(null=True, blank=True, max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    # content = RichTextField(blank=True, null=True)
    # content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
        # return reverse('home')