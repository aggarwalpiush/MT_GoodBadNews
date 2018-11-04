# !usr/bin/env python
# *-- coding : utf-8 --*

import sys
import logging
import argparse
import codecs
import scrap_tweets


def parse(argv, desc):
    parser = argparse.ArgumentParser(description= desc)
    parser.add_argument('-i', '--input_file', type=str, help=
                        "input_file contains tweets ids")
    parser.add_argument('-o', '--output_file', type=str, help=
                        "output path where tweets text need to save")
    return parser.parse_args(argv)


def main():
    args = parse(sys.argv[1:], "collect tweets from id")
    formt = "%(asctime)s %(levelname)s : %(message)s"
    logging.basicConfig(format=formt)
    logging.getLogger().setLevel(logging.INFO)
    st = scrap_tweets.ExtractAuthFeatures()
    with codecs.open(args.output_file, 'w', 'utf-8') as outf:
        with codecs.open(args.input_file, 'r', 'utf-8') as inf:
            for t_id in inf:
                try:
                    if isinstance(int(t_id), int):
                        logging.info("getting tweets for id %s\n", t_id)
                        tweet = st.get_tweets_by_id(int(t_id.strip()))
                        outf.write("%s\t%s\n" %(t_id.strip(), tweet.text))
                except ValueError:
                    continue


if __name__ == '__main__':
    main()



