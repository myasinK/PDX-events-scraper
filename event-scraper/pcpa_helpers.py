import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time
import datetime
import json


def event_days( start_str, end_str ):    
    start_datetime = datetime.datetime.strptime( start_str + "/19", "%m/%d/%y" )
    end_datetime = datetime.datetime.strptime( end_str + "/19", "%m/%d/%y" )
    return ( end_datetime - start_datetime ).days 


def print_days( start_date, num_days ):
    start_date += "/19"
    dates_str = start_date
    dates_array = [ start_date ]
    for n in range( 1, num_days ):
        next_date = datetime.datetime.strptime( start_date, "%m/%d/%y" ) + datetime.timedelta(days=n)
        next_date = next_date.strftime("%m/%d/%y")
        dates_str += ( ", " + next_date )
        dates_array.append( next_date )
        #print(next_date.strftime("%m/%d/%y"))
    return dates_array, dates_str


def read_info_from_page(url, payload, events_json):    
    r = requests.get(url, params = payload)
    soup = BeautifulSoup(r.content)
    data = soup.find_all("div", {"class": "views-row"})
    check_next_page = False
    append_line = ""
    pcpa_link = "https://www.portland5.com"
    
    for each_entry in data:
        if each_entry.h3 is None:
            pass
        else: # if there are events to display
            check_next_page = True             
            event = each_entry.h3.text
            event_page = pcpa_link + each_entry.a['href'] 
            event_venue = each_entry.find("span", {"class":"field-content"}).text
            dates = each_entry.find_all("span",{"class":"date-display-single"})
            start_date = dates[0].text 
            if len( dates ) > 1: ## if there's a range of dates
                end_date = dates[1].text
                num_days = event_days(start_date,end_date)
                dates_array, all_dates = print_days(start_date, num_days)
                event_dates = all_dates                
            else: ## if show is on one day only
                event_dates = start_date + '/19'
            append_line += event + '\n' + event_venue + '\n' + event_page + '\n' + event_dates + '\n\n'
            print( append_line )    
            events_json['events'].append( { 
               'event' : event,
               'event-venue' : event_venue,
               'event-page' : event_page,
               'event-dates' : event_dates
                } )
    return check_next_page, append_line, events_json


def scrape_pcpa( file_path, events_json ):
    url = 'https://www.portland5.com/events?'
    page_num = 1    
    fopen = open( file_path, 'a', encoding='utf-8' )
    check_next_page = True
    
    while ( check_next_page ):
        payload = { "page" : str(page_num) }
        check_next_page, line, events_json = read_info_from_page( url, payload, events_json )        
        write = fopen.write(line) if len( line ) > 0 else -1
        page_num += 1 if check_next_page else 0 
    
    print( '\n\n' + "page number: " + str( page_num ) )
    fopen.close()
    return events_json
