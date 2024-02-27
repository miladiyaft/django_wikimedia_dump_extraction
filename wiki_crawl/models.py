from django.db import models

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    description = models.TextField()


class Video(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    url = models.URLField(max_length=200) 


class Image(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    url = models.URLField(max_length=200) 
    alt = models.CharField(max_length=200)


class InternalLink(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    url = models.URLField(max_length=200) 
    anchor_text = models.CharField(max_length=200)
    type = models.CharField(max_length=20)


class ExternalLink(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    url = models.URLField(max_length=200) 
    anchor_text = models.CharField(max_length=200)
    type = models.CharField(max_length=20)

     