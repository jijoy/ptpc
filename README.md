# pivotal tracker point counter (ptpc)

## Overview

Some agile teams like to assign stories during sprint planning. They want to be fair - and make sure everyone has an equal load. Other teams just assign stories as they pick them up. There's no one way to do it.

Ptpc is little python tool for teams that like to assign stories up front. It looks at how many points each team member has assigned for upcoming stories. We don't want to see things people have started working on yet, only things that are assigned, unstarted and in the backlog.

## How to use it

1. Install Virtualenv
```
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
tar xvfz virtualenv-X.X.tar.gz
cd virtualenv-X.X
[sudo] python setup.py install
```

1. Clone this repo

`git clone git@github.com:jijoy/ptpc.git`

1. Change directories into

`cd ptpc`

1. Create a virtual environment

`virtualenv .`

1. Turn on the virtual environment

`source bin/activate`

1. Install requirements

`pip install -r requirements.txt`

1. Edit the config file

`vim config.py`

1. Modify as follows (note if you have [manual planning](https://www.pivotaltracker.com/blog/manual-planning-trackers-ui-api/) on or off).

```
API_KEY = '4567fdd394c2fcd24ebceb510c79d2d6'
TRACKER_PROJECT = '1930322'
USERS = ['REX','IV','DS','JD','JC','JW','BS']
MANUAL_PLANNING = False
DEBUG = False
```

1. Run the script!

```
python ptpc.py

User      Points
------  --------
rex            1
JW             0
DS             3
BS            14
```



