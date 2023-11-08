import ast
from _ast import AST, ClassDef, AsyncFunctionDef, FunctionDef, expr
from typing import Any

from src.generator.model.response import Response
from src.generator.model.temporal_activity import TemporalActivity
from src.generator.processor.base_processor import BaseProcessor


class TemporalActivityProcessor(BaseProcessor):
    def build(self, response: Response, node: ClassDef | AsyncFunctionDef | FunctionDef, decorator: expr, path: str) -> None:
        response.activities[node.name] = TemporalActivity(
            docstring=ast.get_docstring(node),
            path=path
        )
    