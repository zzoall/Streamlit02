
# 컬럼 2개, 선택된 드라마/만화 제목이 h1의 크기 파란색으로 나오도록 변경해보세요.
import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 사이드바 만드는 방법 1: st.sidebar.요소명 
# Using object notation
# 사이드바에 셀렉트박스(혹은 라디오버튼 등등 뭐라도 좋습니다)로 
# 각 드라마 혹은 애니메이션의 제목 세개를 
# 선택할 수 있도록 해주세요
drama_select = ['캐나다체크인', '또오해영', '검색어를 입력하세요 WWW']
manhwa_select = ['짱구', '안녕자두야', '스폰지밥']

# 인덱스 번호를 활용해서 두 요소를 연결해서 사용하고 있어요 
# 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
drama_select_option = st.sidebar.selectbox('좋아하는 드라마를 선택하세요', drama_select, index=0)
manhwa_select_option = st.sidebar.selectbox('좋아하는 만화를 선택하세요', manhwa_select, index=1)
# 사이드바 만드는 방법 2: with st.sidebar:
#                           변수명 = st.요소명 

# 본문
folder = './data/'

[col1, col2] = st.columns(2)


with col1:
    drama_image_files = ['캐나다체크인.jpg', '또오해영.jpg', 'WWW.jpg']

    html = """
    <style>
    h2 {
        color : blue;
    }
    <style>
    """
    st.markdown(html, unsafe_allow_html=True)

    # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
    st.header(drama_select_option)

    # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
    drama_select_index = drama_select.index(drama_select_option)

    st.write(drama_select_index)
    st.image(folder + drama_image_files[drama_select_index])




with col2:
    manhwa_image_files = ['짱구.jpg', '안녕자두야.jpg', '스폰지밥.jpg']

    # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
    st.header(manhwa_select_option)
    	
    # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
    manhwa_select_index = manhwa_select.index(manhwa_select_option)

    st.write(manhwa_select_index)
    st.image(folder + manhwa_image_files[manhwa_select_index])


# st.write('선택한 드라마:', drama_select_option)
# st.write('선택한 만화:', manhwa_select_option)



import cv2
import numpy as np
img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    # Check the type of cv2_img:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(cv2_img))
    # Check the shape of cv2_img:
    # Should output shape: (height, width, channels)
    st.write(cv2_img.shape)