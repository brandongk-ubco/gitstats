import pandas as pd


def make_record(user, changes=0, commits=0, comments=0, contributed=0):
    return {
        "user": user,
        "changes": changes,
        "commits": commits,
        "comments": comments,
        "contributed": contributed
    }


weekOffWally = make_record("WeekOffWally")
heroHolly = make_record("HeroHolly",
                        changes=5000,
                        commits=20,
                        comments=20,
                        contributed=10)
heroHenry = make_record("HeroHenry",
                        changes=4500,
                        commits=15,
                        comments=15,
                        contributed=10)
goodGina = make_record("GoodGina",
                       changes=1000,
                       commits=5,
                       comments=20,
                       contributed=10)
slackerSam = make_record("SlackerSam",
                         changes=50,
                         commits=1,
                         comments=2,
                         contributed=2)

scenarios = [[weekOffWally], [slackerSam], [goodGina], [heroHolly],
             [weekOffWally, heroHolly], [goodGina, heroHolly],
             [goodGina, heroHolly], [slackerSam, goodGina],
             [slackerSam, goodGina, heroHolly], [heroHenry, heroHolly]]

scenarios = [pd.DataFrame.from_records(i) for i in scenarios]
