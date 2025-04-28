# %%
# import packages
import altair as alt
import pandas as pd

alt.data_transformers.disable_max_rows()

# %% [markdown]
# # Question 2: How does EV type (Battery Electric Vehicles or Plug-in Hybrid Electric Vehicles) vary across counties? 

# %%
def county_plot():
    EV_df_county_clean = pd.read_csv('EV_df_county_clean.csv')
    county_bar_chart = alt.Chart(EV_df_county_clean).mark_bar().encode(
        x = alt.Y('count():Q', title = 'Number of Vehicles'), 
        y = alt.X('County:N', title = 'County', sort = '-x'), 
        color = alt.Color('Electric Vehicle Type:N', title = 'EV Type'),
        tooltip = [
            alt.Tooltip('County:N', title = 'County'), 
            alt.Tooltip('count():Q', title = 'Number of Vehicles'),
            alt.Tooltip('Electric Vehicle Type:N', title = 'EV Type')
            ]
            ).properties(
                title = 'Comparison of EV Types across Counties',
                width = 1000, 
                height = 800)
    return county_bar_chart
