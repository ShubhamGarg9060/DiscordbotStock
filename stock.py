import pandas as pd
import csv
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
import os

company=input("Company Code: ")
dataa = yf.download(company , period="1d" , interval="1m")
dataa.to_csv("Stock.csv")

#df = pd.read_csv('Stock.csv')
#df.head()
#fig = px.line(df, x = 'Datetime', y = 'Close', title='Tesla Stock Closing Prices against Time')

#cdf['Close'].plot(title="TSLA's stock price")

df = pd.read_csv('Stock.csv')
#ticker = yf.Ticker(company)

#cdf = ticker.history(period="max")
#cdf['Close'].plot(title="Stock price")

#trace = go.Scatter(x = cdf['Datetime'], y = cdf['Close'], name='Stock Prices of all years (in USD)')
trace1 = go.Scatter(x = df['Datetime'], y = df['Open'], name='Opening Prices (in USD)')
trace2 = go.Scatter(x = df['Datetime'], y = df['High'], name='High Prices (in USD)')
trace3 = go.Scatter(x = df['Datetime'], y = df['Low'], name='Low Prices (in USD)')
trace4 = go.Scatter(x = df['Datetime'], y = df['Close'], name='Closing Prices (in USD)')
trace5 = go.Scatter(x = df['Datetime'], y = df['Adj Close'], name='Adjusted Closing Prices (in USD)')
fig2 = go.Figure(data=[trace1, trace2, trace3, trace4,trace5] )
fig = go.Figure(trace4 )
#fig3 = go.Figure(trace )
fig.update_layout(title='Closing Prices against Time',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig2.update_layout(title='Stock Prices against Time',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
#fig3.update_layout(title='Stock Prices of all years against Time',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)

if not os.path.exists("images"):
    os.mkdir("images")
#plotly.io.orca.config.executable = '/content/images'
fig.write_image("images/fig1.png" , engine="kaleido")
fig2.write_image("images/fig2.png" , engine="kaleido")
#fig3.write_image("images/fig3.png" , engine="kaleido")