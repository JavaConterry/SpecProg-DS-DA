from spyre import server
import sys

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
        return village_data[(village_data['Year'] > y1) | ((village_data['Year'] == y1) & (village_data['Week'] >= w1)) & (village_data['Year'] < y2) | ((village_data['Year'] == y2) & (village_data['Week'] <= w2))]

    # def getPlot(self, params):
    #     df = self.getData(params).drop(['Volume'], axis=1)
    #     plt_obj = df.plot()
    #     plt_obj.set_ylabel("Price")
    #     plt_obj.set_xlabel("Date")
    #     plt_obj.set_title(params['ticker'])
    #     return plt_obj.get_figure()


app = NOAA_vis()
app.launch()
