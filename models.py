from typing import List
from pydantic import BaseModel

class Component(BaseModel):
    name: str
    type: str  # e.g., "frontend", "backend", "microservice"
    description: str
    inputs: List[str]
    outputs: List[str]
    libraries: List[str]
    additional_info: str

class ArchitectureSpec(BaseModel):
    project_name: str
    overview: str
    components: List[Component]
    communication_patterns: List[str]
    deployment_considerations: List[str] 