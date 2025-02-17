import os
import logging
from typing import List, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_binary(file_path: str) -> bool:
    """Check if file is binary."""
    try:
        with open(file_path, 'tr') as check_file:
            check_file.read()
            return False
    except:
        return True

def append_to_master_file(file_path: str, master_file: str, project_root: str):
    """Append file content to master file, handling encoding issues."""
    if is_binary(file_path):
        logging.warning(f"Skipping binary file: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {str(e)}")
            return

    # Create a project-relative path
    project_relative_path = os.path.relpath(file_path, project_root)

    with open(master_file, 'a', encoding='utf-8') as master:
        master.write(f"\n\n# Content from {project_relative_path}\n\n{content}\n")

def should_skip(item: str) -> bool:
    """Check if an item should be skipped."""
    skip_list = [
        "node_modules", ".git", "__pycache__", ".next",
        ".env", ".gitignore", ".eslintrc.json", "package-lock.json"
    ]
    return any(skip in item for skip in skip_list)

def process_directory(directory: str, master_file: str, project_root: str, depth: int = 0) -> List[str]:
    """Process directory and append content to master file up to a certain depth."""
    if depth > 3:
        return []

    tree = []
    try:
        for item in sorted(os.listdir(directory)):
            if should_skip(item):
                continue

            item_path = os.path.join(directory, item)
            
            if os.path.isfile(item_path):
                tree.append(f"{'  ' * depth}├── {item}")
                append_to_master_file(item_path, master_file, project_root)
            elif os.path.isdir(item_path):
                tree.append(f"{'  ' * depth}├── {item}/")
                tree.extend(process_directory(item_path, master_file, project_root, depth + 1))
    except PermissionError:
        logging.warning(f"Permission denied: {directory}")

    return tree

def main(whitelist_dirs: List[str]):
    project_root = os.path.dirname(os.path.abspath(__file__))
    master_file = os.path.join(project_root, "output.txt")

    with open(master_file, 'w', encoding='utf-8') as f:
        f.write("Master Context\n\n")
        f.write("Project Tree:\n")

    full_tree = []
    for dir_name in whitelist_dirs:
        dir_path = os.path.join(project_root, dir_name)
        if os.path.exists(dir_path):
            logging.info(f"Processing directory: {dir_path}")
            full_tree.append(f"{dir_name}/")
            full_tree.extend(process_directory(dir_path, master_file, project_root))
        else:
            logging.warning(f"Directory not found: {dir_path}")

    # Insert the project tree at the beginning of the file
    with open(master_file, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write("Master Context\n\nProject Tree:\n")
        f.write("\n".join(full_tree))
        f.write("\n\nFile Contents:\n")
        f.write(content)

    logging.info("Context building completed successfully.")

if __name__ == "__main__":
    # List of directories to crawl
    whitelist_dirs = ["backend", "frontend", "src", "app", "components", "lib", "utils", "helpers", "config"]
    main(whitelist_dirs)