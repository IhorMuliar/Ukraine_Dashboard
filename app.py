import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

data = pd.read_csv('data/API_UKR_DS2_en_csv_v2_2060461.csv')

data.drop(['Unnamed: 65', 'Country Name', 'Country Code'], axis=1, inplace=True)

gdp_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'NY.GDP.MKTP.CD'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
pd_gdp = pd.DataFrame(gdp_dict)
fig_gdp = go.Figure()
fig_gdp.add_trace(go.Scatter(x=pd_gdp.iloc[26:].years, 
                        y=pd_gdp.iloc[26:].value,
                        mode='lines+markers',
                        name='Gaps',
                        hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
                        line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_gdp.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=6,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "GDP (current US$)",
    },
    font=dict(
        size = 10,
    ),
    width=350, height=350,
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
    # margin=dict(l=500, r=20, t=50, b=20)
)

pop_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'SP.POP.TOTL'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
pop_dict = pd.DataFrame(pop_dict)
fig_pop = go.Figure()
fig_pop.add_trace(go.Scatter(x=pop_dict.years, 
                         y=pop_dict.value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_pop.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=8,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=8,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "Population, total",
    },
    font=dict(
        size = 10,
    ),    
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

school_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                        'value' : data[data['Indicator Code'] == 'SE.PRM.ENRR'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
school_dict = pd.DataFrame(school_dict)
fig_school = go.Figure()
fig_school.add_trace(go.Scatter(x=school_dict.iloc[11:55].years, 
                         y=school_dict.iloc[11:55].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_school.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=8,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "School enrollment, primary (% gross)",
    },
    font=dict(
        size = 10,
    ),      
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

co_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'EN.ATM.CO2E.PC'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
co_dict = pd.DataFrame(co_dict)
fig_co = go.Figure()
fig_co.add_trace(go.Scatter(x=co_dict.iloc[32:57].years, 
                         y=co_dict.iloc[32:57].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_co.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=7,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "CO2 emissions (metric tons per capita)",
    },
    font=dict(
        size = 10,
    ),     
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

poverty_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'SI.POV.NAHC'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
poverty_dict = pd.DataFrame(poverty_dict)
fig_poverty = go.Figure()
fig_poverty.add_trace(go.Scatter(x=poverty_dict.iloc[41:59].years, 
                         y=poverty_dict.iloc[41:59].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_poverty.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=8,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "Poverty headcount ratio (% of population)",
    },
    font=dict(
        size = 10,
    ),         
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

life_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'SP.DYN.LE00.IN'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
life_dict = pd.DataFrame(life_dict)
fig_life = go.Figure()
fig_life.add_trace(go.Scatter(x=life_dict.iloc[:60].years, 
                         y=life_dict.iloc[:60].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_life.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=7,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "Life expectancy at birth, total (years)",
    },
    font=dict(
        size = 10,
    ),      
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

gni_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'NY.GNP.PCAP.CD'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]}
gni_dict = pd.DataFrame(gni_dict)
fig_gni = go.Figure()
fig_gni.add_trace(go.Scatter(x=gni_dict.iloc[30:60].years, 
                         y=gni_dict.iloc[30:60].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_gni.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=8,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "GNI per capita, Atlas method (current US$)",
    },
    font=dict(
        size = 10,
    ),      
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

capacity_dict = {'years' : data.drop(['Indicator Name', 'Indicator Code'], axis=1).columns,
                      'value' : data[data['Indicator Code'] == 'IQ.SCI.OVRL'].drop(['Indicator Name', 'Indicator Code'], axis=1).to_numpy()[0]} 
capacity_dict = pd.DataFrame(capacity_dict)
fig_capacity = go.Figure()
fig_capacity.add_trace(go.Scatter(x=capacity_dict.iloc[44:].years, 
                         y=capacity_dict.iloc[44:].value,
                         mode='lines+markers',
                         hovertemplate='Ukraine (%{x})'+'<br>%{y}<extra></extra>',
#                          texttemplate="Ukraine (%{x}) <br>(%{y})",
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         )))

fig_capacity.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=8,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    title={
        'text' : "Statistical Capacity score (Overall average)",
    },
    font=dict(
        size = 10,
    ),     
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    width=350, height=350,
    autosize=False,
    showlegend=False,
    plot_bgcolor='white',
#     margin=dict(
#         autoexpand=False,
#         l=500,
#         r=20,
#         t=110,
#     ),
)

#Climate

temp_data = pd.read_csv('data/tas_1991_2016_UKR.csv')
rain_data = pd.read_csv('data/pr_1991_2016_UKR.csv')
temp_pivot = pd.pivot_table(temp_data, values='Temperature - (Celsius)', columns=' Statistics',
                             aggfunc={'Temperature - (Celsius)': np.mean})
rain_pivot = pd.pivot_table(rain_data, values='Rainfall - (MM)', columns=' Statistics',
                             aggfunc={'Rainfall - (MM)': np.mean})
rain_data_dict = {
    'month' : rain_pivot.columns,
    'value' : rain_pivot.values[0]
}
temp_data_dict = {
    'month' : temp_pivot.columns,
    'value' : temp_pivot.values[0]
}
temp_data_plot = pd.DataFrame(temp_data_dict)
rain_data_plot = pd.DataFrame(rain_data_dict)
temp_data_plot = temp_data_plot.reindex([4, 3, 7, 0, 8, 6, 5, 1, 11, 10, 9, 2])
rain_data_plot = rain_data_plot.reindex([4, 3, 7, 0, 8, 6, 5, 1, 11, 10, 9, 2])
rain_data_plot['month'] = rain_data_plot['month'].map(lambda x: x.rstrip('Average'))
temp_data_plot['month'] = temp_data_plot['month'].map(lambda x: x.rstrip('Average'))
fig_climate = make_subplots(specs=[[{"secondary_y": True}]])

fig_climate.add_trace(
    go.Scatter(
        x=temp_data_plot['month'], 
        y=temp_data_plot['value'],
        name="Temperature",
        mode='lines+markers',
        hovertemplate='%{x}'+'<br>%{y} °C<extra></extra>',
        line=dict(width=2,color='black'),
        yaxis = 'y2'
    ),
    secondary_y=True,
)

fig_climate.add_trace(
    go.Bar(
        x=rain_data_plot['month'], 
        y=rain_data_plot['value'],
        name="Rainfall",
        hovertemplate='%{x}'+'<br>%{y} mm<extra></extra>',
        marker_color='rgb(124, 181, 236)',
        width=0.5,
    ),
    secondary_y=False,
)

fig_climate.update_layout(
    xaxis=dict(
        fixedrange=True,
        showline=False,
        showgrid=False,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=12,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        )
    ),
    
    yaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    
    yaxis2 = dict(
        fixedrange=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
    ),
    
    
    hoverlabel=dict(
        bgcolor="rgb(200, 200, 200)",
        font_size=16,
        font_family="Arial"
    ),
    plot_bgcolor='white',
    
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-0.3,
    xanchor="center",
    x=0.5),
    margin_pad=10,
    title_text="Average Monthly Temperature and Rainfall of Ukraine for 1991-2016",
    hovermode  = 'x',
    spikedistance =  -1,
)

fig_climate.update_yaxes(title_text="Rainfall", secondary_y=False)
fig_climate.update_yaxes(title_text="Temperature", secondary_y=True)

crime_data = pd.read_csv('data/ukraine-crime-rate-statistics.csv')
trace1 = go.Scatter(x=crime_data['date'], 
                         y=crime_data[' Per 100K Population'],
                         mode='lines+markers',
                         hovertemplate='<br>%{y}<extra></extra>',
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         ),)

