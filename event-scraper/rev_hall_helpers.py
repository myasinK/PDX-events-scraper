

import requests
from bs4 import BeautifulSoup
from rev_hall_helpers import *
from datetime import datetime, date, time
import datetime
import dateutil.parser

def rev_hall_events( events_json ):
    url = 'https://www.revolutionhall.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    h1 = soup.find_all("h1", {"class": "headliners summary"})
    h2 = soup.find_all("h2", {"class": "dates"})
    
    h1_event_name_list = [h1[n].text for n in range(len(h1))]
    h1_event_page_list = [url + h1[n].a['href'] for n in range(len(h1))]
    h2_event_date_list = [h2[n].text for n in range(len(h2))]

    append_line = ''
    venue = 'Revolution Hall'
    for event in range( len( h1_event_name_list ) ):
        act = h1_event_name_list[event] 
        link = h1_event_page_list[event] 
        date = dateutil.parser.parse( h2_event_date_list[event] ).strftime("%m/%d/%y") 
        if date[-2:] == '19':
            append_line += act + '\n' + venue + '\n' + link + '\n' + date + '\n\n'
            events_json['events'].append( { 
                   'event' : act,
                   'event-venue' : venue,
                   'event-page' : link,
                   'event-dates' : date
                    } )
    return append_line, events_json

def scrape_rev_hall( file_path, events_json ):
    revolution_hall_events, events_json = rev_hall_events( events_json ) 
    fopen = open( file_path, 'a', encoding='utf-8' )
    fopen.write( revolution_hall_events )
    fopen.close()
    return events_json