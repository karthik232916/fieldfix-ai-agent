from fastapi import FastAPI
from pydantic import BaseModel
from app.issue_service import Issue, IssueService

app = FastAPI(
    title="FieldFix AI API",
    version="1.0.0",
)

issue_service = IssueService()

class IssueResponse(BaseModel):
    id: int
    status: str
    message: str
    description: str
    device: str
    severity: str
    agent_action: str
    next_action: str | None = None
    device_status: dict | None = None

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "FieldFix AI API",
        "diagnosis_service": issue_service.is_available(),
    }


@app.post("/issues", response_model=IssueResponse)
async def create_issue(issue: Issue):
    result = issue_service.process_issue(issue)

    return {
        "id": 1,
        "status": result["status"],
        "message": result["diagnosis"],
        "description": result["description"],
        "device": result["device"],
        "severity": result["severity"],
        "agent_action": result["agent_action"],
        "next_action": result["next_action"],
        "device_status": result["device_status"],
    }