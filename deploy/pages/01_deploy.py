import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import datetime

def get_stock_info(maket_type=None):
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    if maket_type == 'kospi':         
        marketType = "stockMkt"      
    elif maket_type == 'kosdaq':
        marketType = "kosdaqMkt"    
    elif maket_type == None:         
        marketType = ""
    url = "{0}?method={1}&marketType={2}".format(base_url, method, marketType)     
    df = pd.read_html(url, header=0)[0]
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
    df = df[['회사명','종목코드']]
    return df

def get_ticker_symbol(company_name, maket_type):     
    df = get_stock_info(maket_type)
    code = df[df['회사명']==company_name]['종목코드'].values    
    code = code[0]
    if maket_type == 'kospi':   
        ticker_symbol = code +".KS"     
    elif maket_type == 'kosdaq':      
        ticker_symbol = code +".KQ" 
    return ticker_symbol



#사이드바, input text, 시작일과 종료일
st.sidebar.header('회사 이름과 기간 입력')
title = st.sidebar.text_input('회사이름', 'NAVER')
date_range = st.sidebar.date_input("시작일과 종료일",[])
button = st.sidebar.button("주가 데이터 가져오기")


# 코드 조각 추가
st.write('# 주식 정보를 가져오는 웹 앱')

if button:
    ticker_symbol = get_ticker_symbol(title, "kospi")     
    ticker_data = yf.Ticker(ticker_symbol)
    start_p = date_range[0]               
    end_p = date_range[1] + datetime.timedelta(days=1) 
    df = ticker_data.history(start=start_p, end=end_p)
    df.index = df.index.date
    st.subheader(f"[{title}] 주가 데이터")
    st.dataframe(df.head())
    st.line_chart(df)

    st.write('#### 주가 데이터 파일 다운로드')
    

    [col1, col2] = st.columns(2)
    with col1:
        csv_data = df.to_csv().encode('utf-8')
        st.download_button(
        label="csv 파일 저장",
        data=csv_data,
        file_name='주가 데이터.csv')

    with col2:
        excel_data = BytesIO()
        st.download_button(
        label="excel 파일 저장",
        data=excel_data,
        file_name='주가 데이터.xlsx')
        




