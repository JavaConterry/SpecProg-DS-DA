from spyre import server
from googlefinance.client import get_price_data

server.include_df_index = True


class StockExample(server.App):
    title = "Historical Stock Prices"

    inputs = [{
        "type": 'dropdown',
        "label": 'Company',
        "options": [
            {"label": "Google", "value": "GOOG"},
            {"label": "Amazon", "value": "AMZN"},
            {"label": "Apple", "value": "AAPL"}],
        "value": 'GOOG',
        "key": 'ticker',
        "action_id": "update_data"
    }]

    controls = [{
        "type": "button",
        "id": "update_data",
        "label": "get historical stock prices"
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

        xchng = "NASD"
        param = {
            'q': ticker,  # Stock symbol (ex: "AAPL")
            'i': "86400",  # Interval size in seconds ("86400" = 1 day intervals)
            'x': xchng,  # Stock exchange symbol on which stock is traded (ex: "NASD")
            'p': "3M"  # Period (Ex: "1Y" = 1 year)
        }
        df = get_price_data(param)
        return df

    def getPlot(self, params):
        df = self.getData(params).drop(['Volume'], axis=1)
        plt_obj = df.plot()
        plt_obj.set_ylabel("Price")
        plt_obj.set_xlabel("Date")
        plt_obj.set_title(params['ticker'])
        return plt_obj.get_figure()


app = StockExample()
app.launch()
