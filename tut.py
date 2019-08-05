import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part,whole):
    return 100 * float(part)/float(whole)

consumer_key = "FcWCZYxZk5HGAtrTi6XM4NWWB"
consumer_secret = "DpDhjGNEjiutESduvKQGRq0NVzOxverV7yGaowM1N0EKPtLypL"

access_token = "2609369311-oNLh2N8K53xTScHTRCaFZptRFWsavFbs2f1n1Kl"

access_token_secret = "2zOgJ71ik56VEY1C8yrbqyBC6gUoWsI6ogrVHQYJRNUkJ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

positive = 0
negative = 0
neutral = 0
polarity = 0
searchTerm = input("Enter the term to be searched: ")
noOfTerms = int(input("enter the number of terms to be searched: "))
tweets = tweepy.Cursor(api.search, q =searchTerm).items(noOfTerms)


for tweet in tweets:
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity+= analysis.sentiment.polarity

    if(analysis.sentiment.polarity == 0):
        neutral+= 1
    elif(analysis.sentiment.polarity >0):
        positive += 1
    elif(analysis.sentiment.polarity <0):
        negative +=1

positive = percentage(positive, noOfTerms)
negative = percentage(negative, noOfTerms)
neutral = percentage(neutral,noOfTerms)

positive = format(positive,'.2f')
negative = format(negative,'.2f')
neutral = format(neutral,'.2f')


print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfTerms) + " tweets.")

if(polarity == 0):
    print("neutral")
elif(polarity>0):
    print("Positive")
elif(polarity<0):
    print("negative")

labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]']

sizes = [positive,negative,neutral]
colors = ['yellowgreen','red','gold']
patches, text = plt.pie(sizes,colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfTerms) + ' Tweets.')
plt.axis('equal')
plt.show()


