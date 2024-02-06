CREATE TABLE PhoneModel (
  modelNumber TEXT PRIMARY KEY,
  modelName TEXT,
  storage INTEGER,
  colour TEXT,
  baseCost REAL,
  dailyCost REAL
);

CREATE TABLE Customer (
  customerId INTEGER PRIMARY KEY,
  customerName TEXT,
  customerEmail TEXT
);

CREATE TABLE Phone (
    modelNumber TEXT,
    modelName TEXT,
    IMEI TEXT PRIMARY KEY,
    FOREIGN KEY (modelNumber, modelName) REFERENCES PhoneModel(modelNumber, modelName),
    /* 
    Ensuring the Luhn algorithm's result is a multiple of 10. 
    Note: Some older SQLite versions had issues with direct modulo operations in CHECK constraints.
    */
    CHECK (
        (
            -- Sum of the digits in the odd positions
            CAST(SUBSTR(IMEI, 1, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 3, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 5, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 7, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 9, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 11, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 13, 1) AS INTEGER) + 
            CAST(SUBSTR(IMEI, 15, 1) AS INTEGER) +
            
            -- Double and sum digits for even positions
            -- / 10 gets 'tens' place, % 10 gets 'ones' place. This also works on single digit results.
            (CAST(SUBSTR(IMEI, 2, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 2, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 4, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 4, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 6, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 6, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 8, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 8, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 10, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 10, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 12, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 12, 1) AS INTEGER) * 2 % 10) + 
            (CAST(SUBSTR(IMEI, 14, 1) AS INTEGER) * 2 / 10 + CAST(SUBSTR(IMEI, 14, 1) AS INTEGER) * 2 % 10)
        ) % 10 = 0
    )
);

CREATE TABLE rentalContract (
    customerId INTEGER,
    IMEI  TEXT,
    dateOut TEXT,
    dateBack TEXT,
    rentalCost REAL,
    PRIMARY KEY (IMEI, dateOut),
    FOREIGN KEY (customerId) REFERENCES Customer(customerId),
    FOREIGN KEY (IMEI) REFERENCES Phone(IMEI) ON DELETE SET NULL
);