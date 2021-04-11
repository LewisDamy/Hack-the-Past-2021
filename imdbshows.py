import cs50
import csv

# Create database
open("shows.db", "w").close()
db = cs50.SQL("sqlite:///shows.db")

# Create table
db.execute("CREATE TABLE shows(tconst TEXT, primaryTitle TEXT, startYear NUMERIC, genres TEXT)")

# Open TSV file
#Download the Dataset from IMDb: https://datasets.imdbws.com/titles.basics.tsv.gz
with open("data.tsv", "r") as titles:

    # Create DictReader
    reader = csv.DictReader(titles, delimiter="\t")

    # Iterate over TSV file
    for row in reader:

        # If non-adult TV shows
        if row["titleType"] == "tvSeries" and row["isAdult"] == "0":

            # If year is not missing
            if row["startYear"] != "\\N":

                # If since 1920
                startYear = int(row["startYear"])
                if startYear >= 1920:

                    # Remove \N from genres
                    genres = row["genres"]

                    # Insert show
                    db.execute("INSERT INTO shows (tconst, primaryTitle, startYear, genres) VALUES(?, ?, ?, ?)", row["tconst"], row["primaryTitle"], startYear, genres)


