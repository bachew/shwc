# README

Lektor 2.3 doesn't run on Python 3, so we're using Python 2.7.

To setup development workspace:

```
$ sudo apt-get install python-dev python-virtualenv
$ virtualenv -p python2 venv
$ . venv/bin/activate
(venv)$ pip install -U pip
(venv)$ pip install -r requirements.txt
```

From here onwards

To start server with updated html and plugins:

```
(venv)$ rm -fr ~/.cache/lektor && lektor server
```

To run unit test:

```
(venv)$ cd packages/shwc
(venv)$ python -m unittest testshwc
```

To build site:

```
(venv)$ ./build  # default build into ./site
```

To serve the built site:

```
(venv)$ ./serve
```

Netlify redirect rules in `assets/_redirects`.
