#! usr/bin/env python
# *-- coding : utf-8 --*

import tweepy
import codecs

class ExtractAuthFeatures(object):

    debug = False

    def __init__(self):
        self.consumer_key = "omFBeHFvgvWoEmadTvH7WAJQz"
        self.consumer_secret = "HZAQjfWoJu1ByNVo8nCav3ARgFCKOGWpObosoPqa0FYRwVonYm"
        self.access_token = "4508853492-zg2va8tJITgeZzzNsGGJkcncIZCErNvbCg21mT9"
        self.access_token_secret = "lUikDtvcQHgoCKTnb6paaNtay4u6QqkJS55ytBu6epnZH"
        self.url_domain = []

    def get_tweets_by_user(self, keyword):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return tweepy.Cursor(api.user_timeline, screen_name=keyword).items()

    def get_tweets_by_query(self, keyword, max_tweets):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return tweepy.Cursor(api.search, q=keyword).items(max_tweets)


def main():
    twit_obj = ExtractAuthFeatures()
    # tweets = twit_obj.get_tweets_by_user('@fsgoodnews')
    # with codecs.open('../scrap_data/good_news', 'w', 'utf-8') as scr_fileobj:
    #     for each_tweet in tweets:
    #         scr_fileobj.write(each_tweet._json['text'] + '\n')
    query = '#badnews'
    max_tweets = 3000
    bad_tweets = twit_obj.get_tweets_by_query(query, max_tweets)
    with codecs.open('../scrap_data/bad_news', 'w', 'utf-8') as scr_fileobj2:
        for each_tweet in bad_tweets:
            scr_fileobj2.write(each_tweet._json['text'] + '\n')


if __name__ == '__main__':
    main()


