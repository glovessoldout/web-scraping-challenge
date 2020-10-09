from flask import Flask, render_template
from flask_pymongo import PyMongo
from scrape_mars import scrape
import pandas as pd

app = Flask(__name__)

# conn = 'mongodb://localhost:27017/webscraping'
# client = pymongo.MongoClient(conn)
# db = client.webscraping
# collection = db.webscraping
webscraping = PyMongo(app, uri="mongodb://localhost:27017/webscraping")


@app.route("/scrape")
def mars_scrape():
    mars = webscraping.db.webscraping
    mars_data = scrape()
    mars.update({}, mars_data, upsert=True)
    print("mars scrapped and loaded into mongo")
    return("data scraped 100%")
    
@app.route("/")
def mongo_import():
    results = webscraping.db.webscraping.find()
    return(render_template("index.html", results=results))

if __name__ == "__main__":
    app.run()