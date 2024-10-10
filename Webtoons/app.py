from flask import Flask ,request ,jsonify
from database import init_db, db



app = Flask(__name__)
init_db(app)

@app.route('/')
def home():
    default_msg = ["Please create a Database and Assign DB URL into DATABASE_URL variable in .env file "," Create a table with following attributes ","sql","CREATE TABLE webtoons (","id SERIAL PRIMARY KEY,","title VARCHAR(255) NOT NULL,","summary TEXT,","characters TEXT[] NOT NULL",");","GET /webtoons: Fetch all webtoons with basic details (title, description, characters).","POST /webtoons: Add a new webtoon entry, including title, summary, and characters.","GET /webtoons/ : Fetch a specific webtoon by its ID, returning detailed information. ","DELETE /webtoons/ : Remove a webtoon entry by its ID. "," Make sure to install all the required modules from the 'requirements.txt'"]
    msg= "\n".join(default_msg)
    return default_msg


class Webtoon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    characters = db.Column(db.ARRAY(db.String), nullable=False)


@app.route('/webtoons', methods=['GET'])
def get_webtoons():
    try:
        webtoons = Webtoon.query.all()
        return jsonify([{
            'id': w.id,
            'title': w.title,
            'description': w.description,
            'characters': w.characters
        } for w in webtoons]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/webtoons', methods=['POST'])
def add_webtoon():
    try:
        data = request.json
        new_webtoon = Webtoon(
            title=data['title'],
            description=data['description'],
            characters=data['characters']
        )
        db.session.add(new_webtoon)
        db.session.commit()
        return jsonify({'id': new_webtoon.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/webtoons/<int:webtoon_id>', methods=['GET'])
def get_webtoon_by_id(webtoon_id):
    try:
        webtoon = Webtoon.query.get_or_404(webtoon_id)
        return jsonify({
            'id': webtoon.id,
            'title': webtoon.title,
           'description': webtoon.description,
           'characters': webtoon.characters
         }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/webtoons/<int:webtoon_id>', methods=['DELETE'])
def delete_webtoon(webtoon_id):
    try:
        webtoon = Webtoon.query.get_or_404(webtoon_id)
        db.session.delete(webtoon)
        db.session.commit()
        return jsonify({'message': 'Webtoon deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500