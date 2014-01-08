from django.forms import ModelForm
from django import forms
from models import TweetData


class TweetForm(ModelForm):
    """
    Form to collect the tweet data from the user.
    """
    content = forms.CharField(required=True,
                              widget=forms.widgets.Textarea(attrs={'cols': 30,
                                                                   'rows': 5,
                                                                   'maxlength': 110}))

    class Meta:
        model = TweetData
        exclude = ('tweeted_by', 'submitted_on', 'category', 'tweeted_content',
                   'generic_item', 'specific_item_type', 'published_on')
