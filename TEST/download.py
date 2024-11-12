import yfinance as yf
import sqlite3
import pandas as pd

# 設定下載的股票代號與日期範圍
symbol = '2330.TW'
start = '2020-01-01'
end = '2024-11-05'

# 下載資料
data = yf.download(symbol, start=start, end=end)

conn = sqlite3.connect('stock_data.db')
cursor = conn.cursor()

# 檢查資料表是否已經存在日期資料
for index, row in data.iterrows():
    date_str = index.strftime('%Y-%m-%d')
    
    # 檢查該日期是否已存在於資料庫中
    cursor.execute("SELECT 1 FROM NewTable WHERE Date = ? AND Tickers = ?", (date_str, symbol))
    result = cursor.fetchone()
    
    if result is None:  # 如果該日期不存在，則插入資料
        open_price = row['Open'] if pd.notnull(row['Open']) else None
        high = row['High'] if pd.notnull(row['High']) else None
        low = row['Low'] if pd.notnull(row['Low']) else None
        adj_close = row['Adj Close'] if pd.notnull(row['Adj Close']) else None
        volume = row['Volume'] if pd.notnull(row['Volume']) else None
        close = row['Close'] if pd.notnull(row['Close']) else None

        # 插入資料
        insertSQL = """
            INSERT INTO NewTable (Date, "Open", High, Low, "Adj Close", Volume, "Close", Tickers)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insertSQL, (date_str, open_price, high, low, adj_close, volume, close, symbol))

# 提交更改並關閉連接
conn.commit()
cursor.close()
conn.close()
