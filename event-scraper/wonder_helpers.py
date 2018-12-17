
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime, date, time, timedelta
import datetime

def wonder_events():
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
        date_formated = datetime.datetime.strptime( month_slash_day + "/19", "%b/%d/%y" ).strftime("%m/%d/%y")
        event = date_and_event.partition(" ")[2]
        if date_formated[0:2] == '12':
            continue
        else:
            append_line += event + "\n" + venue + "\n" + link + "\n" + date_formated + "\n\n"

    return append_line



def scrape_wonder_ballroom(file_path):
    wonder_ballroom_events = wonder_events()
    fopen = open( file_path, 'a', encoding='utf-8' )
    fopen.write( wonder_ballroom_events )
    fopen.close() 

    return

