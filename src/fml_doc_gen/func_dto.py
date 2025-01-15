from typing import List, Optional, Tuple

class FunctionDTO:
    def __init__(self, name: str, output: Optional[str] = None, inputs: Optional[List[Tuple[str, str]]] = []):
        self.name = name
        self.output_type = output
        self.inputs = [(name, input_type) for (name, input_type) in inputs]
