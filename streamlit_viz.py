import streamlit as st
import pandas as pd

st.title("Health risk and Chulha use in Rajasthan")

st.markdown("We analyzed data from 2293 individuals collected across 9 health facilities in the Alwar district of Rajasthan.")


#CHULHA USE BAR CHART

st.subheader("Chulha use (Yes/No) by health facility and block")

chulha_count = pd.read_csv("chulha_count.csv")

health_facilities = chulha_count["Health Facility"].unique()

facility_choice = st.sidebar.multiselect("Choose facility:", health_facilities, default=health_facilities)

chulha_count = chulha_count[chulha_count["Health Facility"].isin(facility_choice)]

st.bar_chart(chulha_count, x="Health Facility", y="Count", color="Chulha Use")

#SCREENED COUNT TABLE

st.subheader("Table of number screened by health facility and block")

screened_count = pd.read_csv("screened_count.csv")


st.dataframe(screened_count)

#MEAN RISK SCORE TABLE

st.subheader("Table of mean risk score by health facility and block")

mean_risk = pd.read_csv("mean_risk.csv")

st.dataframe(mean_risk)
