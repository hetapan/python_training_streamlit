# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import pydeck as pdk

# df = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['a','b','c']
# )
# df

# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# flg = plt.figure()
# ax = plt.axes()
# x = [105,210,300]
# y = [10,20,30]
# ax.plot(x,y)

# st.pyplot(flg)


### 35地図グラフの表示

# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# # pydeckを使用する
# import pydeck as pdk

# tokyo_lat = 35.69
# tokyo_lon = 139.69

# df_tokyo = pd.DataFrame(
#     np.random.randn(1000,2)/[50, 50]+[tokyo_lat, tokyo_lon],
#     columns=['lat', 'lon']
# )

# df_tokyo

# ## 3Dグラフの設定
# # viewの設定
# view = pdk.ViewState(latitude=tokyo_lat, longitude=tokyo_lon, pitch=50, zoom=11)

# # layerの設定
# hexagon_layer = pdk.Layer('HexagonLayer',
#     data=df_tokyo,
#     get_position = ['lon', 'lat'],
#     elevation_scale=6,
#     radius=200,
#     extruded=True
# )

# # deckの設定
# layer_map = pdk.Deck(layers=hexagon_layer, initial_view_state=view)

# # 描画
# st.pydeck_chart(layer_map)


### 36画像の表示
# import streamlit as st
# from PIL import Image

# image = Image.open('sample1.jpg')
# st.image(image, caption='サンプル1', use_column_width=True)

### インタラクティブ機能
import streamlit as st

option_button = st.button('ボタン')

if option_button:
    st.write('ボタンが押されました')
else:
    st.write('ボタンを押してください')

option_radio = st.radio("果物",('りんご','オレンジ'))

option_check = st.checkbox('ちぇっく')

option_select = st.selectbox(
    'どれか選択',
    ('aaa','bbb')
)

option_multiselect = st.multiselect(
    'どれか選択',
    ('aaa','bbb'),
    ('aaa')
)

option_slider = st.slider('貴方の年齢', min_value=0, max_value=50)

st.write(option_slider)

height = st.sidebar.slider('貴方の年齢aa', min_value=0, max_value=50)

