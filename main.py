from request import fetch_bubble_sort_implementation_randomly
from validate import validate_code_blocks
from execute import append_call_and_execute

def main():
    print("Hello! Please provide a list of integers.")
    
    input_str = input()
    
    try:
        input_list = [int(x.strip()) for x in input_str.split(',')]
        print("Thanks. Fetching a random bubble sort implementation. Fingers crossed.")
    except ValueError:
        print("Please ensure you enter a list of integers separated by commas.")
        return
    
    code_blocks = fetch_bubble_sort_implementation_randomly()
    if not code_blocks:
        print("Failed to fetch code blocks.")
        return

    validated_code_block = validate_code_blocks(code_blocks)
    print("Validating code blocks...")
    if not validated_code_block:
        print("Failed to validate code blocks.")
        return

    try:
        sorted_list = append_call_and_execute(validated_code_block, input_list)
        print("Sorted List:", sorted_list)
    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    main()