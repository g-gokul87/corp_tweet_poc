import os
import re
import csv
import twitter
from django.conf import settings
from django.utils import timezone


def parse_category_and_tweet(tf_obj):
    """
    Parse the category, general and specific item type and tweet if the category detected.
    """
    # Reading the taxonamy file
    csv_data = csv.reader(open(os.path.join(settings.ROOT_DIR,
                                    settings.TAXONAMY_FILE_NAME), "rU"))
    csv_list = list(csv_data)[1:]  # Ignoring the header row
    # Removing special characters except whitespace from the user submitted string.
    corrected_tweet = re.sub("[^A-Za-z0-9\s]+", "", tf_obj.content.lower())
    can_break = False
    for each_row in csv_list:
        # Do a substring match of specific item type with corrected tweet.
        if find_whole_match(each_row[2])(corrected_tweet):
            # Matched Specific item, set category and general item type.
            tf_obj.category = each_row[0]
            tf_obj.generic_item_type = each_row[1]
            tf_obj.specific_item_type = each_row[2]
            can_break = True

        # Do a substring match of general item type with corrected tweet.
        elif find_whole_match(each_row[1])(corrected_tweet):
            # Matched Specific item, set category, and general item type.
            tf_obj.category = each_row[0]
            tf_obj.generic_item_type = each_row[1]
            can_break = True

        # Do a substring match of Category with corrected tweet.
        elif find_whole_match(each_row[0])(corrected_tweet):
            # Matched Specific item, set category, and general item type.
            tf_obj.category = each_row[0]
            can_break = True

        if can_break:
            # Comes here only when the break encountered. i.e., when a category detected.
            tf_obj.tweeted_content = "RT:%s %s #Custom #%s" % (tf_obj.tweeted_by.username,
                                                           tf_obj.content, each_row[0])
            # Tweet it.
            if tweet(tf_obj.tweeted_content):
                tf_obj.published_on = timezone.now()
            break

    return tf_obj


def tweet(status):
    """
    Post the tweet status to twitter.
    """
    from allauth.socialaccount.models import SocialApp
    # Posting to twitter
    try:
        social_app = SocialApp.objects.get(provider="twitter")
        api = twitter.Api(consumer_key=social_app.client_id,
                          consumer_secret=social_app.secret,
                          access_token_key=settings.ACCESS_TOKEN,
                          access_token_secret=settings.ACCESS_SECRET)
        api.PostUpdate(status)
    except:  # Twitter API exceptions.
        pass
    else:  # On successful twitter posting, return True.
        return True
    return False


def find_whole_match(w):
    """
    Returns a search object for the whole words substring match.
    """
    return re.compile(r"\b({0})\b".format(w), flags=re.IGNORECASE).search
