======
README
======

Lektor 2.3 doesn't run on Python 3, so we're using Python 2.7.

To setup development workspace:

    sudo apt-get install python-dev python-virtualenv
    virtualenv venv
    . venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt

To start server with updated html and plugins:

    . venv/bin/activate
    rm -r ~/.cache/lektor && lektor server

To run unit test:

    . venv/bin/activate
    cd packages/shwc
    python -m unittest testshwc

To build site:

    . venv/bin/activate
    ./build  # default build into ./site

Redirect rules in `assets/_redirects`.


TODO
====

- favicon.ico: http://sbg-sword-store.sword-buyers-guide.com/wordpress/wp-content/uploads/2016/04/IMG_3291.jpg
