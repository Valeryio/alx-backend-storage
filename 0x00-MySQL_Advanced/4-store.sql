-- The script on the store DB

DELIMITER here //
CREATE TRIGGER decrease_quantity
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
	IF NEW.number > 0 THEN
		UPDATE items
		SET items.quantity = items.quantity - NEW.number;
	END IF;
END; //
DELIMITER
