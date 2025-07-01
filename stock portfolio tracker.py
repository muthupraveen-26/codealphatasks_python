
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 135, "AMZN": 120}
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Stock not found!")

total = 0
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print(f"\nTotal investment: ${total}")
