#!/usr/bin/env python

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.8/gitstats-1.0.8-py3-none-any.whl

import gitstats
from datetime import datetime

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "5f3e0e90d9d8309f5e63fef5dfe591674eb4634a"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

excluded_users = ["bohuie"]

start = datetime.fromisoformat('2020-09-09T10:30')
end = datetime.fromisoformat('2020-09-16T10:30')

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        end=end,
                        excluded_users=excluded_users)
print(stats)
