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
goodGeorge = make_record("GoodGeorge",
                         changes=500,
                         commits=2,
                         comments=5,
                         contributed=5)
slackerSam = make_record("SlackerSam",
                         changes=50,
                         commits=1,
                         comments=2,
                         contributed=2)
loneWolfLarry = make_record("LoneWolfLarry",
                            changes=1000,
                            commits=10,
                            comments=5,
                            contributed=1)

scenarios = [[weekOffWally], [slackerSam], [goodGina], [heroHolly],
             [weekOffWally, heroHolly], [goodGina, heroHolly],
             [goodGina, heroHolly], [goodGeorge, heroHolly],
             [slackerSam, goodGina], [goodGeorge, goodGina],
             [slackerSam, goodGina, heroHolly], [heroHenry, heroHolly],
             [heroHenry, heroHolly, loneWolfLarry]]

scenarios = [pd.DataFrame.from_records(i) for i in scenarios]
