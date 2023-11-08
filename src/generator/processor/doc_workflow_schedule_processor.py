from _ast import AST, ClassDef, AsyncFunctionDef, FunctionDef, expr
from typing import Any

from src.generator.model.response import Response
from src.generator.processor.base_processor import BaseProcessor


class DocWorkflowScheduleProcessor(BaseProcessor):
    def build(self, response: Response, node: ClassDef | AsyncFunctionDef | FunctionDef, decorator: expr, path: str) -> None:
        pass