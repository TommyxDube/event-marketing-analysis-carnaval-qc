import pandas as pd

df = pd.read_csv("event_data.csv")

print("Revenue total:", df["revenue"].sum())
print("Spend total:", df["ad_spend"].sum())

channel = df.groupby("channel").agg({
    "revenue": "sum",
    "ad_spend": "sum",
    "conversions": "sum"
}).reset_index()

channel["cost_per_conversion"] = channel["ad_spend"] / channel["conversions"]

print(channel)

content = df.groupby("content_type").agg({
    "ctr": "mean",
    "conversion_rate": "mean"
}).reset_index()

print(content)
