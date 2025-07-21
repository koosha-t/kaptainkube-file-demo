# API Documentation

## GitHub Utilities

### `save_file_to_repository()`

Save content to a file in a GitHub repository.

**Parameters:**
- `repo_name` (str): Name of the repository
- `file_path` (str): Path to the file in the repository
- `content` (str): File content as a string
- `commit_message` (str): Commit message for the change
- `branch` (str, optional): Branch to commit to (default: "main")
- `github_token` (str, optional): GitHub token (if not provided, loads from env)

**Returns:**
Dictionary containing file information from GitHub API

**Example:**
```python
result = save_file_to_repository(
    "my-repo",
    "src/main.py",
    "def main(): pass",
    "Add main function"
)
print(result["content"]["html_url"])
```
