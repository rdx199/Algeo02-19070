from flask import Flask, render_template, request

import vektorkata, html_getter

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == 'GET':
        term = request.args.get('s')
    elif request.method == 'POST':
        term = request.form['query']
    v = vektorkata.VektorBuilder.build_vektor(term)
    l = sort_similiarity(v)
    print(all_words(v))
    return render_template("search.html",
                           queries=queries,
                           search=l,
                           lengths={i: len(v[1]) for (i, v) in queries.items()},
                           kalimat={i: html_getter.get_url_unclean(url)[:100]+"..." for (i, (url, _)) in queries.items()})

def all_words(term):
    return list(sum(map(lambda x: x[1], queries.values()), term))

def to_list(list_kata, v):
    return [1 if i in v else 0 for i in list_kata]

def sort_similiarity(v):
    l = [(i, vektorkata.similiarity(v, v2)) for (i, (_, v2)) in queries.items()]
    l.sort(key=lambda x: x[1], reverse=True)
    return l

def init(*, _queries):
    global queries
    queries = _queries

if __name__ == "__main__":
    app.run(debug=True)