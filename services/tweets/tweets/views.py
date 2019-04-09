# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from models import Tweet, TweetLikes
import tweet_helper

import json

# Create your views here.

def index(request):
    return HttpResponse("Hey, there. You've found your way :) .")

@csrf_exempt
def login_view(request):

    if request.method != 'POST':
        return HttpResponse("Method not supported", status=405)
    data = json.loads(request.body)
    username = data.get("username", None)
    password = data.get("password", None)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        result = {
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "session_id": request.session.__dict__["_SessionBase__session_key"]
            }
        }
        return HttpResponse(json.dumps(result), status=200, content_type="application/json")
    errors = {
        "errors": [{"message": "Invalid user/password"}]
    }
    return HttpResponse(json.dumps(errors), status=400, content_type="application/json")

@csrf_exempt
def logout_view(request):

    logout(request)

    return HttpResponse("ok", status=200)


def get_all_tweets(request):

    if request.method != 'GET':
        error_message = {"message": "Method not supported."}
        return HttpResponse(json.dumps(error_message), status=405, content_type="application/json")

    result = tweet_helper.get_all_tweets()

    return HttpResponse(json.dumps(result), status=200, content_type="application/json")

def get_tweet(request, pk):
    if request.method != 'GET':
        error_message = {"message": "Method not supported."}
        return HttpResponse(json.dumps(error_message), status=405, content_type="application/json")

    tweet, error_message = tweet_helper.get_tweet_and_replies(pk)
    if error_message:
        return HttpResponse(json.dumps(error_message), status=400, content_type="application/json")

    return HttpResponse(json.dumps(tweet), status=200, content_type="application/json")


@csrf_exempt
def post_tweet(request):
    if request.method != 'POST':
        error_message = {"message": "Method not supported."}
        return HttpResponse(json.dumps(error_message), status=405, content_type="application/json")

    if not request.user.is_authenticated():
        return HttpResponse(json.dumps({"Not Authorised.Please login.",}), status=401, content_type="application/json")

    payload = json.loads(request.body)

    tweet, error_message = tweet_helper.create_tweet(payload, request.user)
    if error_message:
        return HttpResponse(json.dumps(error_message), status=400, content_type="application/json")

    return HttpResponse(json.dumps({"id":tweet.id, "message": "success"}), status=200, content_type="application/json")