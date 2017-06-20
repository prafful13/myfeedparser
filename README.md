# myfeedparser

### Usage

One needs to add some rss feeds before browsing.

`$ python feed.py <RSS-LINK>`

- browse latest feed from the single link `<RSS-LINK>` provided.
- e.g. `$ python feed.py https://news.ycombinator.com/rss`

`$ feed -b`

- browse and select from feeds already added

### Features (what you can do?)

- List feeds from different sources (stored in your library).
- Jump to (optionally) the source page of a feed in default browser.
- Store new RSS URLs in allfeeds.db.


### Help
See `$ python feed.py -h` for detailed usage.

### Installation

Download zip file or clone the repository $ git clone https://github.com/prafful13/myfeedparser.git && cd myfeedparser

Create virtual environment $ virtualenv -p /usr/bin/python2.7 env

Activate the virtual environment $ source env/bin/activate

Install dependencies $ pip install -r requirements.txt

#### Dependencies

- [feedparser](https://pypi.python.org/pypi/feedparser)


### Author

- Prafful Mehrotra
