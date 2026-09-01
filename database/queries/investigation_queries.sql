-- INSERT INTO investigations (
--     investigation_id,
--     transaction_id,
--     investigation_status,
--     decision,
--     investigator_notes
-- )
-- VALUES (
--     'INV1001',
--     'TX1001',
--     'IN_PROGRESS',
--     'PENDING',
--     'Transaction requires fraud and compliance investigation.'
-- );

SELECT
    investigation_id,
    transaction_id,
    investigation_status,
    decision,
    investigator_notes,
    created_at
FROM investigations
WHERE transaction_id = %s;