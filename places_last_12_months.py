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
# Keep-alive comment: 2025-07-10 04:22:46.210992
# Keep-alive comment: 2025-07-10 15:22:51.602244
# Keep-alive comment: 2025-07-11 02:22:45.013889
# Keep-alive comment: 2025-07-11 13:22:46.059056
# Keep-alive comment: 2025-07-12 00:22:32.369859
# Keep-alive comment: 2025-07-12 11:22:50.604031
# Keep-alive comment: 2025-07-12 22:22:46.681675
# Keep-alive comment: 2025-07-13 09:22:46.449498
# Keep-alive comment: 2025-07-13 20:22:31.154813
# Keep-alive comment: 2025-07-14 07:22:43.375885
# Keep-alive comment: 2025-07-14 18:23:06.453250
# Keep-alive comment: 2025-07-15 05:22:56.828373
# Keep-alive comment: 2025-07-15 16:22:51.305003
# Keep-alive comment: 2025-07-16 03:22:50.933278
# Keep-alive comment: 2025-07-16 14:22:51.484627
# Keep-alive comment: 2025-07-17 01:22:46.332940
# Keep-alive comment: 2025-07-17 12:22:52.582668
# Keep-alive comment: 2025-07-17 23:22:44.788885
# Keep-alive comment: 2025-07-18 10:23:06.435645
# Keep-alive comment: 2025-07-18 21:22:45.992554
# Keep-alive comment: 2025-07-19 08:23:26.475886
# Keep-alive comment: 2025-07-19 19:22:31.351705
# Keep-alive comment: 2025-07-20 06:22:55.823072
# Keep-alive comment: 2025-07-20 17:23:01.874677
# Keep-alive comment: 2025-07-21 04:22:56.305707
# Keep-alive comment: 2025-07-21 15:22:42.830807
# Keep-alive comment: 2025-07-22 02:23:05.661463
# Keep-alive comment: 2025-07-22 13:23:19.051848
# Keep-alive comment: 2025-07-23 00:22:52.631682
# Keep-alive comment: 2025-07-23 11:22:42.091663
# Keep-alive comment: 2025-07-23 22:22:45.584075
# Keep-alive comment: 2025-07-24 09:23:01.752658
# Keep-alive comment: 2025-07-24 20:22:47.580558
# Keep-alive comment: 2025-07-25 07:22:42.030305
# Keep-alive comment: 2025-07-25 18:22:47.087987
# Keep-alive comment: 2025-07-26 05:22:41.483219
# Keep-alive comment: 2025-07-26 16:22:46.111218
# Keep-alive comment: 2025-07-27 03:22:41.336485
# Keep-alive comment: 2025-07-27 14:22:31.858897
# Keep-alive comment: 2025-07-28 01:22:52.747949
# Keep-alive comment: 2025-07-28 12:22:47.467073
# Keep-alive comment: 2025-07-28 23:22:46.071329
# Keep-alive comment: 2025-07-29 10:22:21.471003
# Keep-alive comment: 2025-07-29 21:22:52.006898
# Keep-alive comment: 2025-07-30 08:22:48.049212
# Keep-alive comment: 2025-07-30 19:22:56.274846
# Keep-alive comment: 2025-07-31 06:23:01.484145
# Keep-alive comment: 2025-07-31 17:22:46.912681
# Keep-alive comment: 2025-08-01 04:22:45.187494
# Keep-alive comment: 2025-08-01 15:22:56.378303
# Keep-alive comment: 2025-08-02 02:22:40.863760
# Keep-alive comment: 2025-08-02 13:22:51.309779
# Keep-alive comment: 2025-08-03 00:22:46.980482
# Keep-alive comment: 2025-08-03 11:22:51.992780
# Keep-alive comment: 2025-08-03 22:22:46.845005
# Keep-alive comment: 2025-08-04 09:22:43.504283
# Keep-alive comment: 2025-08-04 20:22:47.894346
# Keep-alive comment: 2025-08-05 07:22:50.297500
# Keep-alive comment: 2025-08-05 18:22:51.935042
# Keep-alive comment: 2025-08-06 05:22:46.177187
# Keep-alive comment: 2025-08-06 16:24:37.196049
# Keep-alive comment: 2025-08-07 03:22:50.894841
# Keep-alive comment: 2025-08-07 14:22:52.703109
# Keep-alive comment: 2025-08-08 01:22:41.615379
# Keep-alive comment: 2025-08-08 12:22:52.316539
# Keep-alive comment: 2025-08-08 23:22:52.544940
# Keep-alive comment: 2025-08-09 10:22:46.046467
# Keep-alive comment: 2025-08-09 21:23:08.439313
# Keep-alive comment: 2025-08-10 08:22:52.526478
# Keep-alive comment: 2025-08-10 19:22:52.622461
# Keep-alive comment: 2025-08-11 06:22:46.866287
# Keep-alive comment: 2025-08-11 17:22:52.435683
# Keep-alive comment: 2025-08-12 04:22:51.364359
# Keep-alive comment: 2025-08-12 15:22:43.676719
# Keep-alive comment: 2025-08-13 02:22:52.308700
# Keep-alive comment: 2025-08-13 13:22:48.017152
# Keep-alive comment: 2025-08-14 00:22:45.502758
# Keep-alive comment: 2025-08-14 11:22:53.451470
# Keep-alive comment: 2025-08-14 22:22:46.727222
# Keep-alive comment: 2025-08-15 09:22:46.635938
# Keep-alive comment: 2025-08-15 20:22:35.972386
# Keep-alive comment: 2025-08-16 07:23:00.771527
# Keep-alive comment: 2025-08-16 18:22:47.029173
# Keep-alive comment: 2025-08-17 05:22:50.244402
# Keep-alive comment: 2025-08-17 16:22:45.525456
# Keep-alive comment: 2025-08-18 03:22:47.085989
# Keep-alive comment: 2025-08-18 14:22:48.058946
# Keep-alive comment: 2025-08-19 01:22:47.163165
# Keep-alive comment: 2025-08-19 12:22:52.523480
# Keep-alive comment: 2025-08-19 23:23:14.384697
# Keep-alive comment: 2025-08-20 10:22:48.895587
# Keep-alive comment: 2025-08-20 21:22:51.706297
# Keep-alive comment: 2025-08-21 08:22:48.607470
# Keep-alive comment: 2025-08-21 19:22:52.559072
# Keep-alive comment: 2025-08-22 06:22:52.136827
# Keep-alive comment: 2025-08-22 17:22:47.347118
# Keep-alive comment: 2025-08-23 04:22:56.448513
# Keep-alive comment: 2025-08-23 15:22:45.729682
# Keep-alive comment: 2025-08-24 02:22:45.694585
# Keep-alive comment: 2025-08-24 13:22:46.596376
# Keep-alive comment: 2025-08-25 00:22:53.213940
# Keep-alive comment: 2025-08-25 11:22:52.041208
# Keep-alive comment: 2025-08-25 22:22:46.803417
# Keep-alive comment: 2025-08-26 09:22:47.838028
# Keep-alive comment: 2025-08-26 20:22:51.724045
# Keep-alive comment: 2025-08-27 07:22:56.809481
# Keep-alive comment: 2025-08-27 18:22:26.902847
# Keep-alive comment: 2025-08-28 05:22:57.479455
# Keep-alive comment: 2025-08-28 16:22:47.144156
# Keep-alive comment: 2025-08-29 03:22:31.086610
# Keep-alive comment: 2025-08-29 14:22:37.395893
# Keep-alive comment: 2025-08-30 01:22:36.241913
# Keep-alive comment: 2025-08-30 12:22:31.774866
# Keep-alive comment: 2025-08-30 23:22:35.453816
# Keep-alive comment: 2025-08-31 10:22:31.379636
# Keep-alive comment: 2025-08-31 21:22:42.647972
# Keep-alive comment: 2025-09-01 08:22:45.421220
# Keep-alive comment: 2025-09-01 19:22:42.927824
# Keep-alive comment: 2025-09-02 06:22:31.422474
# Keep-alive comment: 2025-09-02 17:22:42.781000
# Keep-alive comment: 2025-09-03 04:22:35.516192
# Keep-alive comment: 2025-09-03 15:22:38.107186
# Keep-alive comment: 2025-09-04 02:22:40.785027
# Keep-alive comment: 2025-09-04 13:22:49.351661
# Keep-alive comment: 2025-09-05 00:22:31.984960
# Keep-alive comment: 2025-09-05 11:22:27.104923
# Keep-alive comment: 2025-09-05 22:22:36.667352
# Keep-alive comment: 2025-09-06 09:22:32.594165
# Keep-alive comment: 2025-09-06 20:22:31.905945
# Keep-alive comment: 2025-09-07 07:22:37.387081
# Keep-alive comment: 2025-09-07 18:22:37.505734
# Keep-alive comment: 2025-09-08 05:22:33.418084
# Keep-alive comment: 2025-09-08 16:22:38.384345
# Keep-alive comment: 2025-09-09 03:23:03.270380
# Keep-alive comment: 2025-09-09 14:22:38.449861
# Keep-alive comment: 2025-09-10 01:22:31.102695
# Keep-alive comment: 2025-09-10 12:22:43.102550
# Keep-alive comment: 2025-09-10 23:22:31.944074
# Keep-alive comment: 2025-09-11 10:22:34.547112
# Keep-alive comment: 2025-09-11 21:22:32.217059
# Keep-alive comment: 2025-09-12 08:22:46.906567
# Keep-alive comment: 2025-09-12 19:22:37.215706
# Keep-alive comment: 2025-09-13 06:22:25.764009
# Keep-alive comment: 2025-09-13 17:22:32.312839
# Keep-alive comment: 2025-09-14 04:22:22.356229
# Keep-alive comment: 2025-09-14 15:22:33.402403
# Keep-alive comment: 2025-09-15 02:22:31.262350
# Keep-alive comment: 2025-09-15 13:22:33.696087
# Keep-alive comment: 2025-09-16 00:22:32.303676
# Keep-alive comment: 2025-09-16 11:22:37.637931
# Keep-alive comment: 2025-09-16 22:22:31.233643
# Keep-alive comment: 2025-09-17 09:22:33.861751
# Keep-alive comment: 2025-09-17 20:22:42.989792
# Keep-alive comment: 2025-09-18 07:22:39.389033
# Keep-alive comment: 2025-09-18 18:22:38.791708
# Keep-alive comment: 2025-09-19 05:22:32.978052
# Keep-alive comment: 2025-09-19 16:23:07.599579
# Keep-alive comment: 2025-09-20 03:22:37.051772
# Keep-alive comment: 2025-09-20 14:22:38.234534
# Keep-alive comment: 2025-09-21 01:22:37.547437
# Keep-alive comment: 2025-09-21 12:22:37.453523
# Keep-alive comment: 2025-09-21 23:22:32.915436
# Keep-alive comment: 2025-09-22 10:22:35.378714
# Keep-alive comment: 2025-09-22 21:22:31.988484
# Keep-alive comment: 2025-09-23 08:22:34.637665
# Keep-alive comment: 2025-09-23 19:22:39.362142
# Keep-alive comment: 2025-09-24 06:22:33.127058
# Keep-alive comment: 2025-09-24 17:22:37.686541
# Keep-alive comment: 2025-09-25 04:24:50.790413
# Keep-alive comment: 2025-09-25 15:22:42.868764
# Keep-alive comment: 2025-09-26 02:22:38.801496
# Keep-alive comment: 2025-09-26 13:22:42.420601
# Keep-alive comment: 2025-09-26 19:31:09.772741
# Keep-alive comment: 2025-09-27 05:31:14.721452
# Keep-alive comment: 2025-09-27 15:31:09.683967
# Keep-alive comment: 2025-09-28 01:31:14.042493
# Keep-alive comment: 2025-09-28 11:31:15.384651
# Keep-alive comment: 2025-09-28 21:31:13.838174
# Keep-alive comment: 2025-09-29 07:31:20.687617
# Keep-alive comment: 2025-09-29 17:31:30.195386
# Keep-alive comment: 2025-09-30 03:31:08.733719
# Keep-alive comment: 2025-09-30 13:31:15.225322
# Keep-alive comment: 2025-09-30 23:31:33.809658
# Keep-alive comment: 2025-10-01 09:31:40.534638
# Keep-alive comment: 2025-10-01 19:31:14.976973
# Keep-alive comment: 2025-10-02 05:31:43.166550
# Keep-alive comment: 2025-10-02 15:31:40.623659
# Keep-alive comment: 2025-10-03 01:31:14.207963
# Keep-alive comment: 2025-10-03 11:31:35.136811
# Keep-alive comment: 2025-10-03 21:31:09.144889
# Keep-alive comment: 2025-10-04 07:31:09.078807
# Keep-alive comment: 2025-10-04 17:31:19.348534
# Keep-alive comment: 2025-10-05 03:31:13.798819
# Keep-alive comment: 2025-10-05 13:31:18.961221
# Keep-alive comment: 2025-10-05 23:31:39.149462
# Keep-alive comment: 2025-10-06 09:31:45.114835
# Keep-alive comment: 2025-10-06 19:31:17.103713
# Keep-alive comment: 2025-10-07 05:31:16.380417
# Keep-alive comment: 2025-10-07 15:31:37.798927
# Keep-alive comment: 2025-10-08 01:31:14.655310
# Keep-alive comment: 2025-10-08 11:31:16.134327
# Keep-alive comment: 2025-10-08 21:31:15.426488
# Keep-alive comment: 2025-10-09 07:31:18.317508
# Keep-alive comment: 2025-10-09 17:31:17.648054
# Keep-alive comment: 2025-10-10 03:31:04.970064
# Keep-alive comment: 2025-10-10 13:30:56.542851
# Keep-alive comment: 2025-10-10 23:31:09.189522
# Keep-alive comment: 2025-10-11 09:31:15.338250
# Keep-alive comment: 2025-10-11 19:31:08.794909
# Keep-alive comment: 2025-10-12 05:31:12.568990
# Keep-alive comment: 2025-10-12 15:31:17.357716
# Keep-alive comment: 2025-10-13 01:31:11.063878
# Keep-alive comment: 2025-10-13 11:31:42.786589
# Keep-alive comment: 2025-10-13 21:31:05.248386
# Keep-alive comment: 2025-10-14 07:31:09.708165
# Keep-alive comment: 2025-10-14 17:31:12.469196
# Keep-alive comment: 2025-10-15 03:31:09.749825
# Keep-alive comment: 2025-10-15 13:31:11.872897
# Keep-alive comment: 2025-10-15 23:31:15.754825
# Keep-alive comment: 2025-10-16 09:31:11.213119
# Keep-alive comment: 2025-10-16 19:31:17.361702
# Keep-alive comment: 2025-10-17 05:31:15.982795
# Keep-alive comment: 2025-10-17 15:31:32.407055
# Keep-alive comment: 2025-10-18 01:31:10.926777
# Keep-alive comment: 2025-10-18 11:31:35.405575
# Keep-alive comment: 2025-10-18 21:31:45.203055
# Keep-alive comment: 2025-10-19 07:31:05.337945
# Keep-alive comment: 2025-10-19 17:31:40.102607
# Keep-alive comment: 2025-10-20 03:31:38.253048
# Keep-alive comment: 2025-10-20 13:31:16.421837
# Keep-alive comment: 2025-10-20 23:31:10.658644
# Keep-alive comment: 2025-10-21 09:31:16.654169
# Keep-alive comment: 2025-10-21 19:33:17.607125
# Keep-alive comment: 2025-10-22 05:31:11.667005
# Keep-alive comment: 2025-10-22 15:32:17.082318
# Keep-alive comment: 2025-10-23 01:31:10.070422
# Keep-alive comment: 2025-10-23 11:31:23.059900
# Keep-alive comment: 2025-10-23 21:31:12.034531
# Keep-alive comment: 2025-10-24 07:32:31.791748
# Keep-alive comment: 2025-10-24 17:31:21.643855
# Keep-alive comment: 2025-10-25 03:31:15.640276
# Keep-alive comment: 2025-10-25 13:31:39.487972
# Keep-alive comment: 2025-10-25 23:31:11.724893
# Keep-alive comment: 2025-10-26 09:31:04.810490
# Keep-alive comment: 2025-10-26 19:31:41.661849
# Keep-alive comment: 2025-10-27 05:31:22.098830
# Keep-alive comment: 2025-10-27 15:31:37.224184
# Keep-alive comment: 2025-10-28 01:31:14.499326
# Keep-alive comment: 2025-10-28 11:31:16.804781
# Keep-alive comment: 2025-10-28 21:31:05.482654
# Keep-alive comment: 2025-10-29 07:31:12.157646
# Keep-alive comment: 2025-10-29 17:31:21.333619
# Keep-alive comment: 2025-10-30 03:31:11.113960
# Keep-alive comment: 2025-10-30 13:31:42.542812
# Keep-alive comment: 2025-10-30 23:31:17.224646
# Keep-alive comment: 2025-10-31 09:32:31.308569
# Keep-alive comment: 2025-10-31 19:31:06.443119
# Keep-alive comment: 2025-11-01 05:31:15.193382
# Keep-alive comment: 2025-11-01 15:31:04.225718
# Keep-alive comment: 2025-11-02 01:31:16.264655
# Keep-alive comment: 2025-11-02 11:31:17.580956
# Keep-alive comment: 2025-11-02 21:31:31.674636
# Keep-alive comment: 2025-11-03 07:31:12.371306
# Keep-alive comment: 2025-11-03 17:31:15.656547
# Keep-alive comment: 2025-11-04 03:31:15.875719
# Keep-alive comment: 2025-11-04 13:31:43.636818
# Keep-alive comment: 2025-11-04 23:31:35.565117
# Keep-alive comment: 2025-11-05 09:31:46.869670
# Keep-alive comment: 2025-11-05 19:31:16.263813
# Keep-alive comment: 2025-11-06 05:31:41.644909
# Keep-alive comment: 2025-11-06 15:31:29.379070
# Keep-alive comment: 2025-11-07 01:31:14.174099
# Keep-alive comment: 2025-11-07 11:31:18.998289
# Keep-alive comment: 2025-11-07 21:31:17.865042
# Keep-alive comment: 2025-11-08 07:31:05.392942
# Keep-alive comment: 2025-11-08 17:31:21.407541
# Keep-alive comment: 2025-11-09 03:31:55.372113
# Keep-alive comment: 2025-11-09 13:31:16.612482
# Keep-alive comment: 2025-11-09 23:31:06.789518
# Keep-alive comment: 2025-11-10 09:31:12.362243
# Keep-alive comment: 2025-11-10 19:31:28.298270
# Keep-alive comment: 2025-11-11 05:31:13.163171
# Keep-alive comment: 2025-11-11 15:31:10.963465
# Keep-alive comment: 2025-11-12 01:31:18.147197
# Keep-alive comment: 2025-11-12 11:31:20.110097
# Keep-alive comment: 2025-11-12 21:31:37.818078
# Keep-alive comment: 2025-11-13 07:31:00.547533
# Keep-alive comment: 2025-11-13 17:31:12.688080
# Keep-alive comment: 2025-11-14 03:31:18.855610
# Keep-alive comment: 2025-11-14 13:31:39.928131
# Keep-alive comment: 2025-11-14 23:31:11.624521
# Keep-alive comment: 2025-11-15 09:31:15.588027
# Keep-alive comment: 2025-11-15 19:31:20.912662
# Keep-alive comment: 2025-11-16 05:31:12.617022
# Keep-alive comment: 2025-11-16 15:31:16.742544
# Keep-alive comment: 2025-11-17 01:31:06.755704
# Keep-alive comment: 2025-11-17 11:31:40.452887
# Keep-alive comment: 2025-11-17 21:31:08.221564
# Keep-alive comment: 2025-11-18 07:31:11.069468
# Keep-alive comment: 2025-11-18 17:31:12.076249
# Keep-alive comment: 2025-11-19 03:31:14.898073
# Keep-alive comment: 2025-11-19 13:31:07.666425
# Keep-alive comment: 2025-11-19 23:31:09.153779
# Keep-alive comment: 2025-11-20 09:31:17.020693
# Keep-alive comment: 2025-11-20 19:33:06.753111
# Keep-alive comment: 2025-11-21 05:31:12.639864
# Keep-alive comment: 2025-11-21 15:31:17.201435
# Keep-alive comment: 2025-11-22 01:31:21.107521
# Keep-alive comment: 2025-11-22 11:31:06.018447
# Keep-alive comment: 2025-11-22 21:31:16.597949
# Keep-alive comment: 2025-11-23 07:31:17.415318
# Keep-alive comment: 2025-11-23 17:31:20.454485
# Keep-alive comment: 2025-11-24 03:31:10.871707
# Keep-alive comment: 2025-11-24 13:31:07.233591
# Keep-alive comment: 2025-11-24 23:31:17.363046
# Keep-alive comment: 2025-11-25 09:31:39.253208
# Keep-alive comment: 2025-11-25 19:31:13.468102
# Keep-alive comment: 2025-11-26 05:31:24.334064
# Keep-alive comment: 2025-11-26 15:31:23.399355
# Keep-alive comment: 2025-11-27 01:31:16.936825
# Keep-alive comment: 2025-11-27 11:31:13.512860
# Keep-alive comment: 2025-11-27 21:31:07.168007
# Keep-alive comment: 2025-11-28 07:31:05.639809
# Keep-alive comment: 2025-11-28 17:31:17.605748
# Keep-alive comment: 2025-11-29 03:31:11.689991
# Keep-alive comment: 2025-11-29 13:31:22.107564
# Keep-alive comment: 2025-11-29 23:31:11.790144
# Keep-alive comment: 2025-11-30 09:31:13.583829
# Keep-alive comment: 2025-11-30 19:31:02.153628
# Keep-alive comment: 2025-12-01 05:31:01.766188
# Keep-alive comment: 2025-12-01 15:31:08.544405
# Keep-alive comment: 2025-12-02 01:30:51.813059
# Keep-alive comment: 2025-12-02 11:31:14.156702
# Keep-alive comment: 2025-12-02 21:31:16.770865
# Keep-alive comment: 2025-12-03 07:31:13.931336
# Keep-alive comment: 2025-12-03 17:31:21.524540
# Keep-alive comment: 2025-12-04 03:31:11.296105
# Keep-alive comment: 2025-12-04 13:31:09.213837
# Keep-alive comment: 2025-12-04 23:31:11.223050
# Keep-alive comment: 2025-12-05 09:31:11.550192
# Keep-alive comment: 2025-12-05 19:31:06.176348
# Keep-alive comment: 2025-12-06 05:31:11.839207
# Keep-alive comment: 2025-12-06 15:30:58.709801
# Keep-alive comment: 2025-12-07 01:31:07.965348
# Keep-alive comment: 2025-12-07 11:31:11.390057
# Keep-alive comment: 2025-12-07 21:31:07.686770
# Keep-alive comment: 2025-12-08 07:31:20.985858
# Keep-alive comment: 2025-12-08 17:31:06.969644
# Keep-alive comment: 2025-12-09 03:31:11.070091
# Keep-alive comment: 2025-12-09 13:31:10.215526
# Keep-alive comment: 2025-12-09 23:31:11.932119
# Keep-alive comment: 2025-12-10 09:31:13.236292
# Keep-alive comment: 2025-12-10 19:31:17.707104
# Keep-alive comment: 2025-12-11 05:30:52.295196
# Keep-alive comment: 2025-12-11 15:31:14.703210
# Keep-alive comment: 2025-12-12 01:31:11.238170
# Keep-alive comment: 2025-12-12 11:30:58.068619
# Keep-alive comment: 2025-12-12 21:31:16.989640
# Keep-alive comment: 2025-12-13 07:31:10.514948
# Keep-alive comment: 2025-12-13 17:31:12.541898
# Keep-alive comment: 2025-12-14 03:31:14.971445
# Keep-alive comment: 2025-12-14 13:31:10.196179
# Keep-alive comment: 2025-12-14 23:31:05.441683
# Keep-alive comment: 2025-12-15 09:31:11.045591
# Keep-alive comment: 2025-12-15 19:31:10.861769
# Keep-alive comment: 2025-12-16 05:31:18.312070
# Keep-alive comment: 2025-12-16 15:31:06.962419
# Keep-alive comment: 2025-12-17 01:31:37.776239
# Keep-alive comment: 2025-12-17 11:31:05.812612
# Keep-alive comment: 2025-12-17 21:34:21.734200
# Keep-alive comment: 2025-12-18 07:31:12.763568
# Keep-alive comment: 2025-12-18 17:31:22.509247
# Keep-alive comment: 2025-12-19 03:31:18.269668
# Keep-alive comment: 2025-12-19 13:31:12.639212
# Keep-alive comment: 2025-12-19 23:31:49.975244
# Keep-alive comment: 2025-12-20 09:30:56.490513
# Keep-alive comment: 2025-12-20 19:31:11.475549
# Keep-alive comment: 2025-12-21 05:31:09.939537
# Keep-alive comment: 2025-12-21 15:30:54.996623
# Keep-alive comment: 2025-12-22 01:31:09.180668
# Keep-alive comment: 2025-12-22 11:31:12.254315
# Keep-alive comment: 2025-12-22 21:30:56.180861
# Keep-alive comment: 2025-12-23 07:31:13.405939
# Keep-alive comment: 2025-12-23 17:31:15.167928
# Keep-alive comment: 2025-12-24 03:31:01.942088
# Keep-alive comment: 2025-12-24 13:30:57.103739
# Keep-alive comment: 2025-12-24 23:31:03.468737
# Keep-alive comment: 2025-12-25 09:31:17.351530
# Keep-alive comment: 2025-12-25 19:31:11.987541
# Keep-alive comment: 2025-12-26 05:31:11.137379
# Keep-alive comment: 2025-12-26 15:31:10.456825
# Keep-alive comment: 2025-12-27 01:31:04.703473
# Keep-alive comment: 2025-12-27 11:31:09.250047
# Keep-alive comment: 2025-12-27 21:31:10.706110
# Keep-alive comment: 2025-12-28 07:31:10.188077
# Keep-alive comment: 2025-12-28 17:31:17.318947
# Keep-alive comment: 2025-12-29 03:31:05.142182
# Keep-alive comment: 2025-12-29 13:31:11.705618
# Keep-alive comment: 2025-12-29 23:31:06.363819
# Keep-alive comment: 2025-12-30 09:30:56.263832
# Keep-alive comment: 2025-12-30 19:31:14.851217
# Keep-alive comment: 2025-12-31 05:31:07.166357
# Keep-alive comment: 2025-12-31 15:31:08.197453
# Keep-alive comment: 2026-01-01 01:31:17.253222
# Keep-alive comment: 2026-01-01 11:31:12.070664
# Keep-alive comment: 2026-01-01 21:31:23.253614
# Keep-alive comment: 2026-01-02 07:31:13.360101
# Keep-alive comment: 2026-01-02 17:31:11.230018
# Keep-alive comment: 2026-01-03 03:31:08.316133
# Keep-alive comment: 2026-01-03 13:31:13.352599
# Keep-alive comment: 2026-01-03 23:31:15.017015
# Keep-alive comment: 2026-01-04 09:31:07.128580
# Keep-alive comment: 2026-01-04 19:31:13.225366
# Keep-alive comment: 2026-01-05 05:31:11.575483
# Keep-alive comment: 2026-01-05 15:31:17.330141
# Keep-alive comment: 2026-01-06 01:31:06.789279
# Keep-alive comment: 2026-01-06 11:31:08.145833
# Keep-alive comment: 2026-01-06 21:31:07.053583
# Keep-alive comment: 2026-01-07 07:31:06.462358
# Keep-alive comment: 2026-01-07 17:31:06.441337
# Keep-alive comment: 2026-01-08 03:31:14.213665
# Keep-alive comment: 2026-01-08 13:31:08.451919
# Keep-alive comment: 2026-01-08 23:31:06.065262
# Keep-alive comment: 2026-01-09 09:31:07.136024
# Keep-alive comment: 2026-01-09 19:31:11.852094
# Keep-alive comment: 2026-01-10 05:31:15.707094
# Keep-alive comment: 2026-01-10 15:31:00.515457
# Keep-alive comment: 2026-01-11 01:31:08.127801
# Keep-alive comment: 2026-01-11 11:31:16.391983
# Keep-alive comment: 2026-01-11 21:31:10.770575
# Keep-alive comment: 2026-01-12 07:31:13.462162
# Keep-alive comment: 2026-01-12 17:31:10.599623
# Keep-alive comment: 2026-01-13 03:31:08.282553
# Keep-alive comment: 2026-01-13 13:31:02.892544
# Keep-alive comment: 2026-01-13 23:31:15.329290
# Keep-alive comment: 2026-01-14 09:31:08.279792
# Keep-alive comment: 2026-01-14 19:31:11.850050
# Keep-alive comment: 2026-01-15 05:31:11.307246
# Keep-alive comment: 2026-01-15 15:31:19.692430
# Keep-alive comment: 2026-01-16 01:31:15.123028
# Keep-alive comment: 2026-01-16 11:31:22.595025
# Keep-alive comment: 2026-01-16 21:31:10.085596
# Keep-alive comment: 2026-01-17 07:30:55.189733
# Keep-alive comment: 2026-01-17 17:31:10.031901
# Keep-alive comment: 2026-01-18 03:31:11.448716
# Keep-alive comment: 2026-01-18 13:31:06.828446
# Keep-alive comment: 2026-01-18 23:31:16.037831
# Keep-alive comment: 2026-01-19 09:31:14.734324
# Keep-alive comment: 2026-01-19 19:31:09.552540
# Keep-alive comment: 2026-01-20 05:31:05.481922
# Keep-alive comment: 2026-01-20 15:31:12.331683
# Keep-alive comment: 2026-01-21 01:31:10.399398
# Keep-alive comment: 2026-01-21 11:31:07.822120
# Keep-alive comment: 2026-01-21 21:31:13.173991
# Keep-alive comment: 2026-01-22 07:31:13.282742
# Keep-alive comment: 2026-01-22 17:31:04.635937
# Keep-alive comment: 2026-01-23 03:31:46.581606
# Keep-alive comment: 2026-01-23 13:31:19.324490
# Keep-alive comment: 2026-01-23 23:31:12.615989
# Keep-alive comment: 2026-01-24 09:31:21.583198
# Keep-alive comment: 2026-01-24 19:31:14.000855
# Keep-alive comment: 2026-01-25 05:31:07.086080
# Keep-alive comment: 2026-01-25 15:31:16.924657
# Keep-alive comment: 2026-01-26 01:31:12.113221
# Keep-alive comment: 2026-01-26 11:31:12.509696
# Keep-alive comment: 2026-01-26 21:31:16.048714
# Keep-alive comment: 2026-01-27 07:31:14.424745
# Keep-alive comment: 2026-01-27 17:31:17.575571
# Keep-alive comment: 2026-01-28 03:31:12.379789
# Keep-alive comment: 2026-01-28 13:31:14.072912
# Keep-alive comment: 2026-01-28 23:32:35.740956
# Keep-alive comment: 2026-01-29 09:31:16.229748
# Keep-alive comment: 2026-01-29 19:31:04.420306
# Keep-alive comment: 2026-01-30 05:30:56.295005
# Keep-alive comment: 2026-01-30 15:31:12.623857
# Keep-alive comment: 2026-01-31 01:31:18.040029
# Keep-alive comment: 2026-01-31 11:31:14.885466
# Keep-alive comment: 2026-01-31 21:31:14.001910
# Keep-alive comment: 2026-02-01 07:31:18.944832
# Keep-alive comment: 2026-02-01 17:31:11.809846
# Keep-alive comment: 2026-02-02 03:31:25.254303
# Keep-alive comment: 2026-02-02 13:31:26.633781
# Keep-alive comment: 2026-02-02 23:32:22.210733
# Keep-alive comment: 2026-02-03 09:31:14.997270
# Keep-alive comment: 2026-02-03 19:32:35.959376
# Keep-alive comment: 2026-02-04 05:31:17.845465
# Keep-alive comment: 2026-02-04 15:31:18.813709
# Keep-alive comment: 2026-02-05 01:31:13.204743
# Keep-alive comment: 2026-02-05 11:31:14.786007
# Keep-alive comment: 2026-02-05 21:31:19.971787
# Keep-alive comment: 2026-02-06 07:31:05.010650
# Keep-alive comment: 2026-02-06 17:31:17.237002
# Keep-alive comment: 2026-02-07 03:31:14.848497
# Keep-alive comment: 2026-02-07 13:31:18.099170
# Keep-alive comment: 2026-02-07 23:30:54.603530
# Keep-alive comment: 2026-02-08 09:31:17.286826
# Keep-alive comment: 2026-02-08 19:31:19.380198
# Keep-alive comment: 2026-02-09 05:31:26.255072
# Keep-alive comment: 2026-02-09 15:31:28.753221
# Keep-alive comment: 2026-02-10 01:31:04.578237
# Keep-alive comment: 2026-02-10 11:31:20.953378
# Keep-alive comment: 2026-02-10 21:31:24.722024
# Keep-alive comment: 2026-02-11 07:31:20.243569
# Keep-alive comment: 2026-02-11 17:31:20.150048
# Keep-alive comment: 2026-02-12 03:31:20.611583
# Keep-alive comment: 2026-02-12 13:31:25.855608
# Keep-alive comment: 2026-02-12 23:35:24.010364
# Keep-alive comment: 2026-02-13 09:31:24.840000
# Keep-alive comment: 2026-02-13 19:31:23.185540
# Keep-alive comment: 2026-02-14 05:31:11.343112
# Keep-alive comment: 2026-02-14 15:30:55.808664
# Keep-alive comment: 2026-02-15 01:31:17.962807
# Keep-alive comment: 2026-02-15 11:31:10.218267
# Keep-alive comment: 2026-02-15 21:31:11.582774
# Keep-alive comment: 2026-02-16 07:31:06.775126
# Keep-alive comment: 2026-02-16 17:31:06.595679
# Keep-alive comment: 2026-02-17 03:31:11.228541
# Keep-alive comment: 2026-02-17 13:31:38.231729
# Keep-alive comment: 2026-02-17 23:31:13.233147
# Keep-alive comment: 2026-02-18 09:32:42.650360
# Keep-alive comment: 2026-02-18 19:31:45.058009
# Keep-alive comment: 2026-02-19 05:31:06.493373
# Keep-alive comment: 2026-02-19 15:31:39.131223
# Keep-alive comment: 2026-02-20 01:31:06.606688
# Keep-alive comment: 2026-02-20 11:31:08.163456
# Keep-alive comment: 2026-02-20 21:32:06.406438
# Keep-alive comment: 2026-02-21 07:31:37.245809
# Keep-alive comment: 2026-02-21 17:31:36.789418
# Keep-alive comment: 2026-02-22 03:31:37.694415
# Keep-alive comment: 2026-02-22 13:31:37.897235
# Keep-alive comment: 2026-02-22 23:31:35.161624
# Keep-alive comment: 2026-02-23 09:31:05.990467
# Keep-alive comment: 2026-02-23 19:31:37.211775
# Keep-alive comment: 2026-02-24 05:31:14.808606
# Keep-alive comment: 2026-02-24 15:31:47.984598
# Keep-alive comment: 2026-02-25 01:31:43.354155
# Keep-alive comment: 2026-02-25 11:32:08.667939
# Keep-alive comment: 2026-02-25 21:31:13.759130
# Keep-alive comment: 2026-02-26 07:31:13.586026
# Keep-alive comment: 2026-02-26 17:31:46.312663
# Keep-alive comment: 2026-02-27 03:31:44.860418
# Keep-alive comment: 2026-02-27 13:31:45.451851
# Keep-alive comment: 2026-02-27 23:31:11.568935
# Keep-alive comment: 2026-02-28 09:31:12.548057
# Keep-alive comment: 2026-02-28 19:31:07.326835
# Keep-alive comment: 2026-03-01 05:31:40.964957