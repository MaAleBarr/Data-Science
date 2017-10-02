#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:24:01 2017

@author: mariaalejandrabarrios

------------------------------------------------------------------------------
                          Class Description
------------------------------------------------------------------------------
- Funtions used for NYC Taxi data analysis 
------------------------------------------------------------------------------
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

class ListTable(list):
    """ Overridden list class which takes a 2-dimensional list of 
        the form [[1,2,3],[4,5,6]], and renders an HTML Table in 
        IPython Notebook. """
    
    def _repr_html_(self):
        html = ["<table>"]
        for row in self:
            html.append("<tr>")
            
            for col in row:
                html.append("<td>{0}</td>".format(col))
            
            html.append("</tr>")
        html.append("</table>")
        return ''.join(html)


class Taxi(object):
    
    def __init__(self):
        pass
    
    def pivotPrint(self, df, col, val):
        #create table, set header
        table=ListTable()
        df2 = df.pivot(columns = col, values = val)
        table.append(list(df2))
        df2 = pd.concat([df2[col].sort_values().reset_index(drop=True) 
            for col in df2], axis=1, ignore_index=True)
        #iterate through rows and print 
        rowLen = len(df2.ix[0].tolist())
        for i in range(len(df2)):
            if None in df2.ix[i].tolist():
                tally = [1 for f in df2.ix[i].tolist() if f is None ] 
                tally = sum(tally)
                if tally == rowLen:
                    break
                else:
                    table.append(['' if f is None else f for f in df2
                           .ix[i].tolist()])
            else: 
                table.append(df2.ix[i].tolist())         
        return table
    
    def MonthlyTraffic(self, df1, df2, df3, Labels, field, ylabel, flag):
        if flag =='cnt-percent':
            if field == 'passenger_count':
                df1n = df1.groupby([lambda x: x.month, 'passenger_count'] )['dropoff_latitude'].count().to_frame(name='cnt').reset_index()
                df2n = df2.groupby([lambda x: x.month, 'passenger_count'] )['dropoff_latitude'].count().to_frame(name='cnt').reset_index()
                df3n = df3.groupby([lambda x: x.month, 'passenger_count'] )['dropoff_latitude'].count().to_frame(name='cnt').reset_index()
                # difine percent of rides with X number of passangers 
                df1n['percent'] = 100*df1n.cnt/df1.passenger_count.count()
                df2n['percent'] = 100*df2n.cnt/df2.passenger_count.count()
                df3n['percent'] = 100*df3n.cnt/df3.passenger_count.count()
            else:
                df1Val = 100*df1[field].groupby(lambda x: x.month).count()/df1[field].count() 
                df2Val = 100*df2[field].groupby(lambda x: x.month).count()/df2[field].count() 
                df3Val = 100*df3[field].groupby(lambda x: x.month).count()/df3[field].count() 
        elif flag =='cnt-total':
            df1Val = df1[field].groupby(lambda x: x.month).count()
            df2Val = df2[field].groupby(lambda x: x.month).count()
            df3Val = df3[field].groupby(lambda x: x.month).count()        
        else :
            print('Not a valid option, try: percent or total')
       
        if ((field == 'passenger_count') and (flag =='cnt-percent')):
            fig = plt.figure()
            ax = fig.add_subplot(111)
            style = ['b','b--','b:','b-.']
            [ax.plot(df1n.level_0[df1n.passenger_count == f],df1n.percent[df1n.passenger_count == f], style[f-1], 
                     label =Labels[0]+ 'passanger ='+str(f)) for f in range(1,5)]
            style = ['g','g--','g:','g-.']
            [ax.plot(df2n.level_0[df2n.passenger_count == f],df2n.percent[df2n.passenger_count == f], style[f-1], 
                    label =Labels[1]+ 'passanger ='+str(f)) for f in range(1,5)]
            style = ['k','k--','k:','k-.']
            [ax.plot(df3n.level_0[df3n.passenger_count == f],df3n.percent[df3n.passenger_count == f], style[f-1], 
                     label =Labels[2]+ 'passanger ='+str(f)) for f in range(1,5)]
            ax.set_yscale('log')
            ax.set_ylabel(ylabel)
            ax.set_xlabel('Month')
            ax.legend() 
        else:
             # create figure  
            fig = plt.figure()
            ax = fig.add_subplot(111)
            cols = ['b','g','k']
            ax.plot(df1Val, cols[0], label = Labels[0])
            ax.plot(df2Val,cols[1], label =Labels[1])
            ax.plot(df3Val, cols[2],label = Labels[2])
            ax.set_ylabel(ylabel)
            ax.set_xlabel('Month')
            ax.legend() 
        
    
    