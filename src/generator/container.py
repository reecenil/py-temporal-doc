from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory, Singleton

from src.reader.model.ast_map import AstMap
from src.reader.model.node_map import NodeMap
from src.reader.temporal.ast_mapper import AstMapper
from src.reader.temporal.node_builder import NodeBuilder
from src.reader.temporal.parser import TemporalParser


class Container(DeclarativeContainer):
    ast_map = Singleton(AstMap)
    ast_mapper = Singleton(AstMapper, ast_map=ast_map)

    node_map = Singleton(NodeMap)
    node_builder = Singleton(NodeBuilder, node_map=node_map)

    temporal_parser = Factory(
        TemporalParser, ast_mapper=ast_mapper, node_builder=node_builder
    )
