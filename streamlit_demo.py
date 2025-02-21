import streamlit as st
import pandas as pd
from awesome_table import AwesomeTable

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')


airline_selection = st.multiselect(
    label="Airline", 
    help="Select Airline", 
    options=['']+df['airline'].to_list()
)

st.write(f"You chose Airlines: {",".join(airline_selection)}" if airline_selection else "")

st.title("Fatalities Trend Chart - 1985 to 1999")
if airline_selection:
    st.line_chart(data=df[df['airline'].isin(airline_selection)], x='airline', y='fatalities_85_99')
else:
    st.line_chart(data=df, x='airline', y='fatalities_85_99')

st.title("Airline Fatalities")
if not airline_selection:
    AwesomeTable(
            data=pd.json_normalize(df.to_dict(orient='records')),
            show_search=True,
            show_search_order_in_sidebar=True,
            show_order=True,
            key="table1"
        )
else:
    AwesomeTable(
            data=pd.json_normalize(df[df['airline'].isin(airline_selection)].to_dict(orient='records')),
            show_search=True,
            show_search_order_in_sidebar=True,
            show_order=True,
            key="table1"
        )