import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------------------------------
# 기본 설정
# ----------------------------------------------------------------------------
st.set_page_config(page_title="영화 데이터 그래프 도감 1 - 시간", layout="wide")
st.title("영화 데이터 그래프 도감 1 - 시간")

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 열 이름을 코드에서 다루기 쉬운 영문명으로 매핑
    df = df.rename(
        columns={
            "날짜": "date",
            "순위": "rank",
            "영화코드": "movie_code",
            "영화명": "movie_name",
            "일관객": "daily_audience",
            "누적관객": "cumulative_audience",
            "스크린수": "screens",
            "상영횟수": "showings",
        }
    )

    # 하이픈 없는 8자리 숫자 날짜(YYYYMMDD) -> datetime
    df["date"] = pd.to_datetime(df["date"].astype(str), format="%Y%m%d")

    return df


df = load_data()

st.divider()

# ----------------------------------------------------------------------------
# 구역 1. 영화별 일관객 수 변화 (시간에 따른 변화)
# ----------------------------------------------------------------------------
st.header("1. 영화별 일관객 수 변화")

movie_list = sorted(df["movie_name"].dropna().unique())
selected_movie = st.selectbox("영화를 선택하세요", movie_list, key="movie_select_1")

movie_df = df[df["movie_name"] == selected_movie].sort_values("date")

fig1 = px.line(
    movie_df,
    x="date",
    y="daily_audience",
    markers=True,
    labels={"date": "날짜", "daily_audience": "일 관객수"},
    title=f"'{selected_movie}' 일별 관객수 변화",
)
fig1.update_traces(
    hovertemplate="날짜: %{x|%Y-%m-%d}<br>일 관객수: %{y:,}명<extra></extra>"
)
fig1.update_layout(hovermode="x unified")

st.plotly_chart(fig1, use_container_width=True)

st.info("📌 이 그래프로 알 수 있는 것: (여기에 해석 문구를 입력하세요)")

st.divider()

# ----------------------------------------------------------------------------
# 구역 2. (다음 그래프를 위한 자리)
# ----------------------------------------------------------------------------
st.header("2. (다음 그래프)")
st.caption("여기에 다음 그래프를 추가할 예정입니다.")

st.divider()

# ----------------------------------------------------------------------------
# 구역 3. (다음 그래프를 위한 자리)
# ----------------------------------------------------------------------------
st.header("3. (다음 그래프)")
st.caption("여기에 다음 그래프를 추가할 예정입니다.")
