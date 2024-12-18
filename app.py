from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import sqlite3
import piechart2 as pc2
import linechart2 as lc2
import barchart as bc
import linechart as lc
import piechart as pc
import linechart3 as lc3
from theme import theme

app = Dash(__name__)

#deployment
server = app.server

app.layout = html.Div(children=[
    html.Div(children=[
    html.H1('Patent Portfolio Analysis Dashboard',
            style={
                'font-family': theme.font1,
                'font-size': theme.title,
                'color': theme.white,
            }),
    html.P('Made by Sika Deer Team, this dashboard provides an overview of the patent portfolio for System on a Chip (SoC) technology. This dashboard aim to assist in efficient decision making for R&D direction of a company.',
            style={
                'font-family': theme.font1,
                'font-size': theme.subtitle,
                'bold': 'False',
                'color': theme.white,
            }),
    ],
    style={
        'padding': '20px',
        'background-color': theme.highlight3,
        'color': theme.white,
        'border-radius': '25px',
    },             
    ),
    html.Hr(style={'border': '0.25px solid',
                   'width': '95%',
                   'margin': '10px auto',
                   'color': theme.highlight1,
                   }),
    html.Div(children=[
        html.Div(children=[
            html.H4('Competitor Performance Analysis',
                    style={
                        'font-family': theme.font1,
                        'font-size': theme.header,
                        'color': theme.highlight1,
                    }),
            html.P('Understand the race with an overview of the major competitors and their overall performances.',
                   style={
                       'font-family': theme.font1,
                       'font-size': theme.body,
                       'color': theme.highlight1,
                   }),
            dcc.Graph(id='throughput-line-chart'),
            dcc.Slider(
                id='year-slider',
                min=2013,           # Minimum value
                max=2024,         # Maximum value
                step=1,          # Step size
                value=2024,        # Default value
                marks={          # Marks shown on the slider
                    i : {'label': str(i)} for i in range(2013, 2025, 1)
                },
                tooltip={"placement": "bottom", 
                         "style": {'width': '70%'},
                         "always_visible": True},  # Show tooltip
            ),
            html.Div(children=[
                dcc.Graph(id='share-pie-chart', figure = pc.fig),
                dcc.Graph(id='pie-chart', figure = pc2.fig),
                ],
                style = {
                    'width': '100%',
                    'display': 'flex',
                    'justify-content': 'space-around',
                    'align': 'center',
                    'padding': '5px',
                    'height': '400px',
                },
            ),
            html.H5('Importance of Above Data:',
                    style={
                        'font-family': theme.font1,
                        'font-size': theme.header2,
                        'color': theme.highlight1,
                    },
                ),
            html.P('Understanding the current market share, and percentage of active patents maintained by main competitors are key in analyzing their performance up against you.',
                     style={
                          'font-family': theme.font1,
                          'font-size': theme.body,
                          'color': theme.highlight1,
                     }
            ),
        ],
        style={
            'padding': '10px',
            'width': '100%',
        }
        ),
        html.Hr(style={'border': '0.25px solid',
                   'width': '90%',
                   'margin': '10px auto',
                   'color': theme.highlight1,
                   }),
        html.Div(children=[
                    #empty
                    html.Div(
                        children=[
                    html.H4('Find Out What\'s Trending',
                            style={
                                'font-family': theme.font1,
                                'font-size': theme.header,
                                'color': theme.white,
                                }),
                    html.P('Understand the patent trend, get insights into trending category of patent to maximize returns from research.',
                            style={
                                'font-family': theme.font1,
                                'font-size': theme.body,
                                'color': theme.white,
                                }),
                        ],
                        style={
                            'padding': '100px',
                            'width': '220px',
                            'height': '220px',
                            'border-radius': '50%',
                            'background-color': theme.highlight3,
                            'justify-content': 'center',
                            'align-items': 'center',
                            'text-align': 'left',
                        },
                    ),
                    html.Div(
                        children=[],
                        style={
                        'border': '0.25px solid',
                        'margin': '20px auto',
                        'height': '400px',
                        'color': theme.highlight1,}),
                    dcc.Graph(id='bar-chart', figure = bc.fig),
                    ],
                style={'width': '80%', 
                        'height': '80%',
                        'display': 'flex',
                        'justify-content': 'space-around',
                        'align': 'left',
                        'padding': '20px',
                    }),
        dcc.Graph(id='line-chart3', figure = lc3.fig),
        html.Hr(style={'border': '0.25px solid',
                   'width': '90%',
                   'margin': '10px auto',
                   'color': theme.highlight1,
                   }),
        html.H4('Domestic and Foreign Citations Analysis & Comparisons',
                style={
                    'font-family': theme.font1,
                    'font-size': theme.header,
                    'color': theme.highlight1,
                    }),
        html.P('Understand the trend of citations through the years with our Citation Trend Chart. The line chart shows the number of citations for each company, divided into domestic and foreign citations which can help improve understanding of the company\'s impact on the local and global scale.',
               style={
                   'font-family': theme.font1,
                   'font-size': theme.body,
                   'color': theme.highlight1,
                   'width': '40%',
                   }),
        html.Div(children=[
            html.Div(children=[
            html.P('‼️Select companies to compare its citation trend and see the differences.‼️',
                style={
                    'font-family': theme.font1,
                    'font-size': theme.body,
                    'color': theme.darkGrey,
                    }),
            ],
            style={
                'background-color': theme.grey,
                'border-radius': '10px',
                'padding': '10px',
                'width': '40%',
                'text-align': 'center',
            }),
        ],
        style={
            'padding': '20px',
            'width': '100%',
            'text-align': 'center',
            'display': 'flex',
            'align-items': 'center',
            'justify-content': 'space-around',
        }),
        dcc.Graph(id='line-chart', figure = lc2.fig),
        html.Div(children=[
            html.P('Vs.',
                style={
                    'font-family': theme.font1,
                    'font-size': theme.subtitle,
                    'color': theme.highlight1,
                    }),
        ],
        style={
            'padding': '10px',
            'width': '100%',
            'text-align': 'center',
        }),
        dcc.Graph(id='line-chart-comparer', figure = lc2.fig),
    ],
        style={'padding': '10px',
               'text-align': 'left',
               }
    ),
    # html.Div(children=dcc.Graph(id='line-chart', figure = lc2.fig),
    #             style={'padding': '10px'}
    # ),
],
style={'textAlign': 'center',
    },

)

@app.callback(
    Output('throughput-line-chart', 'figure'),
    Input('year-slider', 'value')
)
def update_line_chart(slider_value):
    # Pass the slider value to the function to generate the updated chart
    return lc.generateChart(slider_value)


if __name__ == '__main__':
    app.run(debug=True)
    #app.run_server(debug=True)