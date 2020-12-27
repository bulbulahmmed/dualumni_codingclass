# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 13:16:44 2018

@author: Toluwani_Soares1
"""
#OH MY GOODNESS this took 3 hours vs the 15-20 hours I spent on MERELY JANUARY over the past 1.5 days.
import pandas as pd
from pandas import DataFrame
#import numpy as np
data = pd.read_excel('data/RenamedData.xlsx', sheet_name='datasheet', usecols=(1,2,3,5)) 
data.to_csv('data/observation.txt', sep = '\t', index=None)
data = pd.read_csv('data/observation.txt', delimiter = '\t') 
#
month = '.*-02-.*'
##SortDate=data.sort_values('Date')
monthlydata    = data[data['Date'].astype(str).str.contains(month)]
var_data       = monthlydata.groupby(['lat', 'lon']).mean().reset_index()
var_data.to_csv("data/variogram_data.csv", sep = ',', float_format='%.4f' , index=None)

#-----------------------------------------------------------------------------;
#
#-----------------------------------------------------------------------------;
'''
def get_variogramdata(inpf, mon, outf):
    data = pd.read_csv(inpf, delimiter = '\t')
    February    = data[data['Date'].astype(str).str.contains(mon)]
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
'''
