import ast
from _ast import AST, ClassDef, AsyncFunctionDef, FunctionDef, expr
from typing import Any, List

from src.generator.model.response import Response
from src.generator.model.workflow import Workflow
from src.generator.processor.base_processor import BaseProcessor


class DocWorkflowSequenceProcessor(BaseProcessor):
    def build(self, response: Response, node: ClassDef | AsyncFunctionDef | FunctionDef, decorator: expr, path: str) -> None:
        sequence_list: List[str] = [arg.id for arg in decorator.args] if decorator.args else []

        response.workflows[node.name] = Workflow(
            data=sequence_list,
            docstring=ast.get_docstring(node),
            path=path
        )
