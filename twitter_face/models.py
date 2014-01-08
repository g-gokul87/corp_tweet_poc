from django.db import models
from django.contrib.auth.models import User


class TweetData(models.Model):
    """
    Model holds the tweets.
    """
    content = models.CharField('Original Content', max_length=110)
    tweeted_content = models.CharField('Tweeted Content', max_length=255)
    tweeted_by = models.ForeignKey(User, related_name='tweets')
    submitted_on = models.DateTimeField('Submitted On', auto_now_add=True)
    published_on = models.DateTimeField('Published On', blank=True, null=True)
    category = models.CharField('Category', max_length=255, blank=True, default='Unknown')
    generic_item_type = models.CharField('Generic Item Type', max_length=255, blank=True, default='Unknown')
    specific_item_type = models.CharField('Specific Item Type', max_length=255, blank=True, default='Unknown')

    def __unicode__(self):
        return self.content
