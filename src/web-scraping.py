# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XhwhDBczZQI')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id = 'seven-day-forecast-body')
print(week)

print(week.find_all('li'))
print(week.find_all(class_ = 'forecast-tombstone'))
item = week.find_all(class_ = 'tombstone-container')
print(item[1])
#Now put all of the Day, Short Desc into cols
item[0].find(class_ = 'period-name')

print(item[0].find(class_ = 'period-name').get_text()) #get only the text
print(item[0].find(class_ = 'short-desc').get_text()) #get the next class
print(item[0].find(class_ = 'temp').get_text())

#Collect all these infos in a list, and put them into a for loop
period_names = [item.find(class_ = 'period-name').get_text() for item in item]
short_desc = [item.find(class_ = 'short-desc').get_text() for item in item]
temp = [item.find(class_ = 'temp').get_text() for item in item]
print(period_names)
print(short_desc)
print(temp)

weather_stuff = pd.DataFrame(
    {'Period' : period_names,
    'Short Desc': short_desc,
    'Temperature': temp,})
print(weather_stuff)

# use 'to_csv' to make spreadsheet (CSV file)
