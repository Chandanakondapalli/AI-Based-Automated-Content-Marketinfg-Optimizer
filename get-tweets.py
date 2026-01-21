import tweepy


# Authenticate with Twitter API
twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

print("✅ Authentication successful!")

# Get your own user account info
me = twitterClient.get_me()
print("👤 Logged in as:", me.data.username)

# Get your last 5 tweets
tweets = twitterClient.get_users_tweets(id=me.data.id, max_results=5)

print("\n📝 Your last 5 tweets:")
if tweets.data:
    for tweet in tweets.data:
        print("-", tweet.text)
else:
    print("No tweets found.")
