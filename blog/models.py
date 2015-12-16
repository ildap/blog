from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    text = models.CharField(max_length=1000)
    date = models.DateField()

    def __unicode__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog)
    text = models.TextField()

    def __unicode__(self):
        return self.blog.title
