from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'hidden'

def get_interpretation(angel_number, mood, sun_sign, moon_sign, rising_sign):
    query = (
        f"Provide a call to action for someone who sees angel number {angel_number}. "
        f"Explain how this angel number is influenced by their sun sign ({sun_sign}), moon sign ({moon_sign}), "
        f"and rising sign ({rising_sign}). Additionally, suggest an activity or way to enjoy the moment for someone who is feeling {mood}."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in astrology and numerology, offering practical advice and enjoyment suggestions."},
                {"role": "user", "content": query}
            ],
            temperature=0.7
        )
        
        # Get the response content
        interpretation = response.choices[0].message["content"]

        # Replace newlines with HTML paragraph tags for better formatting
        paragraphs = interpretation.split("\n")
        formatted_interpretation = "".join(f"<p>{paragraph.strip()}</p>" for paragraph in paragraphs if paragraph.strip())

        return formatted_interpretation
    except Exception as e:
        return f"<p>Error: {e}</p>"


@app.route('/', methods=['GET', 'POST'])
def home():
    interpretation = None
    if request.method == 'POST':
        angel_number = request.form.get('angel_number')
        mood = request.form.get('mood')
        sun_sign = request.form.get('sun_sign')
        moon_sign = request.form.get('moon_sign')
        rising_sign = request.form.get('rising_sign')
        interpretation = get_interpretation(angel_number, mood, sun_sign, moon_sign, rising_sign)
    return render_template('index.html', interpretation=interpretation)

if __name__ == '__main__':
    app.run(debug=True)
