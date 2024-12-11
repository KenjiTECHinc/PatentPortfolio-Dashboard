import sqlite3
import pandas as pd
import plotly.express as px
from theme import theme

# Connect to the database
db_path = 'final.db'
conn = sqlite3.connect(db_path)

# Get the list of tables to understand the database structure
query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql(query, conn)
tables

# Extract data related to the 'MIPC3' column to create a bar chart
# Count the number of patents for each MIPC3 category
query = """
    SELECT MIPC3, COUNT(*) as Patent_Count
    FROM '1- Patents'
    GROUP BY MIPC3
    ORDER BY Patent_Count DESC;
"""
mipc3_data = pd.read_sql(query, conn)

query_top_15 = """
    SELECT MIPC3, COUNT(*) as Patent_Count
    FROM '1- Patents'
    GROUP BY MIPC3
    ORDER BY Patent_Count DESC
    LIMIT 15;
"""
mipc3_data_top_20 = pd.read_sql(query_top_15, conn)



# Plotting the top 20 data as a bar chart

fig = px.bar(
    mipc3_data_top_20, 
    x='MIPC3', 
    y='Patent_Count', 
    title='Top 15 MIPC Categories by Number of Patents',
    labels={'MIPC3': 'MIPC Category', 'Patent_Count': 'Number of Patents'},
    )
fig.update_traces(marker_color=theme.highlight1)
fig.update_layout(xaxis_tickangle=-45)

#fig.show()

# plt.figure(figsize=(10, 6))
# plt.bar(mipc3_data_top_20['MIPC3'], mipc3_data_top_20['Patent_Count'])
# plt.xlabel('MIPC Category')
# plt.ylabel('Number of Patents')
# plt.title('Top 20 MIPC Categories by Number of Patents')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()