from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = "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"

def generate_response(prompt, model):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=2048
    )
    return response.choices[0].text

@app.route('/', methods=['GET', 'POST'])
def chat():
    model = "text-davinci-002"
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = generate_response(prompt, model)

        return {'response': response}
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
