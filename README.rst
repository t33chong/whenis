whenis
======

**whenis** is a command-line utility that converts timestamps between
UTC and local timezones.

Installation
------------

::

    pip install whenis

Usage
-----

::

    $ whenis -h
    usage: whenis [-h] [-f TIMEZONE] [-t TIMEZONE] [timestamp [timestamp ...]]

    Convert timestamps between UTC and local timezones.

    positional arguments:
      timestamp             timestamp to be converted

    optional arguments:
      -h, --help            show this help message and exit
      -f TIMEZONE, --from TIMEZONE
                            timezone to convert from (default: utc)
      -t TIMEZONE, --to TIMEZONE
                            timezone to convert to (default: local)

    $ whenis -f utc -t local "12/7/16 1:28:36.156 AM"
    Tue 6 Dec 2016, 5:28:36 PM -08:00

    $ whenis 2016-12-07 01:28:36,156
    Tue 6 Dec 2016, 5:28:36 PM -08:00

    $ whenis -f local -t utc 6 Dec 2016, 5:28:36 PM
    Wed 7 Dec 2016, 1:28:36 AM +00:00

License
-------

`MIT <http://opensource.org/licenses/MIT>`__
