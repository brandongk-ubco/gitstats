#!/usr/bin/env python

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.10/gitstats-1.0.10-py3-none-any.whl

import gitstats
from datetime import datetime

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "d39473c336540452c7808e30e0b51ad1c3f8957e"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

excluded_users = ["bohuie"]

start = datetime.fromisoformat('2021-01-28T13:00')
end = datetime.fromisoformat('2021-01-28T14:00')

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        end=end,
                        excluded_users=excluded_users)
print(stats)
