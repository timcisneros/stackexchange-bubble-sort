import ast

def validate_code_blocks(code_blocks):
    """
    Validates and extracts function definitions from code blocks.
    """
    for code_block in code_blocks:
        try:
            tree = ast.parse(code_block)
            functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            if functions:
                return [ast.unparse(func).strip() for func in functions]
        except SyntaxError:
            continue
    raise Exception("No valid Python function definitions found in the code blocks.")
