# Discord Bot for Stocks

[Discord](https://discord.com/) Bot for Stocks is a bot for the Discord platform that provides us information about stocks of various companies in the form of messages in selected discord channels and direct messages. The stock market is a volatile one and one needs to stay updated about the stock rates to step up one’s trading capabilities.

Our bot will support the following functionalities:

   1.Updates of stock information everytime user queries.

   2.Query commands for information such as:
  
    Stock details of company X for last 6 months,
    Details of multiple companies plotted on the same graph for easy comparison,
    Stock history of multiple companies and more.

## Pre-requisite Skills
[Python](https://www.python.org)

##Post Project Skills
[Pandas](https://pandas.pydata.org/docs/getting_started/overview.html#:~:text=pandas%20is%20a%20Python%20package,world%20data%20analysis%20in%20Python.)
[Plot.ly](https://plotly.com)

## Usage :
```
1.Install Python3
2.Install pip
3.Install all the prerequisites using : pip install -r prerequisites.txt
4.Fetch the respective CSV files containing the required stock details of a company run: stock.py
5.Sort out the required data and plot it using plot.ly.
6.Set up a Discord bot on your server and add the necessary code to configure regular updates in specific channels.
7.Run bot.py:python bot.py [companycode]
8.Add various commands to your bot, which will enable the users to get trade data, based on specific queries.
```

## Prototyping the Discord stock bot
1.Import the `yfinance` module in a Python script and download a `CSV` file containing stock details of your preferred company.

2.Plot the closing price against the Datetime using `Plot.ly` and export the plotting as a `PNG` file.

3.Create a `Discord bot` for your server by going to Discord’s developer portal.

4.Write a sample Python script for the bot. The script needs to access the bot using it’s `token` and send the earlier generated image to a specific channel in your server.

## Set up EOD stock updates in the form of text
The first thing that our bot needs is a way to give us daily conclusive updates of the stock information of a company. To achieve this, we need to set up a mechanism which provides daily End-Of-Day stock updates, w.r.t. a company’s trading data, in the form of text messages.

1.Fetch the `CSV file` containing the stock details of a company for a particular date using the yfinance module.

2.Render out the required data to send it as a message to a dedicated channel in your Discord server.

3.Set up the configuration for the bot to provide this update daily `End-Of-Day`.

4.Provide hourly updates of a company’s trading status


## Retrieve historical stock data

It is always a good practice to look up a company's history in the stock market before making any investment. 

1.Figure out how to obtain the CSV file which contains all the stock information available on a company.

2.Plot the Closing Price against the Date using Plot.ly and export the chart as a PNG file.

3.Configure your bot with a command which fetches the aforementioned plotted chart by taking the company code as input.

4.Send the file to a dedicated channel in your Discord server.

<b>Now Your DiscordServer Start running for Stock Updates! :) </b><br><br>

## References
[A comprehensive guide to downloading stock prices in Python](https://towardsdatascience.com/a-comprehensive-guide-to-downloading-stock-prices-in-python-2cd93ff821d4)<br>
[Scrapping Yahoo Finance at regular intervals](https://stackoverflow.com/questions/61976027/scrapping-yahoo-finance-at-regular-intervals)<br>
[Plot CSV Data | Python0](https://plotly.com/python/plot-data-from-csv/)<br>
[Static Image Export | Python](https://plotly.com/python/static-image-export/)<br>
For curious readers: [Learn how to create beautiful and insightful charts with Python](https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f)<br>
[Discord Developer Portal — Documentation — Intro](https://discord.com/developers/docs/intro)<br>
[How to Make a Discord Bot in Python – Real Python](https://realpython.com/how-to-make-a-discord-bot-python/)<br>
[How to send message to a specific channel in Discord - discordpy](https://discordpy.readthedocs.io/en/latest/faq.html#how-do-i-send-a-message-to-a-specific-channel)<br>
[How to Run or Repeat a Linux Command Every X Seconds Forever](https://www.tecmint.com/run-repeat-linux-command-every-x-seconds/)<br>
[Way to read first few lines for pandas dataframe](https://stackoverflow.com/questions/15008970/way-to-read-first-few-lines-for-pandas-dataframe)<br>
[How to plot multiple lines on the same y-axis using plotly express](https://community.plotly.com/t/how-to-plot-multiple-lines-on-the-same-y-axis-using-plotly-express/29219/8)<br>
