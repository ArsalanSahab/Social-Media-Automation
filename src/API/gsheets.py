#Module to interact with Google Sheets.

# Importing Modules
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sys 

# Setup Path
sys.path.append('/home/machine/projects/social-media-marketing-bot/src/Secrets')  
from my_secrets import POST_CONTENT_SHEET_ID
from my_secrets import SOCIAL_MEDIA_COLUMNS



"""Class for Google Sheets"""

class GSheet():
    

    """Initializer"""

    def __init__(self):
       
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.POST_CONTENT_SHEET_ID = POST_CONTENT_SHEET_ID
        self.MAIN_RANGE = 'Main!A2:S'
        self.SOCIAL_MEDIA_COLUMNS = SOCIAL_MEDIA_COLUMNS




    """Returns a service from Google Sheets."""
    def buildService(self):
       
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '~/Documents/Python/Automation/Social-Media-Automation/src/Secrets/client_secret.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()
        print('Building a service to Google Sheets.')



