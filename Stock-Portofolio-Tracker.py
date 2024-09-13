# import yfinance as yf
# import pandas as pd

# class StockPortfolio:
#     def __init__(self):
#         self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Price', 'Value'])

#     def add_stock(self, ticker, shares):
#         stock = yf.Ticker(ticker)
#         current_price = stock.history(period='1d')['Close'][0]
#         value = shares * current_price
#         self.portfolio = self.portfolio.append({
#             'Ticker': ticker,
#             'Shares': shares,
#             'Price': current_price,
#             'Value': value
#         }, ignore_index=True)
#         print(f"Added {shares} shares of {ticker} at ${current_price:.2f} per share.")

#     def remove_stock(self, ticker):
#         self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
#         print(f"Removed {ticker} from your portfolio.")

#     def update_portfolio(self):
#         for i in range(len(self.portfolio)):
#             ticker = self.portfolio.loc[i, 'Ticker']
#             shares = self.portfolio.loc[i, 'Shares']
#             stock = yf.Ticker(ticker)
#             current_price = stock.history(period='1d')['Close'][0]
#             value = shares * current_price
#             self.portfolio.at[i, 'Price'] = current_price
#             self.portfolio.at[i, 'Value'] = value

#     def view_portfolio(self):
#         self.update_portfolio()
#         print(self.portfolio)

# # Example Usage:
# portfolio = StockPortfolio()
# portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
# portfolio.add_stock('GOOGL', 5)  # Add 5 shares of Google
# portfolio.view_portfolio()        # View current portfolio
# portfolio.remove_stock('AAPL')    # Remove Apple stock from portfolio
# portfolio.view_portfolio()        # View updated portfolio







import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = pd.DataFrame(columns=['Ticker', 'Shares', 'Price', 'Value'])

    def add_stock(self, ticker, shares):
        stock = yf.Ticker(ticker)
        try:
            current_price = stock.history(period='1d')['Close'][0]
        except (IndexError, KeyError):
            print(f"Error retrieving price for {ticker}.")
            return

        value = shares * current_price
        new_row = pd.DataFrame({
            'Ticker': [ticker],
            'Shares': [shares],
            'Price': [current_price],
            'Value': [value]
        })

        self.portfolio = pd.concat([self.portfolio, new_row], ignore_index=True)
        print(f"Added {shares} shares of {ticker} at ${current_price:.2f} per share.")

    def remove_stock(self, ticker):
        self.portfolio = self.portfolio[self.portfolio['Ticker'] != ticker]
        print(f"Removed {ticker} from your portfolio.")

    def update_portfolio(self):
        for i in range(len(self.portfolio)):
            ticker = self.portfolio.loc[i, 'Ticker']
            shares = self.portfolio.loc[i, 'Shares']
            stock = yf.Ticker(ticker)
            try:
                current_price = stock.history(period='1d')['Close'][0]
            except (IndexError, KeyError):
                print(f"Error retrieving price for {ticker}.")
                continue

            value = shares * current_price
            self.portfolio.at[i, 'Price'] = current_price
            self.portfolio.at[i, 'Value'] = value

    def view_portfolio(self):
        self.update_portfolio()
        print(self.portfolio)

# Example Usage:
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
portfolio.add_stock('GOOGL', 5)  # Add 5 shares of Google
portfolio.view_portfolio()       # View current portfolio
portfolio.remove_stock('AAPL')   # Remove Apple stock from portfolio
portfolio.view_portfolio()       # View updated portfolio
