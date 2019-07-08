from datetime import datetime
from pathlib import Path

from rest_framework.views import APIView
from rest_framework.response import Response

from gcore.gcore.git_utils.commit_info_utils import get_repo_head_commit_info
from gcore.settings import BASE_DIR, SERVER_STARTED_TS


class RepositoryInfoView(APIView):
    """

    """
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        """
            {
                "commit": "aad95f46b5ee6abcd99c3a165aa20297642d38ec",  // хеш хед-коммита текущей ветки
                "commit_date": "2018-04-12T07:53:19Z",  // дата хед-коммита текущей ветки
                "branch": "feature/adding_status_info", // текущая ветка
                "version": "release_v1.16.1", // максимальный тег хед-коммита
                "started": "2018-04-12T09:33:25Z", // дата и время запуска приложения
                "uptime_seconds": 69470 // количество секунд между текущим временем на момент запроса и started
            }
        """
        now = datetime.now()
        uptime_seconds = (now - SERVER_STARTED_TS).total_seconds()

        repo_dir = Path(BASE_DIR)

        commit_info = get_repo_head_commit_info(repo_dir)

        git_repo_info = {
            "commit": '',
            "commit_date": '',
            "branch": commit_info['branch_name'],
            "version": '',
            "started": SERVER_STARTED_TS.isoformat(),  # TODO: add ts to timestamps
            "uptime_seconds": uptime_seconds,
        }

        return Response(git_repo_info)
