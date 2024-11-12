import os
import random
import subprocess

from flask import Flask, jsonify, send_file

app = Flask(__name__)

# Set the directory where the memes are stored
MEME_DIRECTORY = '/app/llama'

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200


@app.route('/meme_me', methods=['GET'])
def get_random_meme():
    # Get a list of all the files in the meme directory
    meme_files = os.listdir(MEME_DIRECTORY)

    # Check if there are any memes in the directory
    if not meme_files:
        return 'No memes found in the directory', 404

    # Select a random meme from the list
    random_meme = random.sample(meme_files, 1)[0]

    # Construct the full path to the meme file
    meme_path = os.path.join(MEME_DIRECTORY, random_meme)

    # Determine the file type and set the appropriate mimetype
    if random_meme.endswith('.jpg') or random_meme.endswith('.jpeg'):
        mimetype = 'image/jpeg'
    elif random_meme.endswith('.png'):
        mimetype = 'image/png'
    elif random_meme.endswith('.gif'):
        mimetype = 'image/gif'
    else:
        return f'Unsupported file type: {random_meme}', 400

    # Return the meme as a file
    return send_file(meme_path, mimetype=mimetype)


@app.route('/meme_me_sh', methods=['GET'])
def get_random_meme_sh():
    # Call the Bash script to get the meme file path and mimetype
    try:
        output = subprocess.check_output(['bash', '/app/meme_me.sh'], universal_newlines=True)
        meme_path, mimetype = output.strip().split('\n')
    except subprocess.CalledProcessError as e:
        return e.output, 404

    # Return the meme as a file
    return send_file(meme_path, mimetype=mimetype)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
