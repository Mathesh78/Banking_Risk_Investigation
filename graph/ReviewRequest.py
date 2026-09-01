from pydantic import BaseModel


class ReviewRequest(BaseModel):

    human_decision: str

    human_comments: str