# importing the libraries
from dash import Dash, dcc, html, dash_table
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# init app
app = Dash(__name__)

# data table
def sample_table():
    return pd.read_csv('./dataset/anime.csv').head(10)


# missing values
def missing_values():
    df = pd.read_csv('./dataset/anime.csv')
    return px.imshow(df.isna(),color_continuous_scale='gray')


# genrealized recommendations
def generalized_recommendations():
    anime_df = pd.read_csv('./dataset/anime.csv')
    anime_df['Weighted Rating'] = (anime_df['rating']*anime_df['members'])
    return anime_df.sort_values(by='Weighted Rating',ascending=False)[['anime_id','name','genre','type','rating']].head(15)

# layout
app.layout = html.Div([
    
    # header
    html.H1("Anime Recommender System",id='title'),

    # 1st Row - dataset sample
    html.Div([
        html.H2("Dataset Sample"),
        dash_table.DataTable(
            id="Data Table",
            columns=[{"name":i, "id":i} for i in sample_table().columns],
            data=sample_table().to_dict('records'),
            style_table={'overflowX': 'auto'}
        ),
    ],className="sample-table"),


    # 2nd row - Missing and Generalized Recommendations
    html.Div([

        # 2nd Row , 1st Column
        html.Div([
            html.H2("Missing Values"),
            dcc.Graph(id='missing_values',figure=missing_values())
        ],className="col1"),

        # 2nd Row , 2nd Column
        html.Div([
            html.H2("Generalized Recommendations"),
            dash_table.DataTable(
                id='generalized',
                columns=[{"name":i, "id":i} for i in generalized_recommendations().columns],
                data=generalized_recommendations().to_dict('records'),
                style_table={'overflowX': 'auto'}
            )
        ],className="col2")
    ],className="row1")



],className='body')

# run server
if __name__ == "__main__":
    app.run_server(debug=True)