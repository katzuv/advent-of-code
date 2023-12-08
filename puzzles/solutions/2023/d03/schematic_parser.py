class SchematicParser:
    """Class that parsers the engine schematic."""

    def __init__(self, engine_schematic: str):
        self._schematic = engine_schematic.splitlines()
        self._schematic_length = len(self._schematic)
        self._schematic_width = len(self._schematic[0])

        self._numbers = []
