#!/usr/bin/env python

import gitstats
from datetime import datetime

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
