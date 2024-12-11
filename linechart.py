import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import query_archive as qa
from theme import theme
conn = sqlite3.connect('final.db')

############# Querying Database #############
df = pd.read_sql_query(qa.lineChartQuery, conn)

conn.close()
print(df.columns)  # check the columns of the dataframe

############# Data Preprocessing #############
df_long = df.melt(id_vars="Year", value_vars=["Intel Corporation", "Samsung Electronics", "Taiwan Semiconductor Manufacturing Company"], 
                  var_name="Company", value_name="Count")

custom_color = {
    "Intel Corporation": theme.highlightAlert,
    "Samsung Electronics": theme.highlight1,
    "Taiwan Semiconductor Manufacturing Company": theme.highlight5
}
############# Plotting Chart #############
# create line chart using plotly
fig = px.line(df_long, x="Year", y="Count", color="Company", color_discrete_map=custom_color,
              title="Yearly Patent Throughput (Successful Publication)")
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="No. of Patents Published",
    xaxis=dict(type='category', categoryorder='array', categoryarray=df["Year"]),
)

#fig.show()  # show the chart