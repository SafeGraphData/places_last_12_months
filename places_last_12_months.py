import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics - Last 12 Months",
    layout="wide"
)
#### Last 12 Months ####
global_places_df = (read_from_gsheets("Global Places").query('Country  != "Excluding US"').reset_index(drop=True))
global_places_df = global_places_df[["Release month", "Country", "Total POI"]]

for i, value in enumerate(global_places_df['Release month']):
    try:
        global_places_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%b %Y').strftime('%Y-%m')
    except ValueError:
        global_places_df.loc[i, 'Release month'] = pd.to_datetime(value, format='%B %Y').strftime('%Y-%m')

start_date_str = (datetime.now() - timedelta(days=365)).strftime("%Y-%m")

global_places_df["Release month"] = pd.to_datetime(global_places_df["Release month"])
last_12_months_df = global_places_df[
    (global_places_df["Release month"] >= start_date_str) & (global_places_df["Release month"] <= datetime.now()) &
    (global_places_df["Country"] != "Grand Total")
]
last_12_months_df["Release month"] = pd.to_datetime(last_12_months_df["Release month"])+ pd.DateOffset(1)
last_12_months_df["Release month"] = last_12_months_df["Release month"].dt.strftime('%Y-%m-%dT%H:%M:%SZ')
last_12_months_df['Total POI'] = pd.to_numeric(last_12_months_df['Total POI'])

# st.dataframe(last_12_months_df)

last_12_months = alt.Chart(last_12_months_df).mark_bar().encode(
    x=alt.X('Release month', timeUnit='yearmonth'),
    y='Total POI',
    color=alt.Color('Country', scale=alt.Scale(scheme='redyellowblue')),
    tooltip=[alt.Tooltip('Release month', timeUnit='yearmonth', title='Release month'),
             alt.Tooltip('Country'),
             alt.Tooltip('Total POI', format=',')]
).properties(
    width=900,
    height=500,
    title=alt.TitleParams(
        text='Total POI Count - Last 12 months',
        fontSize=18
    )
).configure_axisY(
    labelAngle=20
).configure_axisX(
    title=None,
    labelAngle=45
)

st.altair_chart(last_12_months, use_container_width=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)


css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-04-25 16:08:28.221148
# Keep-alive comment: 2025-04-25 16:18:22.525482
# Keep-alive comment: 2025-04-26 00:23:57.387601
# Keep-alive comment: 2025-04-26 11:23:52.142347
# Keep-alive comment: 2025-04-26 22:22:51.364454
# Keep-alive comment: 2025-04-27 09:23:22.207928
# Keep-alive comment: 2025-04-27 20:23:17.097001
# Keep-alive comment: 2025-04-28 07:23:47.016927
# Keep-alive comment: 2025-04-28 18:24:07.255891
# Keep-alive comment: 2025-04-29 05:23:37.148033
# Keep-alive comment: 2025-04-29 16:24:21.299634
# Keep-alive comment: 2025-04-30 03:23:11.833806
# Keep-alive comment: 2025-04-30 14:23:39.513061
# Keep-alive comment: 2025-05-01 01:23:51.326892
# Keep-alive comment: 2025-05-01 12:23:22.247548
# Keep-alive comment: 2025-05-01 23:22:55.132593
# Keep-alive comment: 2025-05-02 10:23:41.255325
# Keep-alive comment: 2025-05-02 21:22:52.846984
# Keep-alive comment: 2025-05-03 08:23:17.316464
# Keep-alive comment: 2025-05-03 19:23:35.465198
# Keep-alive comment: 2025-05-04 06:23:41.086213
# Keep-alive comment: 2025-05-04 17:22:50.352490
# Keep-alive comment: 2025-05-05 04:24:00.672177
# Keep-alive comment: 2025-05-05 15:23:18.790920
# Keep-alive comment: 2025-05-06 02:24:11.226347
# Keep-alive comment: 2025-05-06 13:23:12.257747
# Keep-alive comment: 2025-05-07 00:23:11.771375
# Keep-alive comment: 2025-05-07 11:23:12.320644
# Keep-alive comment: 2025-05-07 22:23:22.650352
# Keep-alive comment: 2025-05-08 09:23:15.143624
# Keep-alive comment: 2025-05-08 20:23:23.020620
# Keep-alive comment: 2025-05-09 07:23:30.804482
# Keep-alive comment: 2025-05-09 18:23:43.740329
# Keep-alive comment: 2025-05-10 05:23:20.590121
# Keep-alive comment: 2025-05-10 16:23:14.816133
# Keep-alive comment: 2025-05-11 03:23:15.333895
# Keep-alive comment: 2025-05-11 14:23:06.940726
# Keep-alive comment: 2025-05-12 01:23:12.146861