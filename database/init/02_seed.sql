USE banking_db;

-- 1. Customers
INSERT INTO customers
(
    customer_id,
    name,
    country,
    risk_level,
    account_status
)
VALUES
(
    'C1001',
    'Arun Kumar',
    'India',
    'MEDIUM',
    'ACTIVE'
),
(
    'C1002',
    'Priya Sharma',
    'India',
    'LOW',
    'ACTIVE'
);


-- 2. Accounts
INSERT INTO accounts
(
    account_id,
    customer_id,
    balance,
    currency,
    status
)
VALUES
(
    'A1001',
    'C1001',
    250000.00,
    'INR',
    'ACTIVE'
),
(
    'A1002',
    'C1002',
    150000.00,
    'INR',
    'ACTIVE'
);


-- 3. Transactions
INSERT INTO transactions
(
    transaction_id,
    customer_id,
    account_id,
    amount,
    currency,
    merchant,
    location,
    transaction_type,
    status,
    transaction_time
)
VALUES
(
    'TX1001',
    'C1001',
    'A1001',
    85000.00,
    'INR',
    'ABC Electronics',
    'Dubai',
    'INTERNATIONAL_TRANSFER',
    'PENDING',
    '2026-08-10 10:30:00'
),
(
    'TX1002',
    'C1001',
    'A1001',
    2500.00,
    'INR',
    'Amazon',
    'Chennai',
    'PURCHASE',
    'COMPLETED',
    '2026-08-10 11:00:00'
),
(
    'TX1003',
    'C1002',
    'A1002',
    75000.00,
    'INR',
    'XYZ Services',
    'Mumbai',
    'TRANSFER',
    'PENDING',
    '2026-08-10 12:00:00'
);


-- 4. Fraud alerts
INSERT INTO fraud_alerts
(
    alert_id,
    transaction_id,
    risk_score,
    risk_level,
    reason
)
VALUES
(
    'FA1001',
    'TX1001',
    87.00,
    'HIGH',
    'Large international transaction from an unusual location'
);


-- 5. Investigations
INSERT INTO investigations
(
    investigation_id,
    transaction_id,
    investigation_status,
    decision,
    investigator_notes
)
VALUES
(
    'INV1001',
    'TX1001',
    'IN_PROGRESS',
    'PENDING',
    'Transaction requires fraud and compliance investigation'
);