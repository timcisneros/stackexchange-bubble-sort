import ast

def extract_functions(code):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        print(f"Failed to parse code: {e}")
        return []
    # Extract function definitions from the AST
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    # Convert the AST nodes back to source code
    return [ast.unparse(func).strip() for func in functions]

def validate_code_blocks(code_blocks):
    all_functions = []
    for code_block in code_blocks:
        functions = extract_functions(code_block)
        if functions:
            print("Successfully Extracted Functions:")
            for func in functions:
                print(func)
                all_functions.append(func)
        else:
            print("No valid Python function definitions found in the code block, skipping.")
    return all_functions
