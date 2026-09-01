INSERT INTO investigation_reviews
(
    transaction_id,
    risk_level,
    ai_decision,
    ai_confidence,
    reasons,
    review_status
)
VALUES
(
    %s,
    %s,
    %s,
    %s,
    %s,
    'WAITING_FOR_HUMAN'
);