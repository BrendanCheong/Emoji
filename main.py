import os
import traceback
from SciHub import scihub
from flask import jsonify, request
from read_pdf import read_pdf
from app import app
from emojify.generator import EmojipastaGenerator
from emojify.emoji_move_script import script


generator = EmojipastaGenerator.of_default_mappings()

@app.route('/')
def hello():
    return 'Hello!!'

@app.route('/emoji', methods=['POST'])
def go_headless():
    try:
        _json = request.json
        doi_string = str(_json["doi"])
        if (scihub(doi_string)):
            extracted_text = read_pdf(doi_string)
            emoji_text = generator.generate_emojipasta(extracted_text)
            return jsonify({'success': True, 'msg': emoji_text})
        else:
            raise Exception("doi could not be processed")

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'success': False, 'msg': str(e)})

@app.route('/damn', methods=['GET'])
def emoji_movie():
    try:
        emoji_text = generator.generate_emojipasta(script)
        return jsonify({'success': True, 'msg': emoji_text})
    except Exception as e:
        print(traceback.format_exc())
        status = jsonify({'success': False, 'msg': str(e)})
        status.status_code = 404
        return status