-- INSERT INTO fraud_alerts
-- (
--     alert_id,
--     transaction_id,
--     risk_score,
--     risk_level,
--     reason
-- )
-- VALUES
-- (
--     'FA1001',
--     'TX1001',
--     87.00,
--     'HIGH',
--     'Unusual location and unusually high transaction amount'
-- ),
-- (
--     'FA1002',
--     'TX1003',
--     65.00,
--     'MEDIUM',
--     'Transaction amount higher than customer normal pattern'
-- );

SELECT
    alert_id,
    transaction_id,
    risk_score,
    risk_level,
    reason
FROM fraud_alerts
WHERE transaction_id = %s;