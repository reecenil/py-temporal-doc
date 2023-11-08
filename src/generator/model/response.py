from typing import Optional, Dict

from pydantic import BaseModel

from src.generator.model.temporal_activity import TemporalActivity
from src.generator.model.workflow import Workflow
from src.generator.model.workflow_caller import WorkflowCaller


class Response(BaseModel):
    callers: Dict[str, WorkflowCaller] = {}
    workflows: Dict[str, Workflow] = {}
    activities: Dict[str, TemporalActivity] = {}
