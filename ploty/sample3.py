import pandas as pd
import numpy as np
import plotly.graph_objects as go

y = [1,0,-1,0,0,1,-1]
fig = go.Figure(data=go.Bar(y=y))
# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()