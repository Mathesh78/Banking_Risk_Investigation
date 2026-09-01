CREATE DATABASE IF NOT EXISTS banking_db;

USE banking_db;


-- ==========================================
-- CUSTOMERS
-- ==========================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    risk_level VARCHAR(20),
    account_status VARCHAR(20)
);


-- ==========================================
-- ACCOUNTS
-- ==========================================

CREATE TABLE IF NOT EXISTS accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    balance DECIMAL(15,2) DEFAULT 0.00,
    currency VARCHAR(10),
    status VARCHAR(20),

    CONSTRAINT fk_account_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ==========================================
-- TRANSACTIONS
-- ==========================================

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    account_id VARCHAR(20) NOT NULL,

    amount DECIMAL(15,2) NOT NULL,
    currency VARCHAR(10),

    merchant VARCHAR(100),
    location VARCHAR(100),

    transaction_type VARCHAR(50),
    status VARCHAR(20),

    transaction_time DATETIME,

    CONSTRAINT fk_transaction_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_transaction_account
        FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)
);


-- ==========================================
-- FRAUD ALERTS
-- ==========================================

CREATE TABLE IF NOT EXISTS fraud_alerts (
    alert_id VARCHAR(20) PRIMARY KEY,

    transaction_id VARCHAR(20) NOT NULL,

    risk_score DECIMAL(5,2),
    risk_level VARCHAR(20),

    reason TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_alert_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions(transaction_id)
);


-- ==========================================
-- INVESTIGATIONS
-- ==========================================

CREATE TABLE IF NOT EXISTS investigations (
    investigation_id VARCHAR(20) PRIMARY KEY,

    transaction_id VARCHAR(20) NOT NULL,

    investigation_status VARCHAR(30),

    decision VARCHAR(30),

    investigator_notes TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_investigation_transaction
        FOREIGN KEY (transaction_id)
        REFERENCES transactions(transaction_id)
);