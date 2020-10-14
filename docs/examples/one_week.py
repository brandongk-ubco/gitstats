#!/usr/bin/env python

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.5/gitstats-1.0.5-py3-none-any.whl

import gitstats
from datetime import datetime

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "4c0e8448198305c44d553f71bda03404bffc9be1"
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
