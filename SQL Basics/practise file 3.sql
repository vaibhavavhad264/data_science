SELECT * FROM financials;

SELECT *, IF(currency = 'USD', revenue * 96, revenue) AS currency_INR FROM financials;

SELECT *, IF(currency = 'USD', revenue * 96, revenue) AS currency_INR 
FROM financials
ORDER BY currency_INR DESC;

SELECT *,
CASE
	WHEN unit = 'Billions' THEN revenue*1000
    WHEN unit = 'Thousands' THEN revenue/1000
    ELSE revenue
END AS revenue_MILLION
FROM financials;



