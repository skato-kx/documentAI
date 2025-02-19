from flask import Flask, request, render_template
import openai

app = Flask(__name__)

client = openai.OpenAI()

openai.api_key = "OPENAI_API_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input:
            summary = summarize_text(user_input)
    return render_template("index.html", summary=summary)

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"以下の文章を要約してください: {text}"}]
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)