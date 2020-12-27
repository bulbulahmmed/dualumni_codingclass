# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:16:44 2018

@author: Toluwani_Soares1
"""
#OH MY GOODNESS this took 3 hours vs the 15-20 hours I spent on MERELY JANUARY over the past 1.5 days.
import pandas as pd
from pandas import DataFrame
#import numpy as np
data = pd.read_excel('RenamedData.xlsx', sheet_name='complete', usecols=(2,3,4,9)) 
#data.to_csv('observation.txt', sep = '\t', index=None)
#data = pd.read_csv('observation.txt', delimiter = '\t') 
#
##SortDate=data.sort_values('Date')
##
###hello=data['Date'].str.contains("*-02-*")
##hello=data['Date'].str.contains(".*-02-.*") #named a series "hello", called on the column titled Date in the data Dataframe and told it to find a string containing -02- the .* is the wildcared regex function, anything can be in the place of a wildcard.
##
##February = hello.where(hello=='TRUE')
#February    = data[data['Date'].str.contains('.*-01-.*')]
##sorted_val  = February.sort_values(['lat', 'lon'], ascending=[True, True])
#
#grp = pd.concat(g for _, g in February.groupby("lat") if len(g) > 1) #https://stackoverflow.com/questions/14657241/how-do-i-get-a-list-of-all-the-duplicate-items-using-pandas-in-python FOR FUTURE REFERENCE
#
##df.groupby('sample_id', as_index=False).mean()  # Calculates mean of groupby values
#
#var_data  = February.groupby(['lat', 'lon']).mean().reset_index()
#
##hi= pd.concat(g for _, g in February.groupby(['lat', 'lon']).mean() if len(g)>1)
#
#var_data.to_csv('variogram_data_jan.txt', sep = '\t', float_format='%.4f' , index=None)

#-----------------------------------------------------------------------------;
#
#-----------------------------------------------------------------------------;

def get_variogramdata(inpf, mon, outf):
    data = pd.read_csv(inpf, delimiter = '\t')
    February    = data[data['Date'].str.contains(mon)]
    var_data  = February.groupby(['lat', 'lon']).mean().reset_index()
    var_data.to_csv(outf, sep = '\t', float_format='%.4f' , index=None)
    
    
get_variogramdata('observation.txt', '.*-01-.*', 'variogram_data_jan.txt')
get_variogramdata('observation.txt', '.*-02-.*', 'variogram_data_feb.txt')
get_variogramdata('observation.txt', '.*-03-.*', 'variogram_data_mar.txt')
get_variogramdata('observation.txt', '.*-04-.*', 'variogram_data_apr.txt')
get_variogramdata('observation.txt', '.*-05-.*', 'variogram_data_may.txt')
get_variogramdata('observation.txt', '.*-06-.*', 'variogram_data_jun.txt')
get_variogramdata('observation.txt', '.*-07-.*', 'variogram_data_july.txt')
get_variogramdata('observation.txt', '.*-08-.*', 'variogram_data_aug.txt')
get_variogramdata('observation.txt', '.*-09-.*', 'variogram_data_sep.txt')
get_variogramdata('observation.txt', '.*-10-.*', 'variogram_data_oct.txt')
get_variogramdata('observation.txt', '.*-11-.*', 'variogram_data_nov.txt')
get_variogramdata('observation.txt', '.*-12-.*', 'variogram_data_dec.txt')

