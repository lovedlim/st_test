import streamlit as st
from datetime import datetime

st.title('Hello, World!')

st.write("안녕하세요! Streamlit 애플리케이션에 오신 것을 환영합니다.")

# 현재 시간 표시
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.write(f"현재 시간: {current_time}")
