import requests
import json
import datetime
from tkinter import *
import time

api_key = "your_api_key"
pairs = "EURUSD,USDEUR"
url = "https://forex.1forge.com/1.0.3/quotes?pairs=" + pairs + "&api_key=" + api_key
