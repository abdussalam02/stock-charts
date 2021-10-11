import plotly.graph_objects as go
import pandas as pd
import black
from datetime import datetime 

a = input("Enter the name of the company: ")
df = pd.read_csv(a + '.ns.csv')

fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                                high = df['High'],
                                low = df['Low'],
                                open = df['Open'],
                                close = df['Close'])])

fig.show()
