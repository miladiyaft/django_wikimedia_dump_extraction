from django.db import models

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    main_content = models.TextField()

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    url = models.URLField() 


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

class Tag(models.Model):
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=200)
     