import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import query_archive as qa
import plotly.graph_objects as go
from theme import theme
conn = sqlite3.connect('final.db')

############# Querying Database #############
dfIntel = pd.read_sql_query(qa.lineIntelQuery, conn)
dfSamsung = pd.read_sql_query(qa.lineSamsungQuery, conn)
dfTSMC = pd.read_sql_query(qa.lineTSMCQuery, conn)

companies = ['Intel Corporation', 'Samsung Electronics', 'Taiwan Semiconductor Manufacturing Company']

conn.close()
print(dfIntel.columns)  # check the columns of the dataframe

############# Data Preprocessing #############
dfIntel['Timeline'] = dfIntel['Year'] + ' ' + dfIntel['Quarter']
dfSamsung['Timeline'] = dfSamsung['Year'] + ' ' + dfSamsung['Quarter']
dfTSMC['Timeline'] = dfTSMC['Year'] + ' ' + dfTSMC['Quarter']

list_df = [dfIntel, dfSamsung, dfTSMC]


############# Plotting Chart #############
fig = go.Figure()

for i in range(len(list_df)):
    df = list_df[i]
    
    fig.add_trace(
        go.Scatter(
            x=df['Timeline'], 
            y=df['Domestic'], 
            mode='lines', 
            name=f'{companies[i] if (companies[i] != companies[2]) else 'TSMC'}\'s Domestic Citations', 
            line=dict(color=theme.highlightAlert),
            visible=(i == 0)
            )
        )
    fig.add_trace(
        go.Scatter(
            x=df['Timeline'], 
            y=df['Foreign'], 
            mode='lines', 
            name=f'{companies[i] if (companies[i] != companies[2]) else 'TSMC'}\'s Foreign Citations', 
            line=dict(color=theme.highlight3),
            visible=(i == 0)
            )
        )

buttons = []
for i, company in enumerate(companies):
    visibility = []  # Make only one trace visible
    
    for j in range(len(companies)):
        visibility.append(j == i)
        visibility.append(j == i)

    buttons.append(
        dict(
            label=company if (company != companies[2]) else 'TSMC',
            method="update",
            args=[{"visible": visibility},  # Update trace visibility
                  {"title": f"Citations of {company}"}]  # Update chart title
        )
    )
    
fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            showactive=True,
            buttons=buttons,
            #x=1.15,  # Position the buttons to the right of the chart
            y=0.8,
            xanchor="right",
        )
    ],
    title="Citations of Companies",
    xaxis_title="Year - Quarter",
    yaxis_title="Citations",
    legend_title="Citation Type",
    xaxis_tickangle=-45,
    xaxis_tickwidth=2,
)

#fig.show()  # show the chart