# Stack Exchange Bubble Sort

This Python project demonstrates a dynamic approach to fetching, validating, and executing bubble sort algorithm implementations from Stack Overflow. It utilizes the Stack Exchange API to retrieve a random bubble sort implementation tagged with `python` and `bubble-sort`, validates the fetched code, and then executes it to sort a user-provided list of integers.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.6+
-   pip (Python package manager)
-   Virtual environment (optional but recommended)

### Setting Up

1. **Clone the repository**

    ```bash
    git clone https://github.com/timcisneros/bubble-sort-fetcher.git
    cd stackexchange-bubble-sort
    ```

2. **Set up a virtual environment (Optional)**

    - Create a virtual environment:

        ```bash
        python -m venv venv
        ```

    - Activate the virtual environment:

        - On Windows:

            ```bash
            .\\venv\\Scripts\\activate
            ```

        - On macOS and Linux:

            ```bash
            source venv/bin/activate
            ```

3. **Install required packages**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Program

1. Ensure your virtual environment is activated if you are using one.
2. Run the program:

    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to provide a list of integers you wish to sort.

## How It Works

-   **main.py**: Serves as the entry point of the program. It prompts the user for a list of integers, fetches a random bubble sort implementation, validates it, and then executes it to sort the provided list.
-   **fetch_bubble_sort_implementation_randomly**: Utilizes the Stack Exchange API to fetch posts tagged with `python` and `bubble-sort`, randomly selects an accepted answer, and extracts code blocks that potentially contain a bubble sort implementation.
-   **validate_code_blocks**: Parses the fetched code blocks to ensure they are valid Python functions. It filters out non-functional code snippets and prepares them for execution.
-   **append_call_and_execute**: Dynamically executes the validated bubble sort function definitions with the user-provided list of integers, sorts the list, and outputs the result.
