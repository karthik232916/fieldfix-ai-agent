from app.agent_service import AgentService
from app.ai_service import AIService
from app.models import Issue
from app.ai_client import create_ai_client

class IssueService:
    
    def __init__(self):
        self.ai_service = AIService()
        self.agent_service = AgentService()

    def is_available(self):
        try:
            create_ai_client()
            return True
        except Exception:
            return False

    def diagnose_with_ai(self, issue: Issue):
        return self.ai_service.diagnose(issue)

    def diagnose(self, description: str):
        description = description.lower()

        if "not turning on" in description or "power" in description:
            return "Check the device power connection and battery."

        if "scanner" in description:
            return "Check the scanner connection and restart the device."

        return "The issue requires further investigation."

    def process_issue(self, issue: Issue):
        try:
            agent_result = self.agent_service.investigate(issue)

            if agent_result["action"] == "request_more_information":
                diagnosis = (
                    "I could not find relevant troubleshooting information "
                    "in the FieldFix knowledge base for this issue."
                )
            else:
                diagnosis = agent_result.get("diagnosis")
        except Exception:
            diagnosis = self.diagnose(issue.description)

        return {
            "status": "analyzed",
            "agent_action": agent_result["action"],
            "next_action": agent_result.get("next_action"),
            "device_status": agent_result.get("device_status"),
            "diagnosis": diagnosis,
            "description": issue.description,
            "device": issue.device,
            "severity": issue.severity,
        }