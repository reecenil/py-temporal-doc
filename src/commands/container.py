from dependency_injector.containers import (DeclarativeContainer,
                                            WiringConfiguration)
from dependency_injector.providers import Factory

from src.commands.generate_json.core import GenerateJSON

# from src.reader import container as ReaderContainer
#
#
# reader_container = ReaderContainer.Container()


class Container(DeclarativeContainer):
    # Wiring target list
    wiring_config = WiringConfiguration(modules=[".command_list"])

    # TODO: Inject here
    # generate_json = Factory(GenerateJSON, parser=reader_container.temporal_parser)

    generate_json = Factory(GenerateJSON)
