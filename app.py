import streamlit as st

st.title("송정민 정보 보기")

# 정보 데이터
info = {
    "이름": "송정민",
    "생일": "3월 15일",
    "고등학교": "백신고등학교",
    "학번": "31011",
    "취미": "보드게임",
    "특징": "웃음소리가 매우 특이함"
}

# 사용자에게 보여줄 선택지
choice = st.selectbox("보고 싶은 정보를 선택하세요", list(info.keys()))

# 선택된 정보 출력
st.write(f"**{choice}**: {info[choice]}")
