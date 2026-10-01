from app.knowledge_service import KnowledgeService
from app.ai_client import create_ai_client
from app.models import Issue


class AIService:

    def __init__(self):
        self.knowledge_service = KnowledgeService()

    def diagnose(self, issue: Issue):
        client = create_ai_client()

        knowledge = self.knowledge_service.search(issue.description)
        
        if not knowledge:
            return (
                "I could not find relevant troubleshooting information "
                "in the FieldFix knowledge base for this issue."
            )
        
        knowledge_text = "\n\n".join(
            item["content"] for item in knowledge
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are FieldFix AI, a technical support assistant. "
                        "Analyze equipment problems and provide practical troubleshooting advice. "
                        "Use the retrieved knowledge as the primary source for your answer. "
                        "Do not invent device-specific facts that are not supported by the retrieved knowledge. "
                        "Only recommend actions that are supported by the retrieved knowledge. "
                        "If the retrieved knowledge does not support a recommendation, do not include it. "
                        "If the knowledge does not contain enough information, clearly say that more information is needed."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Device: {issue.device}\n"
                        f"Severity: {issue.severity}\n"
                        f"Problem: {issue.description}\n\n"
                        f"Relevant knowledge:\n---\n{knowledge_text}\n---"
                    ),
                },
            ],
        )

        return response.choices[0].message.content