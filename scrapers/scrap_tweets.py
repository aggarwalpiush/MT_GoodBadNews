#! usr/bin/env python
# *-- coding : utf-8 --*

import tweepy
import codecs


class ExtractAuthFeatures(object):

    debug = False

    def __init__(self):
        self.consumer_key = "fWpDVeJaGr3QRSVBvLal25HLF"
        self.consumer_secret = "YbfqCFoC9yqfwmedq4XYMnbH1PrWBpsNlWNUYyzX87iKJKRsCZ"
        self.access_token = "4508853492-lq0VCRdPWCMuO8ewhQjVbZhSVfSNxhk5oPXaWB8"
        self.access_token_secret = "1IPWk2uZhhldozhzJKAnenSvSaD6SmrWRzpjgBE4xuw9M"
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

    def get_tweets_by_id(self, id_of_tweet):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api.get_status(id_of_tweet)




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


