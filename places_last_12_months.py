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
# Keep-alive comment: 2025-05-12 12:23:42.127476
# Keep-alive comment: 2025-05-12 23:23:15.742912
# Keep-alive comment: 2025-05-13 10:24:14.937668
# Keep-alive comment: 2025-05-13 21:23:16.165758
# Keep-alive comment: 2025-05-14 08:23:42.082494
# Keep-alive comment: 2025-05-14 19:23:41.571651
# Keep-alive comment: 2025-05-15 06:23:42.965656
# Keep-alive comment: 2025-05-15 17:24:06.852523
# Keep-alive comment: 2025-05-16 04:23:28.201378
# Keep-alive comment: 2025-05-16 15:22:30.867539
# Keep-alive comment: 2025-05-17 02:22:49.590021
# Keep-alive comment: 2025-05-17 13:23:23.300150
# Keep-alive comment: 2025-05-18 00:22:47.930951
# Keep-alive comment: 2025-05-18 11:23:16.164822
# Keep-alive comment: 2025-05-18 22:23:13.446957
# Keep-alive comment: 2025-05-19 09:23:49.038241
# Keep-alive comment: 2025-05-19 20:22:48.387122
# Keep-alive comment: 2025-05-20 07:23:04.434057
# Keep-alive comment: 2025-05-20 18:24:16.526509
# Keep-alive comment: 2025-05-21 05:22:48.500537
# Keep-alive comment: 2025-05-21 16:22:57.320390
# Keep-alive comment: 2025-05-22 03:22:51.938518
# Keep-alive comment: 2025-05-22 14:22:55.431840
# Keep-alive comment: 2025-05-23 01:22:54.379674
# Keep-alive comment: 2025-05-23 12:22:54.207238
# Keep-alive comment: 2025-05-23 23:22:58.393099
# Keep-alive comment: 2025-05-24 10:22:56.291673
# Keep-alive comment: 2025-05-24 21:22:53.065043
# Keep-alive comment: 2025-05-25 08:22:53.583377
# Keep-alive comment: 2025-05-25 19:22:58.449969
# Keep-alive comment: 2025-05-26 06:22:43.370636
# Keep-alive comment: 2025-05-26 17:22:47.893150
# Keep-alive comment: 2025-05-27 04:22:53.537151
# Keep-alive comment: 2025-05-27 15:22:57.868158
# Keep-alive comment: 2025-05-28 02:23:07.626843
# Keep-alive comment: 2025-05-28 13:22:56.602244
# Keep-alive comment: 2025-05-29 00:22:51.611091
# Keep-alive comment: 2025-05-29 11:22:46.496146
# Keep-alive comment: 2025-05-29 22:23:01.037540
# Keep-alive comment: 2025-05-30 09:22:46.161806
# Keep-alive comment: 2025-05-30 20:22:46.681154
# Keep-alive comment: 2025-05-31 07:22:59.302892
# Keep-alive comment: 2025-05-31 18:22:53.921430
# Keep-alive comment: 2025-06-01 05:22:52.247894
# Keep-alive comment: 2025-06-01 16:23:05.787116
# Keep-alive comment: 2025-06-02 03:23:07.465680
# Keep-alive comment: 2025-06-02 14:22:57.968036
# Keep-alive comment: 2025-06-03 01:22:48.502272
# Keep-alive comment: 2025-06-03 12:23:02.664991
# Keep-alive comment: 2025-06-03 23:22:58.211029
# Keep-alive comment: 2025-06-04 10:22:58.033021
# Keep-alive comment: 2025-06-04 21:22:36.347810
# Keep-alive comment: 2025-06-05 08:23:00.561550
# Keep-alive comment: 2025-06-05 19:22:49.995870
# Keep-alive comment: 2025-06-06 06:22:48.195080
# Keep-alive comment: 2025-06-06 17:22:31.413765
# Keep-alive comment: 2025-06-07 04:22:33.404200
# Keep-alive comment: 2025-06-07 15:22:42.492733
# Keep-alive comment: 2025-06-08 02:22:47.842692
# Keep-alive comment: 2025-06-08 13:22:50.003610
# Keep-alive comment: 2025-06-09 00:22:32.078758
# Keep-alive comment: 2025-06-09 11:22:46.443889
# Keep-alive comment: 2025-06-09 22:22:54.592572
# Keep-alive comment: 2025-06-10 09:22:58.089598
# Keep-alive comment: 2025-06-10 20:22:51.207389
# Keep-alive comment: 2025-06-11 07:22:52.324474
# Keep-alive comment: 2025-06-11 18:24:39.973718
# Keep-alive comment: 2025-06-12 05:22:49.372982
# Keep-alive comment: 2025-06-12 16:22:52.730573
# Keep-alive comment: 2025-06-13 03:22:53.782689
# Keep-alive comment: 2025-06-13 14:22:42.933692
# Keep-alive comment: 2025-06-14 01:23:02.875462
# Keep-alive comment: 2025-06-14 12:22:50.153469
# Keep-alive comment: 2025-06-14 23:22:41.540161
# Keep-alive comment: 2025-06-15 10:22:27.301741
# Keep-alive comment: 2025-06-15 21:23:01.898368
# Keep-alive comment: 2025-06-16 08:22:58.733423
# Keep-alive comment: 2025-06-16 19:22:42.657695
# Keep-alive comment: 2025-06-17 06:23:19.672265
# Keep-alive comment: 2025-06-17 17:22:47.534570
# Keep-alive comment: 2025-06-18 04:22:53.958886
# Keep-alive comment: 2025-06-18 15:22:51.880921
# Keep-alive comment: 2025-06-19 02:22:51.359897
# Keep-alive comment: 2025-06-19 13:22:50.753103
# Keep-alive comment: 2025-06-20 00:22:48.110966
# Keep-alive comment: 2025-06-20 11:23:37.218693
# Keep-alive comment: 2025-06-20 22:22:56.774805
# Keep-alive comment: 2025-06-21 09:22:42.313169
# Keep-alive comment: 2025-06-21 20:22:54.503899
# Keep-alive comment: 2025-06-22 07:22:47.342631
# Keep-alive comment: 2025-06-22 18:22:37.747372
# Keep-alive comment: 2025-06-23 05:22:54.262872
# Keep-alive comment: 2025-06-23 16:22:47.384139
# Keep-alive comment: 2025-06-24 03:22:54.039025
# Keep-alive comment: 2025-06-24 14:22:33.172561
# Keep-alive comment: 2025-06-25 01:22:27.503268
# Keep-alive comment: 2025-06-25 12:22:49.318912
# Keep-alive comment: 2025-06-25 23:22:52.140515
# Keep-alive comment: 2025-06-26 10:22:59.621899
# Keep-alive comment: 2025-06-26 21:24:23.750774
# Keep-alive comment: 2025-06-27 08:22:52.846815
# Keep-alive comment: 2025-06-27 19:22:49.457848
# Keep-alive comment: 2025-06-28 06:22:56.616047
# Keep-alive comment: 2025-06-28 17:22:46.906007
# Keep-alive comment: 2025-06-29 04:22:35.982134
# Keep-alive comment: 2025-06-29 15:22:26.600937
# Keep-alive comment: 2025-06-30 02:22:47.937066
# Keep-alive comment: 2025-06-30 13:22:29.258106
# Keep-alive comment: 2025-07-01 00:24:34.105515
# Keep-alive comment: 2025-07-01 11:22:49.006761
# Keep-alive comment: 2025-07-01 22:22:53.419509
# Keep-alive comment: 2025-07-02 09:22:47.118042
# Keep-alive comment: 2025-07-02 20:24:35.972696
# Keep-alive comment: 2025-07-03 07:23:01.913387
# Keep-alive comment: 2025-07-03 18:22:27.346010
# Keep-alive comment: 2025-07-04 05:22:50.624579
# Keep-alive comment: 2025-07-04 16:22:47.037923
# Keep-alive comment: 2025-07-05 03:22:45.822734
# Keep-alive comment: 2025-07-05 14:22:50.810853
# Keep-alive comment: 2025-07-06 01:22:48.110302
# Keep-alive comment: 2025-07-06 12:22:45.382770
# Keep-alive comment: 2025-07-06 23:22:46.953318
# Keep-alive comment: 2025-07-07 10:22:47.655125
# Keep-alive comment: 2025-07-07 21:22:45.657237
# Keep-alive comment: 2025-07-08 08:22:50.891871
# Keep-alive comment: 2025-07-08 19:22:46.436127
# Keep-alive comment: 2025-07-09 06:22:57.672272
# Keep-alive comment: 2025-07-09 17:23:30.974193