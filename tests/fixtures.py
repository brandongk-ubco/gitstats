import pandas as pd
from datetime import datetime, timezone

prs = pd.DataFrame.from_records([{
    "id": 0,
    "date": datetime.now(timezone.utc),
    "assignee": "Bob",
    "merged": False
}, {
    "id": 1,
    "date": datetime.now(timezone.utc),
    "assignee": "Bob",
    "merged": False
}, {
    "id": 0,
    "date": datetime.now(timezone.utc),
    "assignee": "Joan",
    "merged": False
}])

comments = pd.DataFrame.from_records([{
    "pr": 0,
    "date": datetime.now(timezone.utc),
    "user": "Bob",
    "id": 0,
    "type": "review"
}])

commits = pd.DataFrame.from_records([{
    "pr": 0,
    "date": datetime.now(timezone.utc),
    "user": "Bob",
    "additions": 100,
    "deletions": 100,
    "changes": 200,
    "id": 0
}])
