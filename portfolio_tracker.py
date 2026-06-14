import os

# 1. Hardcoded dictionary to define stock prices
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "AMZN": 175.00,
    "MSFT": 420.00,
    "GOOGL": 150.00
}

def track_portfolio():
    user_portfolio = {}
    
    print("--- Welcome to CodeAlpha Stock Portfolio Tracker ---")
    print("Available stocks to track:")
    for ticker, price in STOCK_PRICES.items():
        print(f"  • {ticker}: ${price:.2f}")
    print("-" * 50)

    # 2. User Input Loop
    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper().strip()
        
        if symbol == 'DONE':
            break
            
        if symbol not in STOCK_PRICES:
            print(f"❌ '{symbol}' is not in our system. Please try AAPL, TSLA, AMZN, MSFT, or GOOGL.")
            continue
            
        try:
            quantity = int(input(f"Enter the quantity of shares for {symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be a positive number.")
                continue
        except ValueError:
            print("❌ Invalid input! Please enter a whole number for quantity.")
            continue

        # Add or update quantity in the portfolio
        if symbol in user_portfolio:
            user_portfolio[symbol] += quantity
        else:
            user_portfolio[symbol] = quantity
            
        print(f"✅ Added {quantity} shares of {symbol} to your tracker.")

    # 3. Calculate and Display Results
    if not user_portfolio:
        print("\nYour portfolio is empty. Goodbye!")
        return

    print("\n" + "="*20 + " PORTFOLIO SUMMARY " + "="*20)
    print(f"{'Stock':<10}{'Shares':<10}{'Price/Share':<15}{'Total Value':<15}")
    print("-" * 50)

    total_portfolio_value = 0.0
    file_lines = ["=== CodeAlpha Stock Portfolio Report ===\n\n", 
                  f"{'Stock':<10}{'Shares':<10}{'Price/Share':<15}{'Total Value':<15}\n",
                  "-" * 50 + "\n"]

    for symbol, quantity in user_portfolio.items():
        price = STOCK_PRICES[symbol]
        stock_total = quantity * price
        total_portfolio_value += stock_total
        
        # Display Row
        row_str = f"{symbol:<10}{quantity:<10}${price:<14.2f}${stock_total:<14.2f}"
        print(row_str)
        file_lines.append(row_str + "\n")

    print("-" * 50)
    summary_str = f"Total Portfolio Investment Value: ${total_portfolio_value:.2f}"
    print(summary_str)
    print("=" * 50)
    
    file_lines.append("-" * 50 + "\n")
    file_lines.append(summary_str + "\n")

    # 4. Save results to a .txt file (File Handling)
    filename = "portfolio_report.txt"
    try:
        with open(filename, "w") as file:
            file.writelines(file_lines)
        print(f"\n📁 Report successfully saved to: {os.path.abspath(filename)}")
    except IOError:
        print("\n❌ Error: Could not save the portfolio report file.")

if __name__ == "__main__":
    track_portfolio()