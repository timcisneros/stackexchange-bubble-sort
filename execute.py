import ast

def append_call_and_execute(func_defs, array_to_sort):
    """
    Executes the function definitions with the provided array.
    """
    if not func_defs:
        raise Exception("No function definitions provided.")

    combined_funcs = "\n".join(func_defs)
    func_name = extract_function_name(func_defs[0])
    if not func_name:
        raise Exception("Primary function name could not be extracted.")

    exec_code = f"{combined_funcs}\nresult = {func_name}(array_to_sort)"
    exec_globals = {'array_to_sort': array_to_sort, 'result': None}
    exec(exec_code, exec_globals)
    return exec_globals['result']

def extract_function_name(function_code):
    """
    Extracts the name of the first function defined in the given code string.
    """
    parsed_code = ast.parse(function_code)
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.FunctionDef):
            return node.name
    return None

