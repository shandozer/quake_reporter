#!/usr/bin/env python
"""
__author__ = Shannon T. Buckley, 10/8/16
Python 2.7.x
"""

import json
import urllib2
import datetime
import argparse


VERSION = '0.1.0'


def get_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument('-m', '--magnitude', action="store", type=float)

    parser.add_argument('-t', '--timeframe', action="store", choices=['hour', 'week', 'day', 'month'])

    return parser


def print_results(data, magnitude):

    json_data = json.loads(data)

    if 'title' in json_data['metadata']:

        print json_data['metadata']['title']

    count = json_data['metadata']['count']

    print '\n--> {} events found in the {}\n'.format(str(count), json_data['metadata']['title'].split(', ')[1])

    # print sorted(json_data['features'])

    tsunami_quakes = [quake for quake in sorted(json_data['features']) if quake['properties']['tsunami'] == 1]

    tsunami_count = len(tsunami_quakes)

    if tsunami_count > 0:
        print "\t{} of these caused TSUNAMI\n".format(tsunami_count)

    for i in sorted(json_data['features']):

        print '*' * 18 + '\n'
        if i['properties']['time']:

            local_quake_time = i['properties']['time']

            quake_date = datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=local_quake_time)
            print 'Date of Quake: {}'.format(quake_date.strftime('%m-%d-%Y %H:%M:%S'))

            time_since_quake = datetime.timedelta() - datetime.timedelta(days=-quake_date.day,
                                                                         hours=quake_date.hour,
                                                                         minutes=quake_date.minute,
                                                                         seconds=quake_date.second)

        if i['properties']['tsunami'] == 1:

            print "\n\t_/*~~~  TSUNAMI CREATED!  ~~~*\_\n"

        if i['properties']['mag']:

            print '%2.1f' % i['properties']['mag'] + ',', i['properties']['place'], '\n'

        print '*' * 20


def main():

    parser = get_parser()

    args = parser.parse_args()

    intro_statement = '\n\nSearching for Global Earthquake Events'

    if args.timeframe:

        t = args.timeframe
        intro_statement += ' within the last {}...'.format(t)

    else:
        t = 'week'

    print intro_statement

    if args.magnitude:
        mag = args.magnitude
        print '\nMagnitude requested: {}'.format(mag)

        if mag >= 4.5:

            mag = 4.5

        elif mag > 2.5:

            mag = 2.5

        else:

            mag = 1.0  # anything less than 2.5 gets the 1.0+ range
    else:

        mag = 2.5  # a medium sized default

    api_url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{}_{}.geojson'.format(mag, t)

    page = urllib2.urlopen(api_url)

    data = page.read()

    if data:

        print_results(data, mag)

if __name__ == '__main__':

    main()
