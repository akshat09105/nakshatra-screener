import streamlit as st
from database.db import get_companies

st.set_page_config(
    page_title="Nakshatra Stock Screener",
    page_icon="📈",
    layout="wide"
)

# ----------------------------
# Load Data
# ----------------------------
df = get_companies()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("Filters")

nakshatra = st.sidebar.selectbox(
    "Nakshatra",
    ["All"] + sorted(df["nakshatra_name"].dropna().unique().tolist())
)

nakshatra_owner = st.sidebar.selectbox(
    "Nakshatra Owner",
    ["All"] + sorted(df["nakshatra_owner"].dropna().unique().tolist())
)

rashi = st.sidebar.selectbox(
    "Rashi",
    ["All"] + sorted(df["rashi"].dropna().unique().tolist())
)

rashi_owner = st.sidebar.selectbox(
    "Rashi Owner",
    ["All"] + sorted(df["rashi_owner"].dropna().unique().tolist())
)

sector = st.sidebar.selectbox(
    "Sector",
    ["All"] + sorted(df["sector"].dropna().unique().tolist())
)

sector_karak = st.sidebar.selectbox(
    "Sector Karak Planet",
    ["All"] + sorted(df["sector_karak"].dropna().unique().tolist())
)

company_search = st.sidebar.text_input("Search Company")

# ----------------------------
# Filtering
# ----------------------------
filtered_df = df.copy()

if nakshatra != "All":
    filtered_df = filtered_df[
        filtered_df["nakshatra_name"] == nakshatra
    ]

if nakshatra_owner != "All":
    filtered_df = filtered_df[
        filtered_df["nakshatra_owner"] == nakshatra_owner
    ]

if rashi != "All":
    filtered_df = filtered_df[
        filtered_df["rashi"] == rashi
    ]

if rashi_owner != "All":
    filtered_df = filtered_df[
        filtered_df["rashi_owner"] == rashi_owner
    ]

if sector != "All":
    filtered_df = filtered_df[
        filtered_df["sector"] == sector
    ]

if sector_karak != "All":
    filtered_df = filtered_df[
        filtered_df["sector_karak"] == sector_karak
    ]

if company_search:
    filtered_df = filtered_df[
        filtered_df["company_name"].str.contains(
            company_search,
            case=False,
            na=False
        )
    ]

# ----------------------------
# Main Page
# ----------------------------
st.title("📈 Nakshatra Stock Screener")

st.write(f"### Companies Found : {len(filtered_df)}")

st.dataframe(
    filtered_df.reset_index(drop=True),
    use_container_width=True,
    hide_index=True
)