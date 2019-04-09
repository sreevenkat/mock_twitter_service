from models import Tweet, TweetLikes, TweetReplies

# Method checks if requested tweet exists and returns 
# tweet and it's replies or an error message
def get_tweet_and_replies(tweet_id):

    tweet = None
    error = None

    query = Tweet.objects.filter(id=tweet_id, deleted=False)
    if query.exists():
        tweet_object = query[0]
        tweet = tweet_object.get_tweet_and_replies()
    else:
        error = {"message": "Tweet not found"}

    return tweet, error


def get_tweet(tweet_id):
    return Tweet.objects.get(id=tweet_id)

def validate_tweet_payload(payload):
    errors = []
    if "text" not in payload.keys():
        errors.append({"message": "Tweet text is required."})

    if payload.get("text") == "":
        errors.append({"message": "Tweet cannot be empty."})

    if "reply_to" in payload.keys():
        try:
            reply_to = int(payload.get("reply_to"))
            
            query = Tweet.objects.filter(id=reply_to)
            if not query.exists():
                errors.append({"message": "Tweet being replied to does not exist."})

        except:
            errors.append({"reply_to": "Invalid value."})

    return errors

def get_all_tweets():

    query = Tweet.objects.filter(deleted=False).order_by('-created_at')[:20]

    result = []

    for record in query:
        data = {
            "text": record.text,
            "id": record.id,
            "user": {
                "first_name": record.user.first_name,
                "last_name": record.user.last_name
            }
        }

        result.append(data)

    return result

def create_tweet(payload, user):

    errors = validate_tweet_payload(payload)
    new_tweet = None

    if not errors:
        new_tweet = Tweet(text=payload.get("text"), user=user)
        new_tweet.save()

        if payload.get("reply_to", None):
            tweet_being_replied_to = get_tweet(payload.get("reply_to"))
            reply_to = TweetReplies(tweet=new_tweet, reply_to=tweet_being_replied_to)
            reply_to.save()

    return new_tweet, errors