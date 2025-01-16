from func_dto import FunctionDTO

DOCSTRING_TEMPLATE = """
    {function_name}: 
    ### INSERT FUNCTION DEFINITION HERE ###
    {function_parameters}
    {function_output}
      
    Examples:
    --------
    ### INSERT FUNCTION EXAMPLE USAGES HERE ###
"""

DOCSTRING_PARAMETERS_TEMPLATE = """
    Parameters:
    ----------
    {function_params_str}
"""

DOCSTRING_PARAMETER_TEMPLATE = """
    {param_name}: {param_type}
    ### INSERT PARAMETER DEFINITION HERE ###
    
"""

DOCSTRING_OUTPUT_TEMPLATE = """
    Returns:
    -------
    {function_output_type}
        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###
"""

DOCSTRING_PARAMETER_TYPE_PLACEHOLDER = "..."

def generate_template(function_signature: FunctionDTO) -> str:
    # Name logic
    if not function_signature.name:
        raise ValueError("The name of the function cannot be empty!")
    function_name = function_signature.name

    # Parameters logic
    function_params = []
    for input_name, input_type in function_signature.inputs:
        function_param = DOCSTRING_PARAMETER_TEMPLATE.format(
            param_name = input_name, 
            param_type = input_type if input_type else DOCSTRING_PARAMETER_TYPE_PLACEHOLDER)
        function_params.append(function_param)
    function_params_str = "".join(function_params)
    function_parameters = DOCSTRING_PARAMETERS_TEMPLATE.format(
        function_params_str = function_params_str) if function_params_str else ""
    
    # Output type
    function_output_type = function_signature.output_type
    function_output = DOCSTRING_OUTPUT_TEMPLATE.format(function_output_type = function_output_type) if function_output_type else ""

    # Final template
    return DOCSTRING_TEMPLATE.format(
        function_name = function_name,
        function_parameters = function_parameters,
        function_output = function_output)