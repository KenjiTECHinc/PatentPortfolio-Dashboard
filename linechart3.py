import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import query_archive as qa
from theme import theme
conn = sqlite3.connect("final.db")  # Update with your database file name
############# Querying Database #############
df = pd.read_sql_query(qa.lineChartQuery3, conn)

############# Data Preprocessing #############
custom_color = [
    theme.highlight1,
    theme.highlight7,
    theme.highlight5,
    theme.highlight6,
    theme.highlight8,
]
############# Plotting Chart #############
fig = px.line(df, 
              x="Publication Year", 
              y="Patent_Count", 
              color="MIPC3",
              title="Patent Trend for Top 5 Categories in the Past 7 Years",
              labels={"Publication Year": "Year", "Patent_Count": "Number of Patents"},
              markers=True,
              color_discrete_sequence=custom_color,
              )

# Customize the layout
fig.update_layout(
    xaxis=dict(dtick=1),  # Ensure all years are displayed
    yaxis_title="Number of Patents",
    legend_title="MIPC3 Codes",
)

# Show the chart
#fig.show()