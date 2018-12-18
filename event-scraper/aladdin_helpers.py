
from datetime import datetime, date, time, timedelta
import datetime
import requests
from bs4 import BeautifulSoup

def aladdin_events( events_json ):
    url = 'https://www.aladdin-theater.com/listing/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    h1 = soup.find_all("h1", {"class": "headliners summary"})
    h2 = soup.find_all("h2", {"class": "dates"})
    
    h1_event_name_list = [h1[n].text for n in range(len(h1))]
    h1_event_page_list = [url + h1[n].a['href'] for n in range(len(h1))]
    h2_event_date_list = [h2[n].text for n in range(len(h2))]

    append_line = ''
    venue = 'Aladdin Theater'
    for event in range( len( h1_event_name_list ) ):
        act = h1_event_name_list[event] 
        print(act)
        link = h1_event_page_list[event] 
        date_unformatted = h2_event_date_list[event] 
        print( date_unformatted )
        # if correct format add info to append_line
        if date_unformatted.find('/') == -1:
            date_formatted = datetime.datetime.strptime( date_unformatted + ",19", "%a,%b,%d,%y" ).strftime("%m/%d/%y")
            if date_formatted[0:2] == '12':
                continue
            else:
                append_line += act + '\n' + venue + '\n' + link + '\n' + date_formatted + '\n\n' 
                events_json['events'].append( {
                   'event' : act,
                   'event-venue' : venue,
                   'event-page' : link,
                   'event-dates' : date_formatted
                   } )
    return append_line, events_json

def scrape_aladdin( file_path, events_json ):
    aladdin_theater_events, events_json = aladdin_events( events_json )
    print(aladdin_theater_events)
    fopen = open( file_path, 'a', encoding='utf-8' )
    fopen.write( aladdin_theater_events )
    fopen.close()
    return events_json