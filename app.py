from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import connect
import random
import os

app = Flask(__name__)

# MySQL configurations
db = mysql.connector.connect(
    host="localhost",
    user="bharrat",
    password="bharrat7777",
    database="baby_names"
)


def get_random_baby_name(gender):
    cursor = db.cursor()
    query = "SELECT name FROM baby_names WHERE gender = %s"
    cursor.execute(query, (gender,))
    names = cursor.fetchall()  # Fetch all names as tuples
    cursor.close()

    if names:  # Check if any names were found
        return random.choice(names)[0]  # Randomly choose a name and extract the first element (the name itself)
    else:
        return None  # Handle the case where no names were found




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gender = request.form.get('gender')
        random_name = get_random_baby_name(gender)
        return render_template('index.html', random_name=random_name)  # Pass the random_name to the template

    return render_template('index.html', names=None)

if __name__ == '__main__':
    # Use PORT environment variable if available (for potential hosting environments)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)