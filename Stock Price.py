#Prints the current price of a stock per Yahoo Finance. 

#Install the library first by typing pip install yfinance in the terminal

import yfinance as yf

ticker_symbol=input("Type the ticker symbol for the stock: " )

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    current_price = stock.history(period="1d")["Close"].iloc[-1]
    return current_price

price = get_stock_price(ticker_symbol.upper())
print(f"The current price of {ticker_symbol.upper()} is ${price:.2f}")

#price:.2f takes the value to only two decimal places
#.upper() capitalizes the ticker symbol to look all professional and stuff
