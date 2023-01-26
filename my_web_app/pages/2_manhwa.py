# 리팩토링(refactoring)


import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

manhwa_select = ['짱구', '안녕자두야', '스폰지밥']

manhwa_select_option = st.sidebar.selectbox('좋아하는 만화를 선택하세요', manhwa_select, index=0)


# 본문
folder = './data/'

manhwa_image_files = ['짱구.jpg', '안녕자두야.jpg', '스폰지밥.jpg']

# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
st.header(manhwa_select_option)


manhwa_select_index = manhwa_select.index(manhwa_select_option)

st.write(manhwa_select_index)
st.image(folder + manhwa_image_files[manhwa_select_index])