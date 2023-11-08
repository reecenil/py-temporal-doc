from typing import List, Optional

from pydantic import BaseModel

class Workflow(BaseModel):
    sequence: List[str]
    docstring: Optional[str]
    path: str
