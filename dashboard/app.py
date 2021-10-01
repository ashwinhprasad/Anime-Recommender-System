# importing the libraries
from dash import Dash, dcc, html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# init app
app = Dash(__name__)

if __name__ == "__main__":
    app.run_server(debug=True)