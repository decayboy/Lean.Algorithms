import pandas as pd
import numpy as np
from datetime import timedelta


### <summary>
### Basic template algorithm simply initializes the date range and cash. This is a skeleton
### framework you can use for designing an algorithm.
### </summary>
class BasicTemplateAlgorithm(QCAlgorithm):
    '''Basic template algorithm simply initializes the date range and cash'''

    def Initialize(self):
        '''Initialise the data and resolution required, as well as the cash and start-end dates for your algorithm. All algorithms must initialized.'''
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage)
        self.SetBenchmark("SPY")
        self.SetStartDate(2009,12, 1)  #Set Start Date
        self.SetEndDate(2018,8,18)    #Set End Date
        self.SetCash(100000)           #Set Strategy Cash
        self.equity = ['SPY', 'IEF']
        self.months = {}
        # Find more symbols here: http://quantconnect.com/data
        self.AddEquity(self.equity[0], Resolution.Hour)
        self.AddEquity(self.equity[1], Resolution.Hour)
        self.google_trends = pd.DataFrame(columns=['Week', 'interest'])
        self.file = self.Download("https://www.dropbox.com/s/lzah401ulb8cdba/debtMonthly.csv?dl=1")
        self.file = self.file.split("\n")
        
        i = 0
        for row in self.file[1:]:
            one_row = row.split(",")
            self.google_trends.loc[i] = one_row
            i += 1
        self.google_trends["MA3"] = self.google_trends.interest.rolling(3).mean()
        self.google_trends["MA18"] = self.google_trends.interest.rolling(18).mean()
        
        self.google_trends["Signal"] =  self.google_trends["MA3"].astype('float') -  self.google_trends["MA18"].astype('float')
        self.google_trends["Signal"] = self.google_trends["Signal"].shift(1)
    def OnData(self, data):
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.

        Arguments:
            data: Slice object keyed by symbol containing the stock data
        '''
        date_today = self.Time.date()
        date_today = date_today.strftime(format='%Y-%m-%d')
        date_today = date_today[0:7]
        signal = self.google_trends.loc[self.google_trends.Week == date_today,"Signal"].iloc[0]
        
        try:
            invested = self.months[date_today]
        except:
            invested = "No"
        if self.Time.hour == 15 and invested == "No":
            
            if self.Portfolio[self.equity[0]].Quantity > 0 and signal > 0:
                self.Liquidate(self.equity[0])
            if self.Portfolio[self.equity[1]].Quantity > 0 and signal < 0:
                self.Liquidate(self.equity[1])

            if signal < 0 and self.Portfolio[self.equity[0]].Quantity == 0:
                self.SetHoldings(self.equity[0], 1)
                self.months[date_today] = "Yes"
                return
            if signal > 0 and self.Portfolio[self.equity[1]].Quantity == 0:
                self.SetHoldings(self.equity[1], 1)
                self.months[date_today] = "Yes"
                return
