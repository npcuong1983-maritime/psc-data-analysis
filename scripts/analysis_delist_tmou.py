import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import pytz
import camelot
from datetime import datetime
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd
from pandas.tseries.frequencies import to_offset
from pypdf import PdfReader
from pdf2image import convert_from_path
import seaborn as sns
import fitz
from PIL import Image
import pytesseract
data = pd.read_csv("C:/Users/PROBOOK/OneDrive/Python/maritime_research/psc_detention_project/data/detlist_2026.csv", dtype=str)
#print(data.head)
cols = ["IMO No.", "Ship Name",	"Ship Flag", "Year of build", "Gross Tonnage","Ship Type","Classification society","Related ROs",	"Company",	"Place of detention",	"Date of detention",	"Date of release", "Nature of deficiencies"]
data[cols] = data[cols].ffill()# Forward fill merged cell exported from Excel
print(data.groupby("IMO No.").size())# Number of detention grounds per ship
print(data.groupby("Ship Flag")["IMO No."].nunique()) # Number of detained ships by flag state
print(data.groupby("IMO No.")["Nature of deficiencies"].apply(list)) # List of detention grounds for each detained ship
print(data.groupby("Nature of deficiencies")["IMO No."].nunique().sort_values(ascending=False)) # Ranking detention grounds by number of detained ship
data["Def_code"]= (data["Nature of deficiencies"].str.split("-").str[0].str.strip()) # Extract deficiency code
ranking = (data.groupby("Def_code")["IMO No."].nunique().sort_values(ascending=False)) # Ranking deficiency codes by number of detained ships
#plt.xlabel("Deficiency code")
#plt.ylabel("Number of detained ships")
#plt.title("Top 20 detention grounds")
#plt.tight_layout()
#plt.show()