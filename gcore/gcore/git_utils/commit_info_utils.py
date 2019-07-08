from pathlib import Path
from typing import Dict

from git import Repo


def get_repo_head_commit_info(repo_path: Path) -> Dict[str, str]:
    repo = Repo(repo_path)

    branch = repo.active_branch
    commit = branch.commit

    all_tags = repo.tags
    commit_tags = list(filter(lambda tag: tag.commit.binsha == commit.binsha, all_tags))

    commit_latest_tag_name = next(reversed(commit_tags)).name if commit_tags else ''

    commit_info = {
        "branch_name": repo.active_branch.name,
        "commit_hash": commit.hexsha,
        "commit_ts": commit.committed_datetime,
        "commit_tags": commit_latest_tag_name,
    }

    return commit_info
