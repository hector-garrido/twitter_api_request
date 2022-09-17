from pysentimiento import create_analyzer

# here we got a sample of tweets and arranged them in a list of dicitonaries
# with the API, we will change this and use the output of the API request instead
from news_sample import news_sample

analyzer = create_analyzer(task="sentiment", lang="es")

for news in news_sample:

    print(news["text"])
    pred = analyzer.predict(news["text"])
    print(pred.output)

    if pred.output == "POS":
        print("This is a positive tweet, it will be automatically retweeted.")
        print(f"The link of the tweet is the following: {news['link']}")
        # here we would use the API to retweet the selected tweet
    else:
        print("This is not a positive tweet, it will be ignored.")

    print("\n\n")