import streamlit as st
import streamlit.components.v1 as components
import os

# 페이지 기본 설정 (가로 너비 최대화, 타이틀 설정)
st.set_page_config(
    page_title="Comp Envelop Analyzer V3.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Streamlit 기본 여백 제거 CSS (HTML 앱이 꽉 차게 표시되도록 처리)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100%;
        }
        iframe {
            border: none;
            width: 100% !important;
            height: 100vh !important;
        }
    </style>
""", unsafe_allow_html=True)

# 02_Envelop_Web.html 파일 읽기
html_file_path = os.path.join(os.path.dirname(__file__), "02_Envelop_Web.html")

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    # 전체 뷰포트 높이(100vh)를 고려하여 렌더링
    components.html(html_content, height=940, scrolling=True)
else:
    st.error(f"'{html_file_path}' 파일을 찾을 수 없습니다. 저장소 파일 위치를 확인해 주세요.")