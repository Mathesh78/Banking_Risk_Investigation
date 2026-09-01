-- USE banking_db;

-- INSERT INTO customers
-- (customer_id, name, country, risk_level, account_status)
-- VALUES
-- ('C1001', 'Arun Kumar', 'India', 'LOW', 'ACTIVE'),
-- ('C1002', 'Rahul Sharma', 'India', 'MEDIUM', 'ACTIVE'),
-- ('C1003', 'John Smith', 'USA', 'HIGH', 'ACTIVE');

SELECT
    customer_id,
    name,
    country,
    risk_level,
    account_status
FROM customers
WHERE customer_id = %s;