from collections import defaultdict
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
    words = all_words(v)
    words.sort()
    word_queries = defaultdict(lambda l=len(words): [0]*l)
    word_queries.update({i: to_list(words, v) for (i, (_, v)) in queries.items()})
    word_queries[-1] = to_list(words, v)
    words = list(enumerate(words))
    lengths = {i: len(v) for (i, (_, v)) in queries.items()}
    kalimat = {i: html_getter.get_file_unclean(f'test/query_{i}.html')[:150]+"..." for (i, (url, _)) in queries.items()}
    return render_template("search.html",
                           queries=queries,
                           term=term,
                           search=l,
                           lengths=lengths,
                           kalimat=kalimat,
                           words=words,
                           word_queries=word_queries
                           )

@app.route("/perihal")
def perihal():
    return render_template("perihal.html")

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
