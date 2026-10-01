from pathlib import Path


class KnowledgeService:

    def __init__(self):
        self.knowledge_dir = Path(__file__).parent.parent / "knowledge"

    def search(self, query: str):
        results = []

        query_words = set(query.lower().split())

        stop_words = {"is", "the", "a", "an", "to", "of", "and", "on", "in"}

        query_words = query_words - stop_words

        for file_path in self.knowledge_dir.glob("*.txt"):
            content = file_path.read_text()
            content_lower = content.lower()

            matched_words = [
                word for word in query_words
                if word in content_lower
            ]

            if matched_words:
                results.append({
                    "source": file_path.name,
                    "content": content,
                    "matched_words": matched_words,
                })

        return results

def search_knowledge_base(query: str):
    service = KnowledgeService()
    results = service.search(query)

    return [
        {
            "source": item["source"],
            "content": item["content"],
        }
        for item in results
    ]