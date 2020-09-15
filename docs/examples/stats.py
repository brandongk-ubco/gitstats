#!/usr/bin/env python

import gitstats

access_token = "b4a7e03e2600da188608c22ec5de20bb36109e2d"
repository = "brandongk-ubco/gitstats"
group_name = "gitstats"

stats = gitstats.report(access_token, group_name, repository)
print(stats)
