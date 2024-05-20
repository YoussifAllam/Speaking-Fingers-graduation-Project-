from django.db import models

# Create your models here.
class Level_1_const(models.Model): 
    # sound_id = models.AutoField(primary_key=True)
    sound_txt = models.CharField(max_length = 10)
    description = models.TextField()


class Level_2_v_d(models.Model):
    # sound_id = models.AutoField(primary_key=True)
    sound = models.CharField(max_length = 10)
    description = models.TextField()
    
class Level_3_sent(models.Model):
    # sentence_id = models.AutoField(primary_key=True)
    sentence = models.CharField(max_length=200, blank=True)
    
    
class  ReadingTest(models.Model):
    # id = models.AutoField(primary_key=True)
    words_and_sents = models.CharField(max_length = 200,blank=True)