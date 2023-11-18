from flask import Flask, render_template, request
import story_generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate_story():
    start_word = request.args.get('start')
    story = story_generator.generate_story(start_word)
    return story


if __name__ == '__main__':
    app.run(debug=True)
