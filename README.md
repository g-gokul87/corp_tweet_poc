##POC - Twitter Face app for UGC parsing##

Django application allowing users to register via twitter, getting tweets from user, parsing the category, general and specific item type and posting them to twitter with category hashtags.
___
###Requirements###
Specified in the `requirements.txt` file.
___
###Setup###

1. Install all the dependencies using, `pip install -r requirements.txt`.
2. Run `python manange.py runserver` to fireup dev server.
3. Register via twitter and enter tweet content.
4. If a category is recognised from the tweet content, it'll be posted on the `https://twitter.com/GGokul87` timeline. 
5. Check the same in admin. User table is available in `admin/auth/user/` and Tweet Data will be available in `admin/twitter_face/tweetdata/`.

<u>Admin credentials:</u> <br>
Username: *admin* <br>
Password: *password*
___
###Additional Notes###

1. django-allauth is being used for twitter oauth and registration.(https://github.com/pennersr/django-allauth)
2. django-avatar is being used for avatar support.
3. python-twitter is being used for posting tweets.

