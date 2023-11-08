from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton

from src.generator.consts import DecoratorTargets
from src.generator.model.response import Response
from src.generator.parser import Parser
from src.generator.processor.doc_workflow_caller_processor import DocWorkflowCallerProcessor
from src.generator.processor.doc_workflow_schedule_processor import DocWorkflowScheduleProcessor
from src.generator.processor.doc_workflow_sequence_processor import DocWorkflowSequenceProcessor
from src.generator.processor.temporal_activity_processor import TemporalActivityProcessor
from src.generator.processor.temporal_workflow_processor import TemporalWorkflowProcessor


class Container(DeclarativeContainer):
    # Processors
    doc_workflow_caller_processor = Singleton(DocWorkflowCallerProcessor)
    doc_workflow_schedule_processor = Singleton(DocWorkflowScheduleProcessor)
    doc_workflow_sequence_processor = Singleton(DocWorkflowSequenceProcessor)
    temporal_activity_processor = Singleton(TemporalActivityProcessor)
    temporal_workflow_processor = Singleton(TemporalWorkflowProcessor)

    # Response data
    response = Singleton(Response)

    parser = Factory(
        Parser,
        doc_workflow_caller_processor=doc_workflow_caller_processor,
        doc_workflow_schedule_processor=doc_workflow_schedule_processor,
        doc_workflow_sequence_processor=doc_workflow_sequence_processor,
        temporal_activity_processor=temporal_activity_processor,
        temporal_workflow_processor=temporal_workflow_processor,
        response=response,
    )
