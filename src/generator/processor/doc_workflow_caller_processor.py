import ast
from _ast import AST, ClassDef, AsyncFunctionDef, FunctionDef, expr
from typing import List

from src.generator.model.response import Response
from src.generator.model.workflow_caller import WorkflowCaller
from src.generator.processor.base_processor import BaseProcessor


class DocWorkflowCallerProcessor(BaseProcessor):
    def build(self, response: Response, node: ClassDef | AsyncFunctionDef | FunctionDef, decorator: expr, path: str) -> None:
        workflow_list: List[str] = [arg.id for arg in decorator.args] if decorator.args else []

        response.callers[node.name] = WorkflowCaller(
            data=workflow_list,
            docstring=ast.get_docstring(node),
            path=path,
        )
