#!/usr/bin/env python

import gitstats
from datetime import datetime

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.3/gitstats-1.0.3-py3-none-any.whl

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "593dbe85dc185af39f70710ecf67703798449d0a"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

start = datetime.fromisoformat('2020-09-02T10:30')
end = datetime.fromisoformat('2020-09-23T10:30')

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        end=end)

print(stats)
