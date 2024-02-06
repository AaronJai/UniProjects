CREATE VIEW CustomerSummary AS

-- Part 1: Rentals with valid IMEI
SELECT 
    r.customerId,
    pm.modelName,
    SUM(julianday(r.dateBack) - julianday(r.dateOut) + 1) AS daysRented,
    CASE 
        WHEN strftime('%m', r.dateBack) BETWEEN '01' AND '06' THEN  -- Check if month between January and June
            CAST(strftime('%Y', r.dateBack) - 1 AS TEXT) || '/' || strftime('%Y', r.dateBack)   -- Then gets previous year, adds '/' and current year
        ELSE 
            strftime('%Y', r.dateBack) || '/' || CAST(strftime('%Y', r.dateBack) + 1 AS TEXT)   -- Else gets current year, adds '/' and next year
    END AS taxYear, -- CAST used to ensure function returns correct TEXT datatype
    SUM(r.rentalCost) AS rentalCost
FROM rentalContract r
JOIN Phone p USING (IMEI)
JOIN PhoneModel pm USING (modelNumber, modelName)
WHERE r.dateBack IS NOT NULL
GROUP BY r.customerId, pm.modelName, taxYear

UNION ALL

-- Part 2: Rentals with NULL IMEI
SELECT 
    r.customerId,
    NULL AS modelName,
    SUM(julianday(r.dateBack) - julianday(r.dateOut) + 1) AS daysRented,
    CASE    -- Case same as above
        WHEN strftime('%m', r.dateBack) BETWEEN '01' AND '06' THEN 
            CAST(strftime('%Y', r.dateBack) - 1 AS TEXT) || '/' || strftime('%Y', r.dateBack)
        ELSE 
            strftime('%Y', r.dateBack) || '/' || CAST(strftime('%Y', r.dateBack) + 1 AS TEXT)
    END AS taxYear,
    SUM(r.rentalCost) AS rentalCost
FROM rentalContract r
WHERE r.IMEI IS NULL AND r.dateBack IS NOT NULL
GROUP BY r.customerId, taxYear;