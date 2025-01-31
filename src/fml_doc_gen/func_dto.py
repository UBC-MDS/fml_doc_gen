from typing import List, Optional, Tuple


class FunctionDTO:
    """
    Data Transfer Object (DTO) for function metadata.

    Attributes:
        name (Optional[str]): The name of the function.
        output_type (Optional[str]): The return type of the function.
        inputs (Optional[List[Tuple[str, str]]]): A list of input parameters as (name, type) tuples.
        src (Optional[str]): The source code or reference associated with the function.
    """

    def __init__(
        self,
        name: Optional[str] = "",
        output: Optional[str] = None,
        inputs: Optional[List[Tuple[str, str]]] = None,
        src: Optional[str] = None,
    ):
        """
        Initializes a FunctionDTO instance.

        Args:
            name (Optional[str]): The name of the function. Defaults to an empty string.
            output (Optional[str]): The return type of the function. Defaults to None.
            inputs (Optional[List[Tuple[str, str]]]): List of input parameters as (name, type) tuples. Defaults to an empty list.
            src (Optional[str]): The source code or reference associated with the function. Defaults to None.
        """
        if inputs is None:
            inputs = []
        
        self.name = name
        self.output_type = output
        self.inputs = [(name, input_type) for (name, input_type) in inputs]
        self.src = src

    def __str__(self) -> str:
        """
        Returns a string representation of the FunctionDTO instance.

        Returns:
            str: A formatted string containing function name, return type, and inputs.
        """
        return (
            f"Function Name: {self.name}\n"
            f"Return Type: {self.output_type}\n"
            f"Input List: {self.inputs}"
        )
