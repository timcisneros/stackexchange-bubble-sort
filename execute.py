import ast

def extract_function_name(function_code):
    """
    Extracts the name of the first function defined in the given code string.
    """
    try:
        parsed_code = ast.parse(function_code)
        for node in ast.walk(parsed_code):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except SyntaxError as e:
        print(f"Error parsing function code: {e}")
    return None


# execute one or more function definitions with the user-provided parameters
def append_call_and_execute(func_defs, *args, **kwargs):
    print("Starting function execution...")

    if not func_defs:
        print("No function definitions provided.")
        return None

    print(f"Received {len(func_defs)} function definitions.")
    combined_funcs = "\n".join(func_defs)
    print("Function definitions combined into a single code block.")
    
    func_name = extract_function_name(func_defs[0])
    if not func_name:
        print("Primary function name could not be extracted.")
        return None

    print(f"Prepared code for execution with primary function to execute: {func_name}")
    exec_code = f"""
{combined_funcs}

result = {func_name}(*args, **kwargs)
    """
    exec_env = {'args': args, 'kwargs': kwargs, 'result': None}
    
    try:
        exec(exec_code, exec_env, exec_env)
        print("Execution successful. Retrieving result...")
        # Check if args[0] has been modified and use it as the result if 'result' is None
        if exec_env['result'] is None and args:
            exec_env['result'] = args[0]  # Assumes the first argument is the list being sorted
        return exec_env['result']
    except Exception as e:
        print(f"Error during function call {func_name}: {e}")
        return None

