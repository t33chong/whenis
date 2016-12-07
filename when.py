#!/usr/bin/env python

import argparse
import arrow
import parsedatetime
import pytz
import tzlocal

TIMEZONES = ['local', 'utc']

ap = argparse.ArgumentParser(description='Convert timestamps between UTC and local timezone')
ap.add_argument(
    '-f', '--from', metavar='TIMEZONE', dest='from_tz', default='utc',
    choices=TIMEZONES, help='timezone to convert from')
ap.add_argument(
    '-t', '--to', metavar='TIMEZONE', dest='to_tz', default='local',
    choices=TIMEZONES, help='timezone to convert to')
ap.add_argument('timestamp', nargs='*', help='timestamp to be converted')
args = ap.parse_args()

local = str(tzlocal.get_localzone())

if args.from_tz == 'local':
    from_tz = local
elif args.from_tz == 'utc':
    from_tz = 'UTC'

if args.to_tz == 'local':
    to_tz = local
elif args.to_tz == 'utc':
    to_tz = 'UTC'

cal = parsedatetime.Calendar()
datetime, status = cal.parseDT(datetimeString=' '.join(args.timestamp),
                               tzinfo=pytz.timezone(from_tz))
source_dt = arrow.get(datetime)
target_dt = source_dt.to(to_tz)

print(target_dt.format('ddd D MMM YYYY, h:mm:ss A ZZ'))
