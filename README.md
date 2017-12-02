# quake_datafeed.py
Gathers global quake (and tsunami) information and presents to user.

## Version 0.2.1
Provides sorted results (descending time order) and prints depth info.
## Version 0.2.0
Lets you save the json data from your request.
## Version 0.1.0
Prints unsorted results to console for magnitudes **m** and above

## Optional Flags
`-m <magnitude: 1.0, 2.5, or 4.5>`
_(default: 2.5+)_

Input a minimum magnitude filter for your requested data. (Constraints imposed by usgs.gov's api)

`-t <time frame desired: hour, day, week, or month>` 
_(default: 'week')_

Enter the span of time over which you want to collect quake data. 

`-s` 

Use this flag to save a .json file containing the data from your request.