trace2 = go.Bar(x=crime_data['date'], 
                         y=crime_data[' Annual % Change'],
                         hovertemplate='<br>%{y}<extra></extra>',
                         xaxis="x2", yaxis="y2",
                         marker_color='indianred')

data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        fixedrange=True,
        zeroline=False,
        showticklabels=False,
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis=dict(
        domain=[0.4, 1],
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title_text="Per 100K Population"
    ),
    
    xaxis2=dict(      
        anchor="y2",
        fixedrange=True,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=12,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=13,
            color='rgb(82, 82, 82)',
        ),
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis2=dict(
        domain=[0, 0.3],
        fixedrange=True,
        zeroline=True,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title="Annual % Change",
    ),    
    
    barmode='overlay',
    
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ),
    plot_bgcolor='white',
    showlegend = False,
    hovermode  = 'x',
    spikedistance =  -1,
    
)
fig_crime = go.Figure(data=data, layout=layout)

health_data = pd.read_csv('data/ukraine-healthcare-spending.csv')
smoker_data = pd.read_csv('data/ukraine-smoking-rate-statistics.csv')

trace1 = go.Scatter(x=health_data['date'], 
                         y=health_data[' Per Capita (US $)'],
                         mode='lines+markers',
                         hovertemplate='<br>%{y}<extra></extra>',
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         ),)

trace2 = go.Scatter(x=health_data['date'], 
                         y=health_data[' % of GDP'],
                         mode='lines+markers',
                         hovertemplate='<br>%{y}<extra></extra>',
                         xaxis="x2", yaxis="y2",
                         line=dict(
                         width=2,
                         color='rgb(101, 145, 212)'
                         ),)

data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        fixedrange=True,
        zeroline=False,
        showticklabels=False,
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis=dict(
        domain=[0.6, 1],
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title_text="Per Capita (US $)"
    ),
    
    xaxis2=dict(       
        anchor="y2",
        fixedrange=True,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=12,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=13,
            color='rgb(82, 82, 82)',
        ),
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis2=dict(
        domain=[0, 0.4],
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title=" % of GDP",
    ),    
    
    barmode='overlay',
    
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ),
    plot_bgcolor='white',
    showlegend = False,
    hovermode  = 'x',
    spikedistance =  -1,
    title_text='Healthcare Spending 2000-2021'
)

