######################################################################
Author: Shantanu V. Deshmukh 
######################################################################

# plot single bar chart
import plotly.graph_objs as go
import plotly as plotly

def plot_single_bar_graph(x1_data, x2_data, y1_data, y2_data, x_axis_title, y_axis_title, plot_title, output_path, save_filename):

    trace1 = go.Bar(
        x=x1_data,
        y=y1_data,
        name='legend line1'
    )
    
    data = [trace1]
    layout = go.Layout(,
        title=plot_title,
        xaxis=dict(
            title=x_axis_title,
            titlefont=dict(
                # family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title=y_axis_title,
            titlefont=dict(
                # family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename = output_path + save_filename + ".html")


# plot grouped bar chart

import plotly.graph_objs as go
import plotly as plotly

def plot_grouped_bar_graph(x1_data, x2_data, y1_data, y2_data, x_axis_title, y_axis_title, plot_title, output_path, save_filename):

    trace1 = go.Bar(
        x=x1_data,
        y=y1_data,
        name='legend line1'
    )
    trace2 = go.Bar(
        x=x2_data,
        y=y2_data,
        name='legend line2'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group',
        title=plot_title,
        xaxis=dict(
            title=x_axis_title,
            titlefont=dict(
                # family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        ),
        yaxis=dict(
            title=y_axis_title,
            titlefont=dict(
                # family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename = output_path + save_filename + ".html")
