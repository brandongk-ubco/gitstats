#!/usr/bin/env python

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.10/gitstats-1.0.10-py3-none-any.whl

import gitstats
from datetime import datetime

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "21b2a4fb3ca8e7405e8623aefc715f7911485e5e"
repositories = [
    "brandongk-ubco/gitstats",
    "brandongk-ubco/segmenter",
]
group_name = "gitstats"

excluded_users = ["bohuie"]

start = datetime.fromisoformat('2020-09-09T10:30')
end = datetime.fromisoformat('2020-09-16T10:30')

stats = gitstats.report(access_token,
                        group_name,
                        repositories,
                        start=start,
                        end=end,
                        excluded_users=excluded_users)
print(stats)
