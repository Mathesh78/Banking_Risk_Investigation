SELECT
    review_id,
    transaction_id,
    risk_level,
    ai_decision,
    ai_confidence,
    reasons,
    review_status,
    created_at
FROM investigation_reviews
WHERE review_status = 'WAITING_FOR_HUMAN'
ORDER BY created_at ASC;