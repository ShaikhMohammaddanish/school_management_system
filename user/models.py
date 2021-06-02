from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.


user_types = [
        ('admin', 'admin'),
        ('teacher', 'teacher'),
        ('student', 'student'),
    ]

gender_chice = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

class myAccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email.')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user= self.create_user(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self.db)
        return user


class userProfile(AbstractBaseUser):

    email = models.EmailField(max_length=60, unique=True, verbose_name='Email')
    user_name =  models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField( auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    user_type = models.CharField(max_length=10, choices=user_types, default='student')
    Contact_no = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10 , choices=gender_chice, default='Male')
    Address = models.TextField(max_length=100)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user_profile', default='user_profile/defult.png')


    USERNAME_FIELD= 'email'

    objects = myAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj = None):
        return self.is_admin


    def has_module_perms(self, app_Label):
        return True



