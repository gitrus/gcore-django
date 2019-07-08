from pathlib import Path
from typing import Dict

from git import Repo


def get_repo_head_commit_info(repo_path: Path) -> Dict[str, str]:
    repo = Repo(repo_path)

    commit_info = {
        'branch_name': repo.head.name
    }

    return commit_info
