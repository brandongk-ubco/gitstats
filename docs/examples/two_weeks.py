#!/usr/bin/env python

import gitstats
from datetime import datetime

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.1.0/gitstats-1.1.0-py3-none-any.whl

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "21b2a4fb3ca8e7405e8623aefc715f7911485e5e"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

excluded_users = ["bohuie"]

start = datetime.fromisoformat('2020-09-02T10:30')
end = datetime.fromisoformat('2020-09-16T10:30')

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        end=end,
                        excluded_users=excluded_users)

print(stats)
