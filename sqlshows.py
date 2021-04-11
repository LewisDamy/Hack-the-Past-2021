import cs50
import csv

#rewrite shows.db
open("shows.db", "r")
db = cs50.SQL("sqlite:///shows.db")


#db.execute("CREATE TABLE titlerating(tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT, averageRating NUMERIC, numVotes NUMERIC)")

db.execute("SELECT * FROM ratings.db JOIN shows.db")
#db.execute("SELECT * INTO titlerating FROM ratings.db")


# Select the top 10 movies from each decade from 60' up to 90'
# and display them into: primaryTitle/startYear/averageRating/numVotes/genres

for i in range(6, 10):
    print(f"Top films from the {i}0' decade:")

    for j in range(10):
        shows = db.execute(f"SELECT * FROM titlerating WHERE startYear >= 19{i}1 AND WHERE startYear <= 19{i + 1}0 LIMIT 10")
        print(shows)