from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from autoslug import AutoSlugField

        

class User(AbstractUser):
    email = models.EmailField(unique = True)
    gender = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='user_images/')
    phone_no = models.CharField(max_length = 10)
    
    def __str__(self):
            return "{}".format(self.email)

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
            return self.name   

class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
            return self.name  
 
      

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=250)
    text = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnail_images/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): 
            return self.title + ' | ' + str(self.author)

class Comment(models.Model):          
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(null=True , blank=True)
    name = models.CharField(max_length=250, null=True , blank=True)
    text = models.TextField(null=True , blank=True)
    # comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='replies')
   
    class Meta:
       ordering=['-created_date']

    def __str__(self):
       return str(self.name) + ' comment ' + str(self.text)

    @property
    def children(self):
       return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


    
