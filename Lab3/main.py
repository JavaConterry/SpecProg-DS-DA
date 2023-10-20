from spyre import server
import sys
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(1, 'C:\\Users\\glebo\\Documents\\University\\SpecProg\\Lab2') #path to lab2 lib
from requester import request_data
from sparse_time import parseYWYW


data = request_data()

class NOAA_vis(server.App):
    title = "NOAA data visualization"

    inputs = [{
        "type": 'dropdown',
        "label": 'NOAA dropdown',
        "options": [
            {"label": "VCI", "value": "VCI"},
            {"label": "TCI", "value": "TCI"},
            {"label": "VHI", "value": "VHI"}],
        "key": 'ticker',
        "action_id": "update_data"
    },
    {
        "type": 'dropdown',
        "label": 'Village',
        "options": [
            {"label": "Cherkasy", "value": "22"},
            {"label": "Chernihiv", "value": "24"},
            {"label": "Chernivtsi", "value": "23"},
            {"label": "Crimea", "value": "25"},
            {"label": "Dnipropetrovs", "value": "3"},
            {"label": "Donetsk", "value": "4"},
            {"label": "Ivano-Frankivs", "value": "8"},
            {"label": "Kharkiv", "value": "19"},
            {"label": "Kherson", "value": "20"},
            {"label": "Khmel'nyts'kyy", "value": "21"},
            {"label": "Kiyv", "value": "9"},
            {"label": "Kyivcity", "value": "26"},
            {"label": "Kirovohrad", "value": "10"},
            {"label": "Luhansk", "value": "11"},
            {"label": "L'viv", "value": "12"},
            {"label": "Mykolayiv", "value": "13"},
            {"label": "Odessa", "value": "14"},
            {"label": "Poltava", "value": "15"},
            {"label": "Rivne", "value": "16"},
            {"label": "Sevastopol", "value": "27"},
            {"label": "Sumy", "value": "17"},
            {"label": "Ternopil", "value": "18"},
            {"label": "Transcarpathia", "value": "6"},
            {"label": "Vinnytsya", "value": "1"},
            {"label": "Volyn", "value": "2"},
            {"label": "Zaporizhzhya", "value": "7"},
            {"label": "Zhytomyr", "value": "5"}],
        "key": 'village',
        "action_id": "update_data"
    },
    {
        "type": 'text',
        "label": 'y.w-y.w',
        "key": 'time',
        "action_id": "update_data"
    },
    ]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "get data"
    }]

    tabs = ["Plot", "Table"]

    outputs = [
        {
            "type": "plot",
            "id": "plot",
            "control_id": "update_data",
            "tab": "Plot"},
        {
            "type": "table",
            "id": "table_id",
            "control_id": "update_data",
            "tab": "Table",
            "on_page_load": True
        }
    ]

    def getData(self, params):
        ticker = params['ticker']
        if ticker == 'empty':
            ticker = params['custom_ticker'].upper()
        time = params['time']
        y1, w1, y2, w2 = parseYWYW(time)
        village_data = data[int(params['village'])]
        village_data['Time_ID'] = village_data['Year'] *52 +village_data['Week']
        return(village_data[(village_data["Time_ID"]>=(y1*52+w1)) & (village_data["Time_ID"]<=(y2*52+w2))].iloc[:, :-1]) 
        

    def getPlot(self, params):
        df = self.getData(params)
        df_copy = df.copy()
        df_copy = df_copy.reset_index(drop=True)
        for i in range(len(df_copy[['Year','Week']].values)):
            df_copy['Week'][i] = str(df_copy['Year'][i]) +"-" +str(df_copy['Week'][i])
            df_copy.drop(['Year'], axis=1)
        print(df_copy)
        plot = df_copy.plot(x='Week', y=params['ticker'], xlabel="Year-week", ylabel="Value")
        return plot.get_figure()


app = NOAA_vis()
app.launch()
