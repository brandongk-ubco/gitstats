#!/usr/bin/env python

import gitstats
from datetime import datetime

# Install with:
# pip uninstall -y gitstats
# pip install --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.0.0/gitstats-1.0.0-py3-none-any.whl

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = "8eeb340597670d9169c9350f99aaefa39c1def03"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

start = datetime.fromisoformat('2020-09-02T10:30')

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        weeks=2)
print(stats)
