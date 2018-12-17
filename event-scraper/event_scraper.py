
from pcpa_helpers import *
from wonder_helpers import *
from aladdin_helpers import *
from rev_hall_helpers import *


file_path = 'C:\\xampp\\htdocs\\all_events.txt'

scrape_pcpa( file_path )

scrape_aladdin( file_path )

scrape_rev_hall( file_path )

scrape_wonder_ballroom( file_path )


