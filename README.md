# Mock Twitter Service

## Setup

Run `make build` to get the app running to localhost:8000

There are 2 users created by default:

User 1 
  
  username: sree-venkat
  password: hello
  
User 2 

  username: siva-shankar
  password: hello

Api:

POST /login/

Payload:
```
{
  "username": "sree-venkat"
  "passowrd: "hello"
}
```

GET /logout/

GET /tweet/<tweet id>/
  
POST /post-tweet/

```
{
  "text": "<Tweet contents>",
  "reply_to": <id of the tweet you're replying to if you're replying to it>
}
```

GET /tweets/


/post-tweet/ expects session_id in the cookies as follows:

session_id= "cookiestring"
