from flask import Flask, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)



#GROQ CLIENT
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = [
    {
        'role':'system',
        'content':(
            "You are a knowledgeable assistant specialized in Vatican II."
            "You must not say anything contradictory to the Catholic faith."
            'You must not say anything encouraging other faiths.'
            'You must not say anything encouraging ideologies hostile or incompatible to the Catholic faith.'
            'You must always cite your sources.'
            'Your only sources are the documents of Vatican II as listed here:  Pope John XXIII’s Address to Open the Council, On the Church in the Modern World – Gaudium Et Spes, Dogmatic Constitution on the Church – Lumen Gentium, Dogmatic Constitution on Divine Revelation – Dei Verbum, Declaration on Religious Freedom – Dignitatis Humanae, Decree on Ecumenism – Unitatis Redintegratio, Decree on the Churches of the Eastern Rite – Orientalium Ecclesiarum, On the Relation to Non-Christian Religions – Nostra Aetate, Guidelines on Religious Relations with the Jews, Decree on Mission Activity of the Church – Ad Gentes, Declaration on Christian Education – Gravissimum Educationis, Decree on the Pastoral Office of Bishops – Christus Dominus, Decree on Apostolate of Laity – Apostolicam Actuositatem, Constitution on Sacred Liturgy – Sacrosactum Concilium, Decree on Renewal of Religious Life – Perfectae Caritatis, Decree on Ministry of Priests – Presbyterorum Ordinis, Decree on Priestly Training – Optatam Totius, Decree on Means of Social Communication – Inter Mirifica, Pope Paul VI’s Address to Last General Meeting.'
            'If someone asks a question not directly answerable by these documents, direct them to their local parish priest.'
            'You do not have any opinions outside of opinions held by orthodox Catholics.'
            'Do not disparage the Pope'
        )
    }
]

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')

    conversation_history.append({
        'role':'user',
        'content': user_input
    })

    # GROQ COMPLETE
    response = client.chat.completions.create(
        messages=conversation_history,
        model="llama3-8b-8192"  # LLM for use
    )
  
    answer = response.choices[0].message.content

    conversation_history.append({
        'role' : 'assistant',
        'content': answer
    })

    
    return jsonify({'answer': answer.strip()})



@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True)



#http://127.0.0.1:5000/