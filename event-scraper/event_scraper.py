
from pcpa_helpers import *
from wonder_helpers import *
from aladdin_helpers import *
from rev_hall_helpers import *


file_path = 'C:\\xampp\\htdocs\\all_events.txt'
json_path = 'C:\\xampp\\htdocs\\events-json.txt'

events_json = {}
events_json['events'] = []

scrape_pcpa( file_path, events_json )

scrape_aladdin( file_path, events_json )

scrape_rev_hall( file_path, events_json )

# Uses selenium
scrape_wonder_ballroom( file_path, events_json )

with open(json_path, 'a') as json_file:
    json.dump( events_json, json_file )
