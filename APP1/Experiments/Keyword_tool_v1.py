import time
import urllib
import os
import datetime
import logging
# from sqlalchemy import create_engine
import argparse
from datetime import date, datetime, timedelta
from datetime import date
# from dateutil.relativedelta import relativedelta
import datetime
# from functools import reduce
import requests
import openpyxl
import pandas as pd
import numpy as np
import json
import re, string


keywords_df = pd.read_excel(r"C:\Users\yogesh.kharat\OneDrive - Marico Ltd\Documents\Yogesh\Trendspotting_Code_New\config\config_v1.xlsx",sheet_name="Seed Keywords")
credentials = pd.read_excel(r"C:\Users\yogesh.kharat\OneDrive - Marico Ltd\Documents\Yogesh\Trendspotting_Code_New\config\config_v1.xlsx",sheet_name="API credentials")
payload_df = pd.read_excel(r"C:\Users\yogesh.kharat\OneDrive - Marico Ltd\Documents\Yogesh\Trendspotting_Code_New\config\config_v1.xlsx",sheet_name="payload_info")

