import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2026-01-15", end="2026-02-15")
channels = ["Google Ads", "Meta Ads", "Organic Social", "Email", "Direct"]
content_types = ["Video", "Image", "Carousel", "Story"]
devices = ["Mobile", "Desktop"]
regions = ["Québec", "Montréal", "Autres"]

data = []

for date in dates:
    for channel in channels:
        impressions = np.random.randint(1000, 10000)
        clicks = int(impressions * np.random.uniform(0.02, 0.08))
        conversions = int(clicks * np.random.uniform(0.02, 0.15))
        spend = round(np.random.uniform(50, 500), 2)
        revenue = conversions * np.random.randint(10, 50)

        data.append({
            "date": date,
            "channel": channel,
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "ad_spend": spend,
            "revenue": revenue,
            "content_type": np.random.choice(content_types),
            "device": np.random.choice(devices),
            "region": np.random.choice(regions)
        })

df = pd.DataFrame(data)

df["ctr"] = df["clicks"] / df["impressions"]
df["conversion_rate"] = df["conversions"] / df["clicks"]

df.to_csv("event_data.csv", index=False)

print("Dataset généré.")
