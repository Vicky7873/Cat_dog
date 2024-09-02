import os
import sys
from pathlib import Path


list_of_folders = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"src/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/components/__init__.py",
    f"src/logging/__init__.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for folder in list_of_folders:
    path = Path(folder)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        with open(path, "w") as f:
            pass
        print(f"Created: {path}")