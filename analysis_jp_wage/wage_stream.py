import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk

import plotly.express as px


st.title('日本の賃金データダッシュボード')

df_jp_ind = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_全国_全産業.csv', encoding='shift_jis')
df_jp_category = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_全国_大分類.csv', encoding='shift_jis')
df_pref_ind = pd.read_csv('./csv_data/雇用_医療福祉_一人当たり賃金_都道府県_全産業.csv', encoding='shift_jis')

### ■2019年：一人当たり平均賃金のヒートマップ
st.header('■2019年：一人当たり平均賃金のヒートマップ')

jp_lat_lon = pd.read_csv('./pref_lat_lon.csv')
jp_lat_lon = jp_lat_lon.rename(columns={'pref_name': '都道府県名'})
jp_lat_lon

df_pref_map = df_pref_ind[(df_pref_ind['年齢'] == '年齢計') & (df_pref_ind['集計年'] == 2019)]
df_pref_map = pd.merge(df_pref_map, jp_lat_lon, on = '都道府県名')
df_pref_map['一人当たり賃金（相対値）'] = ((df_pref_map['一人当たり賃金（万円）']-df_pref_map['一人当たり賃金（万円）'].min())/(df_pref_map['一人当たり賃金（万円）'].max()-df_pref_map['一人当たり賃金（万円）'].min()))

view = pdk.ViewState(
    longitude=139.691648,
    latitude=35.689185,
    zoom=4,
    pitch=40.5,
)

layer = pdk.Layer(
    "HeatmapLayer",
    data=df_pref_map,
    opacity=0.4,
    get_position=["lon", "lat"],
    threshold=0.3,
    get_weight = '一人当たり賃金（相対値）'
)

layer_map = pdk.Deck(
    layers=layer,
    initial_view_state=view,
)

st.pydeck_chart(layer_map)

show_df = st.checkbox('Show DataFrame')
if show_df:
    st.write(df_pref_map)

### ■2019年：一人当たり平均賃金のヒートマップ
st.header('■集計年別の一人当たり賃金(万円)の推移')

df_ts_mean = df_jp_ind[(df_jp_ind['年齢'] == "年齢計")]
df_ts_mean = df_ts_mean.rename(columns={'一人当たり賃金（万円）': '全国一人当たり賃金（万円）'})

df_pref_mean = df_pref_ind[df_pref_ind['年齢'] == "年齢計"]
pref_list = df_pref_ind['都道府県名'].unique()
option_pref = st.selectbox(
    '都道府県名',
    (pref_list)
)

df_pref_mean = df_pref_mean[df_pref_mean['都道府県名'] == option_pref]

df_mean_line = pd.merge(df_ts_mean, df_pref_mean, on='集計年')
df_mean_line = df_mean_line[['集計年', '全国一人当たり賃金（万円）','一人当たり賃金（万円）']]
df_mean_line = df_mean_line.set_index('集計年')
st.line_chart(df_mean_line)