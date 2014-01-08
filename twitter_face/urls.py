from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import HomePageView, SaveTweetView


urlpatterns = patterns('twitter_face.views',
    url(r'^$', login_required(HomePageView.as_view()), name='home'),
    url(r'^tweet/save/$', login_required(SaveTweetView.as_view()), name='save_tweet'),
)
