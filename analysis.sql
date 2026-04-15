SELECT
    channel,
    SUM(revenue) AS total_revenue,
    SUM(ad_spend) AS total_spend,
    SUM(conversions) AS total_conversions,
    SUM(ad_spend) / SUM(conversions) AS cost_per_conversion
FROM event_data
GROUP BY channel
ORDER BY total_revenue DESC;

SELECT
    content_type,
    AVG(ctr) AS avg_ctr,
    AVG(conversion_rate) AS avg_conversion_rate
FROM event_data
GROUP BY content_type
ORDER BY avg_ctr DESC;
