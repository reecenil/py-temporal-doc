from typing import List, Optional

from pydantic import BaseModel


class WorkflowCaller(BaseModel):
    workflows: List[str]
    docstring: Optional[str]
    path: str
