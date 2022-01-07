import os
import traceback
from SciHub import scihub
from flask import jsonify, request
from read_pdf import read_pdf
from app import app
from emojify.generator import EmojipastaGenerator
from emojify.emoji_move_script import script


generator = EmojipastaGenerator.of_default_mappings() # turns input text into emojis

@app.route('/')
def hello():
    return 'Hello!!'

@app.route('/emoji', methods=['POST'])
def go_headless():
    try:
        _json = request.json
        doi_string = str(_json["doi"])
        if (scihub(doi_string)): # first we input the inputted doi string into the scihub webscraper and get the pdf
            extracted_text = read_pdf(doi_string) # then we extract text from the pdf
            emoji_text = generator.generate_emojipasta(extracted_text) # convert text to emojis
            return jsonify({'success': True, 'msg': emoji_text})
        else:
            raise Exception("doi could not be processed")

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'success': False, 'msg': str(e)})

@app.route('/damn', methods=['GET'])
def emoji_movie():
    try:
        emoji_text = generator.generate_emojipasta(script) # by default if the dois cannot be found by the scraper frontend will go to this route
        return jsonify({'success': True, 'msg': emoji_text})
    except Exception as e:
        print(traceback.format_exc())
        status = jsonify({'success': False, 'msg': str(e)})
        status.status_code = 404
        return status