fig_health = go.Figure(data=data, layout=layout)
trace1 = go.Scatter(x=smoker_data['date'], 
                         y=smoker_data[' Smoking Rate (Ages 15+)'],
                         mode='lines+markers',
                         hovertemplate='<br>%{y}<extra></extra>',
                         line=dict(
                            width=2,
                            color='rgb(101, 145, 212)'
                         ),)

trace2 = go.Bar(x=smoker_data['date'], 
                         y=smoker_data[' Annual Change'],
                         hovertemplate='<br>%{y}<extra></extra>',
                         xaxis="x2", yaxis="y2",
            
                         marker_color='indianred')

data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        gridcolor='rgb(150, 150, 150)',
        showgrid=True,
        gridwidth=0.5,
        fixedrange=True,
        zeroline=False,
        showticklabels=False,
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis=dict(
        domain=[0.4, 1],
        gridcolor='rgb(150, 150, 150)',
        fixedrange=True,
        showgrid=True,
        gridwidth=0.5,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title_text="Per 100K Population"
    ),
    
    xaxis2=dict(      
        anchor="y2",
        fixedrange=True,
        showticklabels=True,
        zeroline=False,
        ticks='outside',
        tickangle=360,
        nticks=12,
        tickwidth=1,
        tickfont=dict(
            family='Arial',
            size=13,
            color='rgb(82, 82, 82)',
        ),
        showspikes = True,
        spikemode  = 'across',
        spikesnap = 'data',
        showline=True,
        spikedash = 'solid',
        spikethickness=2,
    ),
    
    yaxis2=dict(
        domain=[0, 0.3],
        fixedrange=True,
        zeroline=False,
        showline=False,
        showticklabels=True,
        tickfont=dict(
            family='Arial',
            size=11,
            color='rgb(82, 82, 82)',
        ),
        title="Annual % Change",
    ),    
    
    barmode='overlay',
    
    hoverlabel=dict(
        bgcolor="white",
        font_size=14,
        font_family="Arial"
    ),
    plot_bgcolor='white',
    showlegend = False,
    hovermode  = 'x',
    spikedistance =  -1,
    title_text='Smoking Rate 2007-2021'
)

fig_smoker = go.Figure(data=data, layout=layout)


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = "Ukraine Development Indicators"


app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H2(
                    children="Ukraine", className="header-title"
                ),
            ],
            className="container header",
        ),

        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div([
                            dbc.Row([
                                html.Div(
                                    children=[
                                        html.H4(
                                            children="World View", className=""
                                        ),
                                    ],
                                    className="container mt-5",
                                ),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'gdp',
                                        figure = fig_gdp,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",
                                ),

                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'pop',
                                        figure = fig_pop,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",   
                                ),

                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'school',
                                        figure = fig_school,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",  
                                ),                                
                            ]),

                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'co',
                                        figure = fig_co,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",  
                                ),

                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'poverty',
                                        figure = fig_poverty,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",  
                                ), 

                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'life',
                                        figure = fig_life,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",  
                                ), 
                            ]),

                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'gni',
                                        figure = fig_gni,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4", 
                                ),

                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'capacity',
                                        figure = fig_capacity,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col-sm-4 mt-4",  
                                ), 
                            ]),                                                         
                        ]),
                    ],
                    className='container'
                ),

                html.Div(
                    children=[
                        html.Div([
                            dbc.Row([
                                html.Div(
                                    children=[
                                        html.H4(
                                            children="Climate", className=""
                                        ),
                                    ],
                                    className="container mt-5",
                                ),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'climate',
                                        figure = fig_climate,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col mt-3",
                                ),                                
                            ]),


                                                        
                        ]),
                    ],
                    className='container'
                ),
            
                html.Div(
                    children=[
                        html.Div([
                            dbc.Row([
                                html.Div(
                                    children=[
                                        html.H4(
                                            children="Crime Rate & Statistics", className=""
                                        ),
                                    ],
                                    className="container mt-5",
                                ),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'crime',
                                        figure = fig_crime,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col mt-3",
                                ),                                
                            ]),


                                                        
                        ]),
                    ],
                    className='container'
                ),

                html.Div(
                    children=[
                        html.Div([
                            dbc.Row([
                                html.Div(
                                    children=[
                                        html.H4(
                                            children="Health", className=""
                                        ),
                                    ],
                                    className="container mt-5",
                                ),
                            ]),
                            dbc.Row([
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'health',
                                        figure = fig_health,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col mt-3",
                                ),
                                dbc.Col(html.Div([
                                    dcc.Graph(
                                        id = 'smoker',
                                        figure = fig_smoker,
                                        config={"displayModeBar": False}
                                    ),
                                    ]), className="col mt-3 mb-5",
                                ),                                 
                            ]),                                           
                        ]),
                    ],
                    className='container'
                ),                              
            ],
            className='wrapper',
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)