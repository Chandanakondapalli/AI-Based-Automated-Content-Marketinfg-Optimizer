import json
import tweepy
from run_prompt import execute_gemini_for_tweets

API_KEY = "AIzaSyDlkxxjJmbjAHLF3_rfb4NgNiksbMrm2yc"
API_SECRET_KEY = "181hPlUZWDRVZjYRrkHEQhZqGRv1P7PAs7G16lRuBdISsuLeZ1"
ACCESS_TOKEN = "1463363707254177792-6U7wsjGN0x8iHPNWuxRNM5ZMn1WDFI"
ACCESS_TOKEN_SECRET = "YlOVAE463M8c5rkOJ6DqiaPR1prnMIVTZQrMIwJlkZ3jt"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAANqM3gEAAAAAinuS5A1QvQGy%2Bq3RTjz4XEf%2BkDI%3D8pemVGrHZsMo6aaCoqP3cpxUboOZdYuF34waGCehquVmcA6al9"

twitterClient = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)


def create_tweet(prompt):
    """Create a tweet based on the given prompt using Gemini AI"""
    try:
        result = execute_gemini_for_tweets(prompt)
        return json.loads(result)
    except Exception as e:
        return {
            "tweet": "",
            "prediction": "error",
            "explanation": str(e)
        }


def extract_tweets_from_user(username="sundarpichai"):
    """Extract tweets from a specific Twitter user"""
    user = twitterClient.get_user(username=username)
    user_id = user.data.id
    tweets = twitterClient.get_users_tweets(user_id, max_results=50, tweet_fields=['created_at', 'public_metrics', 'text'])
    
    with open("extracted_tweets.json", "w") as json_file:
        json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    
    return tweets.data


if __name__ == "__main__":
    extract_tweets_from_user()