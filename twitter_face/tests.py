"""
Unit tests for twitter_face app.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from models import TweetData


class TweetDataTest(object):
    """
    Base class for Tweet Data test.
    """
    def create_test_user(self):
        """
        Creates an User object.
        """
        return User.objects.create_user("john", "lennon@example.com", "johnpassword")

    def create_tweet_data(self, title="Test TweetData"):
        """
        Creates a TweetData object.
        """
        return TweetData.objects.create(content="blah blah blah",
                                        tweeted_content="blah blah blah #custom",
                                        tweeted_by=self.create_test_user(),
                                        submitted_on=timezone.now())


class TweetDataModelTest(TestCase, TweetDataTest):
    """
    This test case tests the TweeData model.
    """
    def test_tweet_data(self):
        """
        Tests the TweetData model and unicode function
        """
        td = self.create_tweet_data()
        self.assertTrue(isinstance(td, TweetData))
        self.assertEqual(td.__unicode__(), td.content)


class TweetDataViewsTest(TestCase, TweetDataTest):
    """
    This test case tests the tweet face apps views.
    """
    def test_home_page_view(self):
        """
        Tests the home page view.
        """
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_save_tweet_view(self):
        """
        Tests the save tweet view.
        """
        url = reverse("save_tweet")
        user = self.create_test_user()
        self.client.login(username=user.username, password=user.password)
        response = self.client.post(url, {"content": "Just bought an awesome wedding ring!", })
        self.assertEqual(response.status_code, 302)
