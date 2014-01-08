from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from forms import TweetForm
from utils import parse_category_and_tweet


class HomePageView(TemplateView):
    """
    Home page view to land after login.
    """
    template_name = "tweet.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["tweet_form"] = TweetForm()
        return context


class SaveTweetView(View):
    """
    Saves the tweet in database and post the same to twitter.
    """
    def post(self, request, *args, **kwargs):
        tf = TweetForm(data=request.POST)
        if tf.is_valid():
            tf_obj = tf.save(commit=False)
            tf_obj.tweeted_by = request.user
            tf_obj = parse_category_and_tweet(tf_obj)
            tf_obj.save()
            return HttpResponseRedirect("/")
        else:
            return render_to_response("tweet.html",
                                  {"tweet_form": tf},
                                  context_instance=RequestContext(request))

