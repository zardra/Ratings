import model
import csv
from datetime import datetime

def load_users(session):
    # use u.user
    with open("./seed_data/u.user", "rb") as f:
        reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in reader:
            email = row[0] + "@ratings.com"
            entry = model.User(id=row[0], email=email, password="password", age=row[1], zipcode=row[4])
            session.add(entry)
    session.commit()

def load_movies(session):
    # use u.item
    with open("./seed_data/u.item", "rb") as f:
        reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
        for row in reader:
            name = row[1].strip("()1234567890")
            name = name.decode("latin-1")
            if row[2]:
                date = datetime.strptime(row[2], "%d-%b-%Y")
                entry  = model.Movie(id=row[0], name=name, released_date=date, imdb_url=row[4])
                # print entry.name, entry.released_date, entry.imdb_url
            session.add(entry)
    session.commit()

def load_ratings(session):
    # use u.data
    with open("./seed_data/u.data", "rb") as f:
        reader = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        for row in reader:
            entry = model.Rating(movie_id=row[0], user_id=row[1], rating=row[2])
            # print entry.id, entry.movie_id, entry.user_id, entry.rating
            session.add(entry)
    session.commit()            

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
