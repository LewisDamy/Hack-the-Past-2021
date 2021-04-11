import cs50
import csv
import sqlite3

# Create database
open("ratings.db", "w").close()
db = cs50.SQL("sqlite:///ratings.db")

# Create table
db.execute("CREATE TABLE rating(tconst TEXT, averageRating NUMERIC, numVotes NUMERIC)")

# Open TSV file
#Download the Dataset from IMDb: https://datasets.imdbws.com/titles.basics.tsv.gz
with open("ratingshows.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

            numVotes = int(row["numVotes"])
            averageRating = row["averageRating"]


            # Insert show
            db.execute("INSERT INTO rating (tconst, averageRating, numVotes) VALUES(?, ?, ?)", row["tconst"], averageRating, numVotes)

