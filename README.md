# Event Marketing Analysis – Carnaval de Québec Case Study

## Overview
This project analyzes the marketing performance of a cultural event inspired by the Carnaval de Québec.

The objective is to identify which marketing channels, content types, and audience segments generate the highest impact on traffic, conversions, and revenue.

## Business Objective
Optimize marketing investment decisions by answering:

- Which channels generate the most revenue?
- Which content types drive the highest engagement and conversion?
- Which channels are the most cost-efficient?
- Where should budget be increased or reduced?

## Dataset
This project uses a synthetic dataset inspired by real-world marketing campaigns.

It includes:
- Paid media (Google Ads, Meta Ads)
- Organic traffic
- Email campaigns
- Device and regional segmentation

## Key Metrics
- CTR (Click-through rate)
- Conversion rate
- Cost per conversion
- Revenue
- ROAS (Return on ad spend)

## Tools Used
- Python (Pandas)
- SQL
- Excel
- GitHub

## Dashboard

This dashboard provides a clear overview of marketing performance across channels, devices, and content types.

It is designed to support data-driven decision-making by identifying where to invest, what to optimize, and how to improve overall campaign performance.

### Key Metrics
- Revenue
- Ad Spend
- ROAS
- CTR
- Conversion Rate
- Cost per Conversion

### Dashboard Insights
- Google Ads is the most profitable channel, generating the highest revenue and ROAS
- Email campaigns show the highest conversion rate, especially during high-intent periods
- Mobile drives the majority of traffic but underperforms in conversion compared to desktop
- Video content delivers the highest engagement and CTR, outperforming static formats

### Business Impact
- Reallocating budget toward Google Ads could significantly increase overall revenue
- Improving mobile conversion rate represents a major opportunity for growth
- Reducing spend on low-performing channels and formats can improve marketing efficiency
- Prioritizing high-performing content types can increase engagement and conversions

### Filters Available
- Channel
- Device
- Region

### Preview

![Marketing Dashboard](dashboard.png)

## Key Insights
- Google Ads generates the highest revenue contribution and strong conversion performance
- Meta Ads delivers high reach but lower conversion efficiency compared to other channels
- Email campaigns show the highest conversion rate during high-intent periods
- Mobile traffic dominates volume but significantly underperforms in conversion compared to desktop

## Sample Results

Based on the dataset:

- Total revenue generated: $5,800
- Total ad spend: $1,350
- ROAS: 4.2x

### Channel Performance Highlights
- Google Ads is the primary revenue driver and most scalable channel
- Email campaigns have the highest conversion efficiency
- Organic Social generates traffic but contributes minimally to revenue

### Content Performance Highlights
- Video content drives the highest engagement and CTR
- Carousel content performs moderately across metrics
- Static images consistently underperform in conversion

## Recommendations
- Reallocate approximately +25% of budget toward Google Ads to maximize revenue growth potential
- Improve mobile user experience to increase conversion rate and capture lost revenue
- Reduce investment in low-performing channels and content formats (Organic Social, static creatives)
- Prioritize campaigns during high-intent periods to increase overall efficiency and ROAS

## Project Structure
- `event_data.csv` → dataset
- `generate_dataset.py` → data generation
- `analysis.py` → data analysis
- `analysis.sql` → SQL queries

## How to Run

This project can be explored directly using the provided dataset and analysis files.

- `event_data.csv` contains the dataset
- `analysis.py` includes analysis logic and KPI calculations
- `analysis.sql` contains example queries for data extraction and aggregation

## Context

This project is inspired by real-world experience in event marketing and digital campaign management, including large-scale cultural events.

The analysis focuses on practical decision-making: where to invest, what to optimize, and how to improve marketing performance using data, with a clear focus on business impact and profitability.
