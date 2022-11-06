#Gas Price Daily Tracker Scrape and Load Direct to Google Sheets Thru API
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:57:57 2022

@author: bobtr
"""
import pandas as pd
import gspread
import bs4 as bs
import datetime as dt
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from urllib.request import Request, urlopen
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

#tested in local here; add credentials json file in source tree in remote server
#credentials = Credentials.from_service_account_file('D:/OneDrive/NYIT/CSCI-665-SWE/Team1Project/gaspricetracker-365614-5f98bd64597b.json', scopes=scopes)

# now try in EC2
# This worked !@
# Moved the sheet to my main Google Acc to add in a script to generate datetime when the sheet is updated
credentials = Credentials.from_service_account_file('gaspricetracker-367021-BTreeAcct.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

#new URL for Main Google Acct
gs = gc.open_by_url('https://docs.google.com/spreadsheets/d/18-Rc4x0qOaOeZ2ASFgm0lSZXf4bf80Fzm5Q-hInB8O0/edit#gid=0')

                    
worksheet1 = gs.worksheet('GPT1')

# read the data and write to google sheets thru API 
req = Request('https://gasprices.aaa.com/state-gas-price-averages/', headers={'User-Agent': 'Mozilla/5.0'})
sauce = urlopen(req).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav
body = soup.body
text = soup.text
div = soup.div

data = []
table = soup.find('table', attrs={'class':'sortable-table tablesorter tablesorter-default tablesorter27d7549b7878e'})

table_body = soup.find('tbody')

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    
# dataframe (create or import it)
df = pd.DataFrame(data)

# add timestamp # change default UTC time to our timezone by way of pytz
# getting timezone by name
# some otions below to fix to local time:
#    NYC_tz = pytz.timezone('US/Eastern')
#    date_timeNYC = dt.datetime.now.localize(None)
#    fmt = '%m-%d %H:%M %Z%z'
#    pytz_string = NYC_tz.strftime(fmt)
#    t = [date_timeNYC for i in df.index]
#    t = [dt.datetime.now(tz=NYC_tz).dt.tz_localize(None) for i in df.index]

t = [dt.datetime.now() for i in df.index]
s = pd.Series(t, name = 'TimeStamp')
df.insert(0, 'TimeStamp', s)

set_with_dataframe(worksheet1,df,2,1,include_column_header=False)

#end - check your google sheets for data.
    