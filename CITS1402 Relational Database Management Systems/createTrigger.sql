CREATE TRIGGER updateRentalCost AFTER UPDATE
ON rentalContract
FOR EACH ROW
WHEN NEW.dateBack IS NOT NULL AND OLD.dateBack IS NULL
BEGIN
    UPDATE rentalContract
    SET rentalCost = ROUND(
        (SELECT baseCost + (dailyCost * (julianday(NEW.dateBack) - julianday(NEW.dateOut) + 1))
        FROM PhoneModel
        JOIN PHONE USING (modelNumber, modelName)
        WHERE Phone.IMEI = NEW.IMEI)
    , 2)
    WHERE customerId = NEW.customerId AND IMEI = NEW.IMEI AND dateOut = NEW.dateOut;
END;