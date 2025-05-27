import streamlit as st

universities = {
    "서울대학교": {"score_range": "1~2등급", "location": "서울 관악구"},
    "연세대학교": {"score_range": "2~3등급", "location": "서울 서대문구"},
    "고려대학교": {"score_range": "2~3등급", "location": "서울 성북구"},
    "한양대학교": {"score_range": "3~4등급", "location": "서울 성동구"},
    "성균관대학교": {"score_range": "3~4등급", "location": "서울 종로구"},
    "중앙대학교": {"score_range": "4~5등급", "location": "서울 동작구"},
    "경희대학교": {"score_range": "4~5등급", "location": "서울 동대문구"},
    "이화여자대학교": {"score_range": "3~4등급", "location": "서울 서대문구"},
    "부산대학교": {"score_range": "4~5등급", "location": "부산 금정구"},
    "경북대학교": {"score_range": "4~5등급", "location": "대구 북구"},
    "전북대학교": {"score_range": "5~6등급", "location": "전북 전주"},
    "충남대학교": {"score_range": "5~6등급", "location": "대전 유성구"},
    "강원대학교": {"score_range": "6~7등급", "location": "강원 춘천"},
    "광운대학교": {"score_range": "5~6등급", "location": "서울 노원구"},
    "건국대학교": {"score_range": "5~6등급", "location": "서울 광진구"},
    "홍익대학교": {"score_range": "5~6등급", "location": "서울 마포구"},
    "숙명여자대학교": {"score_range": "5~6등급", "location": "서울 용산구"},
    "세종대학교": {"score_range": "6~7등급", "location": "서울 광진구"},
    "부경대학교": {"score_range": "6~7등급", "location": "부산 남구"},
    "조선대학교": {"score_range": "6~7등급", "location": "광주 동구"},
}

st.title("한국 대학 순위별 정보")

st.write("아래에서 대학을 선택하면 수능 점수대와 위치 정보를 보여줍니다.")

selected_univ = st.selectbox("대학을 선택하세요", list(universities.keys()))

info = universities[selected_univ]

st.subheader(f"{selected_univ} 정보")
st.write(f"- 수능 점수대: {info['score_range']}")
st.write(f"- 위치: {info['location']}")
