#!/usr/bin/python

import sys
from newspaper import Article, Config, nlp

def main(argv):
    if len(argv) > 1:
        htmlist = argv[1]
    else:
        htmlist = 'htmlist'

    # Our permanent config for html cleaning
    config = Config()
    config.language = 'id'
    config.MIN_SENT_COUNT = 20
    config.memoize = False
    config.fetch_images = False
    config.verbose= True

    cleaner = Article(url='', config=config)

    with open(htmlist, 'r') as f:
        htmfile = f.read().split('\n')

    raw = []

    for htm in htmfile:
        print (htm)
        if not htm.endswith("rss.html"):
            with open(htm, 'r') as f:
                h = f.read()

            cleaner.set_html(h)
            cleaner.parse()
            sentences = nlp.split_sentences(cleaner.text)
            #raw.append(sentences])
        
            with open('htm-out', 'a') as f:
                [f.write(r + '\n') for r in sentences]

if __name__ == "__main__":
    main(sys.argv)

