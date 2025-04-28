import streamlit as st
import altair as alt
import pandas as pd
import vis_1
import vis_2

st.title("Electric Vehicle Dashboard - Washington, US")

st.header('Average Electric Range by EV Model and Type')
st.altair_chart(vis_1.range_plot(), use_container_width=True)
st.header('EV Type Distribution Across Counties')
st.altair_chart(vis_2.county_plot(), use_container_width=True)
