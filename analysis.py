import pandas as pd

# Load data
df = pd.read_csv("event_data.csv")

# Basic metrics
df["ctr"] = df["clicks"] / df["impressions"]
df["conversion_rate"] = df["conversions"] / df["clicks"]
df["roas"] = df["revenue"] / df["ad_spend"]

# Channel performance
channel_perf = df.groupby("channel").agg({
    "revenue": "sum",
    "ad_spend": "sum",
    "conversions": "sum"
}).sort_values(by="revenue", ascending=False)

# Content performance
content_perf = df.groupby("content_type").agg({
    "clicks": "sum",
    "conversions": "sum"
}).sort_values(by="conversions", ascending=False)

print("\n=== CHANNEL PERFORMANCE ===")
print(channel_perf)

print("\n=== CONTENT PERFORMANCE ===")
print(content_perf)
