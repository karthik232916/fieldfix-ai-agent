from app.device_service import check_device_status
from app.models import Issue
from app.ai_service import AIService
from app.knowledge_service import search_knowledge_base


class AgentService:
    
    def __init__(self):
        self.ai_service = AIService()

    def investigate(self, issue: Issue):
        knowledge = search_knowledge_base(issue.description)
        device_status = check_device_status(issue.device)

        if knowledge:
            diagnosis = self.ai_service.diagnose(issue)

            if device_status["status"] == "offline":
                next_action = "Check device connectivity before continuing troubleshooting."
            else:
                next_action = "Provide troubleshooting steps to the technician."

            return {
                "action": "diagnose_with_ai",
                "reason": "Relevant troubleshooting knowledge was found.",
                "knowledge": knowledge,
                "device_status": device_status,
                "diagnosis": diagnosis,
                "next_action": next_action,
            }

        return {
            "action": "request_more_information",
            "reason": "No relevant troubleshooting knowledge was found.",
            "knowledge": [],
        }