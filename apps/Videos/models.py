from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    # is_Fav = models.BooleanField(default=False)
    # Add more fields as necessary, such as category or tags

    def __str__(self):
        return self.title
    
class FavoriteVideos(models.Model):
    user = models.ForeignKey('Users.User', related_name='favorite_videos', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, related_name='favorited_by', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'video')  # Ensures a user can't favorite the same video more than once

    def __str__(self):
        return f"{self.user.username} - {self.video.title}"