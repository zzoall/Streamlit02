import streamlit as st

st.title("멀티페이지 웹 앱, 개별페이지 한단계 바깥에 저장해두면 자동으로 첫번재 페이지라고 인식함.")

# 숫자로 시작하는 파일은 일반 문자가 나올 때까지 숫자와 구분자 삭제(다만 숫자만 있는 파일 이름에서는 숫자 삭제 안 함)
# 구분자로 시작하는 파일 이름에서는 일반 숫자가 나올 때까지 구분자 삭제
# 일반 문자 사이에 있는 구분가는 하나의 공백으로 처리

st.subheader("사이드바에서 페이지를 선택하세요.")
st.subheader("chart1") 
st.subheader("chart2")
st.subheader("chart3") 
# st.markdown(     """     <style>
#     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width:250px;}</style>
#     """, unsafe_allow_html=True )