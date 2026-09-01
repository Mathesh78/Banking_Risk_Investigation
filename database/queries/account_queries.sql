-- INSERT INTO accounts
-- (account_id, customer_id, balance, currency, status)
-- VALUES
-- ('A1001', 'C1001', 250000.00, 'INR', 'ACTIVE'),
-- ('A1002', 'C1002', 120000.00, 'INR', 'ACTIVE'),
-- ('A1003', 'C1003', 500000.00, 'USD', 'ACTIVE');

SELECT
    account_id,
    customer_id,
    balance,
    currency,
    status
FROM accounts
WHERE account_id = %s;