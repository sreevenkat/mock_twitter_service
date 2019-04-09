#!/usr/bin/env python
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from tweets.models import Tweet, TweetReplies, TweetLikes


class Command(BaseCommand):

    def handle(self, *args, **options):

        user = User(username="sree-venkat", first_name="Sreevenkat", 
                    last_name="Ganapathi", email="gsvetr@gmail.com", 
                    is_superuser=True)
        user.set_password("hello")
        user.save()

        user1 = User(username="siva-shankar", first_name="SivaShankar", 
                    last_name="Ramesh", email="appooti@mac.com", 
                    is_superuser=True)
        user1.set_password("hello")
        user1.save()

        hello_tweet = Tweet(text="Hello twitter. Hit me up.", user=user)
        hello_tweet = hello_tweet.save()

        reply_tweet = Tweet(text="Here take it.", user=user1)
        reply_tweet = reply_tweet.save()

        reply_object = TweetReplies(tweet=reply_tweet, reply_to=hello_tweet)
        reply_object.save()