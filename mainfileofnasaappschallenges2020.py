#The dataset which were given is in here:

#Indented block

#ftp://data.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/MOPITT/2020/MOP02J-20200322-L2V18.0.3.csv

#you can save and then upload this file in the next step.

from google.colab import files
uploaded = files.upload()


#reading the data:
import pandas as pd
import io
df = pd.read_csv(io.StringIO(uploaded['data.csv'].decode('utf-8')), sep = ',')
df

#Extracting columns which we need from dataset, which are included of: Latitude, Longitude, CO total, and surface temperature. 
#We keep the first two ones, ask the user to enter their own latitude and longitude. 
#Then if it matches, the system will return the CO total measure and the Surface temperature of that particular point (with provided those latitude and longitude from user).

df[' Longitude']
df[df.columns[1]]

latlist = list(df[df.columns[0]])
longlist = list(df[df.columns[1]])

for i, j in zip(latlist, longlist):
  s.append([i,j])

print(s)


df[df.columns[0:2]]

lat,long = df[df.columns[0:2]]

COTotalColumn = df[df.columns[2]]
COTotalColumn

COMR_Surface = df[df.columns[3]]
COMR_Profile = df[df.columns[4:-1]]
RetrievedSurfaceTemperature = df[df.columns[-1]]
pip install matplotlib
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
import numpy as np


userlat, userlong = input("Enter latitude: "), input("Enter longitude: ") 


l = df[' Longitude']


k = df['RetrievedSurfaceTemperature ']


m = df[' COTotalColumn']


if userlat in df['# Latitude']:
  if userlong in df[' Longitude']:
    print(k[userlat], m[userlat])
    
    
    
  
  
  
