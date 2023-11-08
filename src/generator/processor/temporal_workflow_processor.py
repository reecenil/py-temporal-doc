import ast
from _ast import AST, ClassDef, AsyncFunctionDef, FunctionDef, expr
from typing import Any

from src.generator.model.response import Response
from src.generator.model.workflow import Workflow
from src.generator.processor.base_processor import BaseProcessor


class TemporalWorkflowProcessor(BaseProcessor):
    def build(self, response: Response, node: ClassDef | AsyncFunctionDef | FunctionDef, decorator: expr, path: str) -> None:
        # If workflow is already registered via doc_workflow_name, do not replace
        if node.name not in response.workflows:
            response.workflows[node.name] = Workflow(
                sequence=[],
                docstring=ast.get_docstring(node),
                path=path
            )
