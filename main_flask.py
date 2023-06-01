import sys

sys.path.insert(0, 'pkg/oasis_ai')

from pkg.oasis_ai.command_analyzer import CommandAnalyzer

from flask import Flask, jsonify, request
app = Flask(__name__, static_url_path='/', static_folder='public')

commandAnalyzer = CommandAnalyzer()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/ping")
def ping():
    return jsonify({ 'msg': 'pong' })

@app.route("/api/cmd/", methods=['POST'])
def execute_cmd():
    try:
        execution_result = commandAnalyzer.execute_command(request.json['cmd_text'])
        query_result = str(execution_result['source'])
        return jsonify({ 'answer_text': query_result })
    except Exception:
        return jsonify({ 'answer_text': "Ooops... Sorry, I can't handle your query!" })

if __name__ == "__main__":
    app.run()