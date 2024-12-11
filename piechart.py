import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import query_archive as qa
from theme import theme
conn = sqlite3.connect('final.db')

############# Querying Database #############

table_name = '1- Patents'
df = pd.read_sql_query(qa.pieChartQuery, conn)

conn.close() # close the connection
print(df.columns)

############# Data Preprocessing #############
# get names of companies (keep it unique) and save it as a pandas dataframe

############# Plotting Chart #############
# Make a pie chart based on the "Legal Status" column
fig = px.pie(df, values='Patents', names='Holder', title='Patents Ownership Market Share')

fig.update_traces(
    marker=dict(colors=[theme.highlight2, theme.highlight1, theme.highlightAlert]),
)

fig.update_layout(
    legend_title='Company',
)

## Display the pie chart
#fig.show()