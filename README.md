
---

# AI File System Agent

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Powered by uv](https://img.shields.io/badge/powered%20by-uv-green.svg)](https://github.com/astral-sh/uv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet powerful AI agent built with Python and Google's Gemini API that can interact with your local file system. This project was created primarily as a **learning exercise** to explore the capabilities of Large Language Models (LLMs) through "function calling".

This project uses **[uv](https://github.com/astral-sh/uv)**, an extremely fast Python package installer and resolver, to manage its environment and dependencies.

---

> ## ⚠️ **Warning: Use With Extreme Caution**
>
> This agent is capable of making real changes to your file system, including **creating, renaming, and permanently deleting files and directories**. It is strongly recommended to run this agent in a sandboxed, controlled environment (like a dedicated folder or a virtual machine) and to never run it with administrative privileges. The author is not responsible for any data loss.

---

## Core Concept

This agent uses a natural language interface to translate user requests into concrete actions. When you ask it to do something, it doesn't just generate text; it uses the Gemini model to decide which of its available "tools" (Python functions) to use and with what arguments.

The agent's "brain" is the Gemini LLM, and its "hands" are a set of Python functions that can interact with the file system.

## Agent Capabilities

The agent is equipped with the following tools, allowing it to perform a range of file operations:

-   `get_current_path()`:
    -   **Description**: Finds out which directory it's currently in.
    -   **Example Prompt**: "Where am I?" or "What is the current path?"

-   `get_directory_content(path)`:
    -   **Description**: Lists all files and subdirectories within a given path in a tree-like format.
    -   **Example Prompt**: "Show me the files in the current directory." or "What's inside the `src` folder?"

-   `create_path(path)`:
    -   **Description**: Creates new files or directories. It's smart enough to create parent directories if they don't exist.
    -   **Example Prompt**: "Create a new folder called `documents`." or "Make an empty file named `notes.txt` inside `documents`."

-   `rename_path(source, destination)`:
    -   **Description**: Renames or moves a file or directory from a source path to a destination path.
    -   **Example Prompt**: "Rename `notes.txt` to `important_notes.txt`." or "Move the `images` folder into `documents`."

-   `delete_path(path)`:
    -   **Description**: **Permanently deletes** a file or an entire directory and all of its contents.
    -   **Example Prompt**: "Delete the `cache` folder." or "Remove the file `temp.log`."

## Getting Started

Follow these steps to get the agent running on your local machine.

### Prerequisites

-   Python 3.12+
-   **`uv`**: You need `uv` installed. If you don't have it, see the official [installation guide](https://github.com/astral-sh/uv#installation).
-   An API key from [Google AI Studio](https://aistudio.google.com/).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ProImpact/AI-File-System-Agent.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment using `uv`:**
    ```bash
    uv venv
    source .venv/bin/activate
    ```

3.  **Install dependencies using `uv`:**
    The `sync` command installs all dependencies specified in `pyproject.toml` into the virtual environment, making it a perfect match.
    ```bash
    uv pip sync
    ```

4.  **Set up your API Key:**
    Create a `.env` file in the root of the project by copying the example file.
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and add your Google API Key:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

Run the main script to start the interactive agent.

```bash
python main.py
```

You will be greeted by the agent and can start giving it commands in plain English.

### Example Interaction

```
🤖✨ File System Agent Initialized ✨🤖
Enter your request. Type 'exit' or 'quit' to leave.

👤 User: list all files
🤖 Thinking... ⠋
⚙️ Agent wants to use the tool: get_directory_content
▶️  Arguments: {'start_path': '.'}
✅ Tool result: ./
    main.py
    src/
    .env
    ...
🤖 Agent: Here is the content of the current directory: ...

------------------------------
👤 User: create a new folder called my_new_project/
🤖 Thinking... ⠴
⚙️ Agent wants to use the tool: create_path
▶️  Arguments: {'path': 'my_new_project/'}
✅ Tool result: ✅ Directory created or already exists at: 'my_new_project'
🤖 Agent: I have successfully created the directory 'my_new_project/'.

------------------------------
👤 User: exit
🤖 Agent: Goodbye!
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.