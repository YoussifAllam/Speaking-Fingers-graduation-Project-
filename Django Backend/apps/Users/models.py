from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')
    otp = models.IntegerField(default=0)
    otp_created_at = models.DateTimeField(auto_now_add=True)

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username



class Profile(models.Model):
    
    """
    receiver decorator registers the save_profile function as a receiver of the post_save signal for the User model.
    This means that save_profile is called every time a User instance is saved.
    
    save_profile Function: Inside this function, 
    a check is performed to determine if the save operation corresponds to the creation of a new User instance (if created:).
    If so, a corresponding Profile instance is automatically created with Profile.objects.get_or_create(user=instance)
    
    """
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    reset_password_token = models.CharField(max_length=50,default="",blank=True)
    reset_password_expire = models.DateTimeField(null=True,blank=True) 
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    else:
        # For existing users without a profile, create one
        if not hasattr(instance, 'profile'):
            Profile.objects.get_or_create(user=instance)
            
            