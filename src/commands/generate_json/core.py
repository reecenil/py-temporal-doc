import os

from src.commands.command import Command


class GenerateJSON(Command):
    # def __init__(self):
    #     pass

    """
    Class for generating diagram
    """

    def __read_file(self, file_path: str):
        if not file_path.lower().endswith(".py"):
            print(f"{file_path} is not a python file. Skipping...")
            return

        with open(file_path) as file:
            try:
                df = file.read()
                # TODO: Parse here
                # self.__parser.create_ast_mapping(df, file_path)
            except Exception:
                print(f"Unable to parse: {file_path}. Skipping...")

    def __read_directory(self, path: str):
        for subdir, dirs, files in os.walk(path):
            for file in files:
                self.__read_file(subdir + "/" + file)

    def execute(self, **kwargs) -> None:
        """
        Execute generate diagram entry point

        Args:
            **kwargs: arguments from CLI

        Returns:
            None
        """

        if "path" in kwargs:
            path: str = kwargs["path"]

            if os.path.isdir(path):
                self.__read_directory(path)
            elif os.path.isfile(path):
                self.__read_file(path)

            # Creates relationship ties for all saved nodes
            # self.__parser.build_tree()

        print("Generate JSON done")
