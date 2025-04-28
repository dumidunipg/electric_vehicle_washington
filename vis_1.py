# %%
# import packages
import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()

# %% [markdown]
# # Question 1: What is the average electric range between Electric Vehicle Models by Battery Electric Vehicles and Plug-In Hybrid Electric Vehicles? 

# %%
def range_plot():
    EV_df = pd.read_csv('EV_Population_Clean.csv')
    EV_df_clean = EV_df.copy() # making a copy for cleaning
    EV_df_clean = EV_df_clean[EV_df_clean['Electric Range'].notna() & (EV_df_clean['Electric Range']>0)]
    bars = alt.Chart(EV_df_clean).mark_bar().encode(
        x = alt.X('average(Electric Range):Q', title = 'Average Electric Range'), 
        y = alt.Y('Model:N', sort = '-x'), 
        color = alt.Color('Electric Vehicle Type:N'),
        tooltip = [
            alt.Tooltip('Make:N'),
            alt.Tooltip('Model:N'),
            alt.Tooltip('average(Electric Range):Q', title = 'Average Electric Range (Miles)'),
            ]).properties(
                title = 'Average Electric Range by EV Model and Type')
    bar_chart = bars.facet(
        row = 'Electric Vehicle Type:N'
        ).resolve_scale(
            y ='independent', 
            x = 'independent'
            )
    return bar_chart



