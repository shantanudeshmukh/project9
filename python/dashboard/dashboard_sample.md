Sample dashboard file
--------

Thanks, to plotly for making this easy!!!

    import dash
    from dash.dependencies import Input, Output
    import dash_core_components as dcc
    import dash_html_components as html
    from pandas_datareader import data as web
    from datetime import datetime as dt
    import pandas as pd
    from pandas.api.types import is_list_like
    pd.core.common.is_list_like = pd.api.types.is_list_like
    
    app = dash.Dash()
    
    app.layout = html.Div([
        html.H1('Stock Tickers'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Coke', 'value': 'COKE'},
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'}
            ],
            value='COKE'
        ),
        dcc.Graph(id='my-graph')
    ])
    
    @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = web.DataReader(
            selected_dropdown_value, data_source='google',
            start=dt(2017, 1, 1), end=dt.now())
        return {
            'data': [{
                'x': df.index,
                'y': df.Close
            }]
        }
    
    if __name__ == '__main__':
        app.run_server()

run the above code and you will observe the following error

    cannot import: is_list_like in fred.py

so, now in this case, paste the following import lines on the top of fred.py

    import pandas as pd
    from pandas.api.types import is_list_like
    pd.core.common.is_list_like = pd.api.types.is_list_like
    
after which run your code you are good !!!
    
