
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime, date, time, timedelta
import datetime

def wonder_events( events_json ):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path = 'C:\\Users\\Yasin\\Downloads\\chromedriver.exe', chrome_options=chrome_options)
    driver.get('https://www.wonderballroom.com/event/1745386-english-beat-portland/')
    headliners = driver.find_elements_by_class_name("headliners")
    venue = "Wonder Ballroom"
    append_line = ""

    for n in range( 0, len(headliners) - 1 ): 
        link = headliners[n].find_elements_by_tag_name("a")[0].get_attribute("href")
        date_and_event = headliners[n].find_elements_by_tag_name("a")[0].text
        month_slash_day = date_and_event.partition(" ")[0]
        date_formatted = datetime.datetime.strptime( month_slash_day + "/19", "%b/%d/%y" ).strftime("%m/%d/%y")
        event = date_and_event.partition(" ")[2]
        if date_formatted[0:2] == '12':
            continue
        else:
            append_line += event + "\n" + venue + "\n" + link + "\n" + date_formatted + "\n\n"
            events_json['events'].append( {
                'event' : event,
                'event-venue' : venue,
                'event-page' : link,
                'event-dates' : date_formatted
                } )
    return append_line, events_json



def scrape_wonder_ballroom( file_path, events_json ):
    wonder_ballroom_events, events_json = wonder_events( events_json )
    fopen = open( file_path, 'a', encoding='utf-8' )
    fopen.write( wonder_ballroom_events )
    fopen.close() 

    return events_json

