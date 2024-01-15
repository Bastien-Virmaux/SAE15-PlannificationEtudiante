import pandas as pd
import numpy as np

dates = ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"]
sales = [200, 300, 400, 200, 300, 300]
prices = [3, 1, 2, 4, 3, 2]

df = pd.DataFrame({"Date": dates, "Sales": sales, "Price": prices})

filtered_df = df.query("Sales == 300")
print(filtered_df)
