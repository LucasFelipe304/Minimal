# Minimal - Task List Manager

This Python script allows users to manage a task list directly from the terminal. The program offers features for adding, modifying, viewing, and deleting tasks. Tasks are automatically saved in a JSON file, ensuring they are available even after the program is closed.

## Code Structure

The code includes the following main sections:

- **User Interaction**: Terminal-based interface that displays a menu of options and accepts user input.
- **Task Management**:
  - Add new tasks.
  - Modify existing tasks.
  - Delete tasks by index.
  - View the full task list.
  
- **Data Persistence**: Tasks are saved in a `tasks.json` file and automatically loaded when the program starts. This ensures that users do not lose their tasks when they close the terminal.

## Features
  - Automatic File Creation: If the tasks.json file does not exist, it will be automatically created during the first run.
  - Task Persistence: Tasks are saved in the tasks.json file so that they are available across multiple runs of the program.
  - Simple Task Management: Add, modify, view, and delete tasks using simple terminal commands.
  - Error Handling: The code handles invalid inputs, such as out-of-range indices or incorrect characters.
  
## Requirements

To run this project, you need to have Python installed on your system.

## Installation Guide

### Windows

1. **Install Python**:
   - Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download and install Python for Windows, making sure to check the box that says "Add Python to PATH" during installation.

2. **Clone the repository**:
   Open Command Prompt and run:
   ```bash
   git clone <repository URL>
   cd <repository name>


3. **Run the script**: Once you're in the project directory, run:
   ```bash
   python <filename>.py

## Linux
1. **Install Python**:
    - Most Linux distributions come with Python pre-installed. If Python is not installed, open a terminal and run:
   ```bash
     sudo apt update
     sudo apt install python3
   ```
2. **Clone the repository**: Open the terminal and run:
   ```bash
   git clone <repository URL>
   cd <repository name>
  
3. **Run the script**: Once you're in the project directory, run:
   ```bash
   python <filename>.py

## Example
  After running the script, any added tasks will be saved to a JSON file. To see the contents of this file, you can open tasks.json directly or display it in the terminal using:
  ``` 
  cat tasks.json
 ```

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
