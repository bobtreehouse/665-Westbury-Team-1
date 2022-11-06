from __future__ import print_function
from flask import Flask
import os.path
import pandas as pd
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import gspread
from chartStudioAPIconfig import api_key_Chart_Studio
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from urllib.request import Request, urlopen

scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

# tested in local here; add credentials json file in source tree in remote server
# credentials = Credentials.from_service_account_file('D:/OneDrive/NYIT/CSCI-665-SWE/Team1Project/gaspricetracker-365614-5f98bd64597b.json', scopes=scopes)

# now try in EC2
# This worked !@!
# Moved the sheet to main Google Acc to add in a script to generate datetime when the sheet is updated

credentials = Credentials.from_service_account_file('gaspricetracker-367021-BTreeAcct.json', scopes=scopes)

gc = gspread.authorize(credentials)

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

# new URL for Main Google Acct

gs = gc.open_by_url('https://docs.google.com/spreadsheets/d/18-Rc4x0qOaOeZ2ASFgm0lSZXf4bf80Fzm5Q-hInB8O0/edit#gid=0')

# tell it to use Worksheet 1 (renamed to GPT1)                    
worksheet1 = gs.worksheet('GPT1')

# assign a veriable to spreadsheet name and range of cells

GasPriceTracker_SPREADSHEET_ID = '18-Rc4x0qOaOeZ2ASFgm0lSZXf4bf80Fzm5Q-hInB8O0'

GasPriceTracker_RANGE_NAME = 'GPT1!A1:G52'

service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=GasPriceTracker_SPREADSHEET_ID,
                            range=GasPriceTracker_RANGE_NAME).execute()
values = result.get('values', [])

##############################################

# !! Now here below we are Passing the Data from the Google Sheets Spreadsheet by way of the API into the Pandas Dataframe (df) !! 

############################################## 

data = values

headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)

# Uncomment below in test environment to print results to console.
# Comment out the below lines for Production deployment as we do not need to print to the console.

# print(df.head())
# print(df)

# Below uses elements of the Pandas dataframe to pass to the Chorpleth Heat Map from the Plotly Library andd populate it
# Much trial and error was required to discover the Plotly map feature requires used of 'two-letter' state codes
# Additionally the gas prices need to be populated as Floats not String (so no dollar sign $) for use in the chart to create the gradations of color.

# This line below will take column headers from the dataframe and use as labels in the "hover" feature so here we pass them as Strings

df['text'] = "State: " + df['State'] + ": Regular $" + df['Regular'].astype(str)  + " Mid-Grade $" + df['Mid-Grade'].astype(str) + " Premium $" +  df['Premium'].astype(str) + " Diesel $" + df['Diesel'].astype(str) + "<br>Timestamp: " + df['Timestamp'].astype(str)  

# This is the contruction of the Plotly Heatmap or "Choropleth" map

fig = go.Figure(data=go.Choropleth(
    locations=df["StateCode"],
    z=df["Regular"],
    locationmode='USA-states',
    colorscale='Reds',
    
    # in the local version we rotated the legend to horizontal and placed below but this was not an option when hosting the chart in the Chart-Studio site associated with Plotly 
    
    #colorbar_title="Avg. Price per Gallon of Regular-grade",
    #colorbar={"orientation": "h", "x": 0.5, "y": 0.1},

    text=df["text"],)

)

# make space for explanation / annotation
fig.update_layout(margin=dict(l=20, r=5, t=0, b=40),paper_bgcolor="LightSteelBlue",autosize=True)

fig.update_layout(font_family="calibri")

fig.update_layout(
    autosize=False,
    width=1000, height=710,
    #title_text='<br><br>USA Daily Gas Price Tracker - Averages By State<br>Hover on the State to display the latest daily prices of Regular, Mid-Grade, Premium and Diesel <br>The hover text also includes a timestamp denoting when the data was written to the server',
    title_text='<br><br>USA Daily Gas Price Tracker - Averages By State', title_x=0.5,
    geo_scope='usa',
)


# Run the Plotly Graph

fig.show()

# Now connect and Push this to Chart-Studio where we host the plotly chart: 

username = 'bobtreehouse' # your username
api_key = api_key_Chart_Studio

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

#below line connects and pushes the Chart where we then generate an iframe and embed into our Azure front-end:

py.plot(fig, filename = 'USA_Gas_Price_Heatmap', auto_open=False)

# end

