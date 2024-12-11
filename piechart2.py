import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import query_archive as qa
from theme import theme

# Step 1: Connect to the database
conn = sqlite3.connect("final.db")  # Update with your database file name

# Step 2: Execute the query and load the data into a DataFrame
df = pd.read_sql_query(qa.pieChartQuery2, conn)

# Step 3: Close the database connection
conn.close()

# Step 4: Filter for a specific company (e.g., "Alpha Inc.")
labels = ['Valid', 'Overdue', 'Published']

traceList = []
for i in range(len(df["Holder"])):
    traceList.append(go.Pie(labels=labels, values=df.iloc[i, 2:], name=df.iloc[i, 1], marker=dict(colors=[theme.highlight1, theme.highlightAlert, theme.highlight2]), visible=False))

traceList.append(go.Pie(labels=labels, values=df.iloc[:, 2:].sum(axis=0), name="All Companies", marker=dict(colors=[theme.highlight1, theme.highlightAlert, theme.highlight2]), visible=True))
                 
# Step 5: Create the pie chart
fig = go.Figure(data=traceList)

fig.update_layout(
    title="Patent Legal Status (All Companies)",
    updatemenus=[dict(
        type="dropdown",
        buttons=[
            {
                "label": "Show All",
                "method": "update",
                "args": [
                    {"visible": [False] * len(df["Holder"]) + [True]},
                    {"title": "Patent Legal Status (All Companies)"}
                ]
            },
            *[{
                "label": company,
                "method": "update",
                "args": [
                    {"visible": [company == df["Holder"][i] for i in range(len(df["Holder"]))] + [False]}, 
                    {"title": f"Patent Legal Status ({company})"}
                ]
            }
            for company in df["Holder"]
            ]
        ],
        direction="down",
        showactive=True,
        x=0.0,
        yanchor="middle",
    )]
)

#fig.show()  # Display the chart
