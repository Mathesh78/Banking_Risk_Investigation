UPDATE investigation_reviews
SET
    human_decision = %s,
    human_comments = %s,
    review_status = 'COMPLETED',
    reviewed_at = CURRENT_TIMESTAMP
WHERE review_id = %s
AND review_status = 'WAITING_FOR_HUMAN';