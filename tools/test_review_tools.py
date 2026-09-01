from tools.review_tools import (
    get_pending_reviews
)


result = get_pending_reviews()

print("\n========== PENDING REVIEWS ==========")

for review in result:
    print(review)