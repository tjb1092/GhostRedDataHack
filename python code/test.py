#SOFTWARE OVERVIEW

#This script will query the provided SQL server for categorical data
#    and numerical stats related to the device performance
#The numerical stats are processed into a single HealthStat
#   and output to a CSV to be plugged into a web app

import sqlite3
from sklearn import linear_model
import pandas as pd
conn = sqlite3.connect('C:\\Users\\Jacob\\Desktop\\GE\\art-of-data-api\\art-of-data-api\\db.sqlite3') 
c = conn.cursor()
df = pd.read_sql("Select a.name app_name, a.business business, d.name  d_name, d.location location, s.cpu_capcity cpu_cap, s.cpu_usage_mhz cpu_usage_mhz, s.cpu_usage_percent cpu_usage_p, s.mem_capacity_provisioned mem_cap, s.mem_usage mem_usage FROM api_applicationgroup a, api_device d, api_devicestat s WHERE a.name = d.application_id AND d.name = s.device_id limit 1000;",conn)
print df
import numpy as np
fields = ['app_name', 'business', 'd_name', 'location', 'cpu_cap', 'cpu_usage_mhz', 'cpu_usage_p', 'mem_cap', 'mem_usage']
columns = ['app_name', 'business', 'd_name', 'location', 'HS','cpu_percent', 'mem_percent']
HSdf = pd.DataFrame(columns=columns, index = range(0,len(df))) #DF that holds output CSV data including health stat
HSdf['cpu_percent'] = df.cpu_usage_p
corrs = df.corr() #perform correlation coefficient matrix on numerical stats
corrs.fillna(0.0, inplace=True)
print corrs 
coefs = corrs['cpu_usage_p'] # pulls the corr coefs related to cpu usage
coefs +=1
print coefs.divide(2)

#Normalize cpu_cap, cpu_usage_mhz, cpu_usage_p, mem_cap, mem_usage columns to prepare for HS equation
for column in range(4,9):
    df[fields[column]] = df[fields[column]] - df[fields[column]].min()
    df[fields[column]] = df[fields[column]].divide(df[fields[column]].max()-df[fields[column]].min())
    df[fields[column]].multiply(coefs[fields[column]])
df.fillna(0.5, inplace=True)

#pass through SQL data and calcuated stats
HSdf['app_name'] = df['app_name']
HSdf['business'] = df['business']
HSdf['d_name'] = df['d_name']
HSdf['location'] = df['location']
HSdf['HS'] = df['cpu_cap']+df['cpu_usage_mhz']+df['cpu_usage_p']+df['mem_cap']+df['mem_usage']
HSdf['HS'] = HSdf['HS'].divide(4)
HSdf['mem_percent'] = df.mem_cap/df.mem_usage

#attempt at averaging HS based on dev name   
#HSdict = dict()
#for row in range(0,len(HSdf)):
#    d_all = my_map[HSdf['d_name']]
#    
#    if HSdict.has_key(dall):
#        d_all.append(HS)
#    else
#       d_all = []
    
HSdf.to_csv('testOutput')
