from confluent_kafka import Producer
import json
import time
import logging
import os
import sys
from dotenv import load_dotenv
import tweepy

load_dotenv()
bearer_token = os.environ.get('BEARER_TOKEN')
word_to_track = sys.argv[1]

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

p=Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():

    client = tweepy.Client(bearer_token)
    tweets = client.search_recent_tweets(query=word_to_track, 
                                        tweet_fields=['author_id', 'created_at', 'text', 'lang'],
                                        max_results = 100)
    
    for tweet in tweets.data:
        data={
                'author_id':tweet.author_id,
                'created_at': tweet.created_at,
                'id': tweet.id,
                'lang':tweet.lang,
                'text':tweet.text
            }
        m=json.dumps(data, default=str)
        p.poll(1)
        p.produce(sys.argv[2], m.encode('utf-8'),callback=receipt)
        p.flush()
        time.sleep(3)
        
if __name__ == '__main__':
    main()