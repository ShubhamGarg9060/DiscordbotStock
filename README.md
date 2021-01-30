# DiscordbotStock

Discord Bot for Stocks is a bot for the Discord platform that provides us information about stocks of various companies in the form of messages in selected discord channels and direct messages. The stock market is a volatile one and one needs to stay updated about the stock rates to step up one’s trading capabilities.


Our bot will support the following functionalities:

  updates of stock information everytime user queries.

  Query commands for information such as:
  
    Stock details of company X for last 6 months,

    Details of multiple companies plotted on the same graph for easy comparison,

    Stock history of multiple companies and more.


Project Stages
The project consists of the following stages:

Fetch the respective CSV files containing the required stock details of a company.

Sort out the required data and plot it using plot.ly. This will provide us with proper visualization of the data. For example:

Set up a Discord bot on your server and add the necessary code for configuring regular updates in specific channels.

Add various commands to your bot, which will enable the users to get trade data, based on specific queries.


Pre-requisite skills
Python
Post Project Skills
Pandas
Plot.ly

Prototyping the Discord stock bot
Import the yfinance module in a Python script and download a CSV file containing stock details of your preferred company. The stock details should be for a period of one day with intervals of 1 minute.

Plot the closing price against the Datetime using Plot.ly and export the plotting as a PNG file.

Create a Discord bot for your server by going to Discord’s developer portal. Enable the bot in your server(Create a server if you don’t have one).

Write a sample Python script for the bot. The script needs to access the bot using it’s token and send the earlier generated image to a specific channel in your server.

Set up EOD stock updates in the form of text
The first thing that our bot needs is a way to give us daily conclusive updates of the stock information of a company. To achieve this, we need to set up a mechanism which provides daily End-Of-Day stock updates, w.r.t. a company’s trading data, in the form of text messages.


Fetch the CSV file containing the stock details of a company for a particular date using the yfinance module. (Set the period to 1d and withdraw the interval parameter)

Render out the required data to send it as a message to a dedicated channel in your Discord server.

Set up the configuration for the bot to provide this update daily End-Of-Day.

Provide hourly updates of a company’s trading status


Now that we have basic EOD updates in place, we should make the bot more useful. That can be done by configuring useful hourly updates about stocks. we’ll configur updates of the trading information of a company in the form of a plotted chart.

Come up with a script which does the following on intervals of every hour:

Fetching stock data of a company in CSV forma. [Set the period to 1d and interval to 1m.]

Filter out the data for last hour.

Plot the closing price against the Datetime using Plot.ly using the filtered data and export the chart as a PNG file.

Set up daily trade updates

We already have daily EOD updates, in the form of text, in place. But we need some human understandable details of the stock with respect to the changes that occur on the current day. To achieve this, set up a script that fetches the trade information of a company such as details of stock parameters for the day and sends an update in a Discord channel, in the form of a plotted chart.

Fetch stock data of a company in CSV format(as depicted in earlier milestones). [Set the period to 1d and interval to 1m.]

Plot the following two charts:

Closing price against Datetime.

All the parameters(except Volume) against Datetime.

Send the charts as an update in a Discord channel two times a day.

Retrieve historical stock data

It is always a good practice to look up a company's history in the stock market before making any investment. We’ll be able to add a feature to your bot which will help with the same. You should be able to configure your bot, such that it is able to provide the history of a company’s stock information

Figure out how to obtain the CSV file which contains all the stock information available on a company.

Plot the Closing Price against the Date using Plot.ly and export the chart as a PNG file.

Configure your bot with a command which fetches the aforementioned plotted chart by taking the company code as input.

Send the file to a dedicated channel in your Discord server.
