from dependency_injector.containers import (DeclarativeContainer,
                                            WiringConfiguration)
from dependency_injector.providers import Factory

from src.commands.generate_json.core import GenerateJSON
from src.generator import container as GeneratorContainer

generator_container = GeneratorContainer.Container()


class Container(DeclarativeContainer):
    # Wiring target list
    wiring_config = WiringConfiguration(modules=[".command_list"])

    generate_json = Factory(GenerateJSON, parser=generator_container.parser)

