from pydantic import BaseModel


class Issue(BaseModel):
    description: str
    device: str
    severity: str