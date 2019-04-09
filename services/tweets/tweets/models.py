from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import json

class Tweet(models.Model):

    text = models.CharField(max_length=280)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def get_tweet_and_replies(self):
        tweet = {
            "text": self.text,
            "user": {
                "first_name": self.user.first_name,
                "last_name": self.user.last_name
            },
            "replies": self.get_tweet_replies()
        }

        return tweet

    def get_tweet_replies(self):
        tweet_replies = TweetReplies.objects.filter(reply_to=self, deleted=False).order_by('-created_at')[:5]

        replies = []

        for reply in tweet_replies:
            tweet_data = {
               "text": reply.tweet.text,
                "user": {
                    "first_name": reply.tweet.user.first_name,
                    "last_name": reply.tweet.user.last_name
                }
            }

            replies.append(tweet_data)

        return replies
    


class TweetReplies(models.Model):

    tweet = models.ForeignKey('Tweet', null=True, related_name="reply_tweet")
    reply_to = models.ForeignKey('Tweet', null=True, related_name="reply_to_tweet")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False)

class TweetLikes(models.Model):

    tweet = models.ForeignKey('Tweet')
    liked_by = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted = models.BooleanField(default=False)