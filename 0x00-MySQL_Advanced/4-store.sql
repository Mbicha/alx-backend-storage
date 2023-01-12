-- Trigger that decreases quantity after 
-- adding new order

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number
WHERE NEW.item_name = name;
