import streamlit as st

st.title("숫자 카운터")

if "count" not in st.session_state: # Streamlit에서 값을 저장하는 공간
    st.session_state.count = 0

if st.button("숫자 증가"):
    st.session_state.count += 1

if st.button("초기화"):
    st.session_state.count = 0

st.write(f"현재 숫자: {st.session_state.count}") # 화면에 내용을 출력하는 함수