import pandas as pd

tables = pd.read_html("https://en.wikipedia.org/wiki/Google", header=0, parse_dates=["Revenue"])

print(tables.to_json(orient="records", date_format="iso"))
