import pandas as pd
import plotly.express as px
import streamlit as st


# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide",
)

DATA_URL = (
    "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"
)


# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 날짜: 20250901 -> 2025-09-01
    df["날짜"] = pd.to_datetime(
        df["날짜"].astype(str),
        format="%Y%m%d",
    )

    # 숫자형 열을 명시적으로 숫자로 변환
    numeric_columns = [
        "순위",
        "영화코드",
        "일관객",
        "누적관객",
        "스크린수",
        "상영횟수",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


df = load_data()


# --------------------------------------------------
# 제목
# --------------------------------------------------
st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.markdown(
    "1년치 일별 박스오피스 데이터를 이용해 영화의 시간에 따른 관객 변화를 살펴봅니다."
)


# ==================================================
# 그래프 1
# ==================================================
st.divider()
st.header("그래프 1. 영화별 일관객 변화")

st.write(
    "영화를 하나 선택하면 해당 영화가 박스오피스 10위권에 기록된 날짜의 "
    "일관객 변화를 확인할 수 있습니다."
)

# 영화 목록
movie_names = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
    "영화를 선택하세요",
    movie_names,
)

# 선택한 영화 데이터
movie_df = (
    df[df["영화명"] == selected_movie]
    .sort_values("날짜")
    .copy()
)

# Plotly 선 그래프
fig = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    title=f"{selected_movie} - 날짜별 일관객",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수",
    },
)

fig.update_traces(
    hovertemplate="날짜: %{x|%Y-%m-%d}<br>관객수: %{y:,}명<extra></extra>",
)

fig.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수",
)

st.plotly_chart(
    fig,
    width="stretch",
)

st.markdown("**이 그래프로 알 수 있는 것**")
st.write(
    f"{selected_movie}의 일별 관객수가 시간에 따라 어떻게 증가하거나 감소했는지 확인할 수 있습니다."
)


# ==================================================
# 앞으로 추가할 그래프 영역
# ==================================================
st.divider()
st.header("그래프 2. 다음 그래프")
st.info("여기에 두 번째 그래프를 추가하세요.")


st.divider()
st.header("그래프 3. 다음 그래프")
st.info("여기에 세 번째 그래프를 추가하세요.")


st.divider()
st.header("그래프 4. 다음 그래프")
st.info("여기에 네 번째 그래프를 추가하세요.")
