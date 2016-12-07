#!/usr/bin/env python

import argparse
import arrow
import parsedatetime
import pytz
import tzlocal


def parse_args():
    timezones = ['local', 'utc']

    ap = argparse.ArgumentParser(
        prog='whenis',
        description='Convert timestamps between UTC and local timezones.')
    ap.add_argument(
        '-f', '--from', metavar='TIMEZONE', dest='from_tz', default='utc',
        choices=timezones, help='timezone to convert from (default: utc)')
    ap.add_argument(
        '-t', '--to', metavar='TIMEZONE', dest='to_tz', default='local',
        choices=timezones, help='timezone to convert to (default: local)')
    ap.add_argument('timestamp', nargs='*', help='timestamp to be converted')

    return ap.parse_args()


def timezones(args):
    local = str(tzlocal.get_localzone())

    if args.from_tz == 'local':
        from_tz = local
    elif args.from_tz == 'utc':
        from_tz = 'UTC'

    if args.to_tz == 'local':
        to_tz = local
    elif args.to_tz == 'utc':
        to_tz = 'UTC'

    return (from_tz, to_tz)


def convert(timestamp, from_tz, to_tz):
    cal = parsedatetime.Calendar()
    datetime, status = cal.parseDT(datetimeString=' '.join(timestamp),
                                   tzinfo=pytz.timezone(from_tz))
    source_dt = arrow.get(datetime)
    target_dt = source_dt.to(to_tz)

    return target_dt.format('ddd D MMM YYYY, h:mm:ss A ZZ')


def main():
    args = parse_args()
    from_tz, to_tz = timezones(args)
    print(convert(args.timestamp, from_tz, to_tz))


if __name__ == '__main__':
    main()
