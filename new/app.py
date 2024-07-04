from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from macros import *
import os
import bcrypt
import jwt

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE')

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "everolla"
# app.config['MYSQL_PASSWORD'] = "Password12!"
# app.config['MYSQL_DB'] = "leodb"

mysql = MySQL(app)
CORS(app, support_credentials=True)
app.json.sort_keys= False

# List all users
@app.route('/user/list', methods=['GET'])
def get_users():
	cursor = None
	try:
		cursor = mysql.connection.cursor()
		cursor.execute("SELECT name_last_name, email, password FROM users")
		users = cursor.fetchall()
		user_data = [{'name_last_name': user[0], 'email': user[1], 'password': user[2]} for user in users]
		cursor.close()

	except Exception as err:
		cursor.close()
		print(f"Error retrieving users: {err}")
		return jsonify({'error': 'Error retrieving users'}), 500

	return jsonify(user_data), 200

def checkSQL(value):
	if not value:
		return True
	invalid_strings = ["'", '"', '\\', ';', '--', '%', 'DROP', 'SELECT', 'INSERT', 'DELETE', 'UPDATE', 'CREATE', 'ALTER', 'TRUNCATE', 'RENAME', 'REPLACE', 'GRANT', 'REVOKE', 'UNION', 'JOIN', 'FROM', 'WHERE', 'HAVING', 'ORDER', 'GROUP', 'BY', 'AS', 'ON', 'INTO', 'VALUES', 'SET', 'ADD', 'COLUMN', 'TABLE', 'DATABASE', 'INDEX', 'KEY', 'CONSTRAINT', 'PRIMARY', 'FOREIGN', 'CHECK', 'REFERENCES', 'DEFAULT', 'AUTO_INCREMENT', 'UNIQUE', 'NOT', 'NULL', 'AND', 'OR', 'XOR', 'IS', 'LIKE', 'IN', 'BETWEEN', 'EXISTS', 'ALL', 'ANY', 'SOME', 'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'JOIN', 'INNER', 'OUTER', 'LEFT', 'RIGHT', 'FULL', 'NATURAL', 'CROSS', 'USING', 'COUNT', 'SUM', 'AVG', 'MIN', 'MAX', 'AS', 'DISTINCT']
	for string in invalid_strings:
		if string in value:
			return True
	return False	


@app.route('/user/register/interest', methods=['POST', 'GET'])
def Interests():
	if request.method == 'POST':
		try:
			data = request.get_json()
			decod = data['jwt']
			encoded = decod.encode('utf-8')
			try:
				id = jwt.decode(encoded, 'secret', algorithms=['HS256'])
				id_user = id["id"]
			except Exception as err:
				print(f"Error decoding jwt: {err}")
				return jsonify({'error': 'Invalid input'}), 400
			for key in data:
				if key == 'jwt':
					continue
				if checkSQL(str(data[key])) or checkSQL(key) or not key.isnumeric():
					return jsonify({'error': 'Invalid input'}), 400
				value = data[key]
				cursor = mysql.connection.cursor()
				cursor.execute("INSERT INTO user_interests (priority, fk_id_interest, fk_id_user) VALUES (%s, %s, %s)", (value, key, id_user,))
				mysql.connection.commit()
				cursor.close()
			return jsonify({'message': 'Interests inserted successfully'}), 201

		except Exception as err:
			print(f"Error inserting interest: {err}")
			return jsonify({'error': 'Error inserting interest'}), 500


	if request.method == 'GET':
		try:
			cursor = mysql.connection.cursor()
			cursor.execute("SELECT * FROM interests")
			interests = cursor.fetchall()
			cursor.close()
		except Exception as err:
			print(f"Error retrieving interests: {err}")
			return jsonify({'error': 'Error retrieving interests'}), 500
		return jsonify(interests), 200

@app.route('/user/register/areaOfInterest', methods=['POST', 'GET'])
def setAreaOfInterest():
	if request.method == 'POST':
		try:
			data = request.get_json()
			decod = data['jwt']
			encoded = decod.encode('utf-8')
			try:
				id = jwt.decode(encoded, 'secret', algorithms=['HS256'])
				id_user = id["id"]
			except Exception as err:
				print(f"Error decoding jwt: {err}")
				return jsonify({'error': 'Invalid input'}), 400
			for key in data:
				if key == 'jwt':
					continue
				print(data[key], "key: ", key)
				if checkSQL(str(data[key])) or checkSQL(key) or not key.isnumeric():
					return jsonify({'error': 'Invalid input'}), 400
				match data[key]:
					case 4:
						print("4")
						value = Max_Aoi
					case 3:
						print("3")
						value = Second_Aoi
					case 2:
						print("2")
						value = Third_Aoi
					case 1:
						print("1")
						value = Last_Aoi
				print(key)
				cursor = mysql.connection.cursor()
				cursor.execute("INSERT INTO user_aoi (priority, fk_id_aoi, fk_id_user) VALUES (%s, %s, %s)", (value, key, id_user,))
				mysql.connection.commit()
			cursor.close()
			return jsonify({'message': 'Area of interest inserted successfully'}), 201
			
		except Exception as err:
			print(f"Error inserting interest: {err}")
			return jsonify({'error': 'Error inserting area of interest'}), 500
	
	if request.method == 'GET':
		try:
			cursor = mysql.connection.cursor()
			cursor.execute("SELECT * FROM aoi")
			areas = cursor.fetchall()
			cursor.close()
			return jsonify(areas), 200
		
		except Exception as err:
			print(f"Error retrieving areas of interest: {err}")
			return jsonify({'error': 'Error retrieving areas of interest'}), 500


# Register a new user
@app.route('/user/register', methods=['POST'])
def register():
	try:
		points = []
		data = request.get_json()
		points.append(data['name'])
		points.append(data['last_name'])
		points.append(data['email'])
		points.append(data['password'])
		points.append(data['birthdate'])
		points.append(data['address'])
		points.append(data['phone_number'])
		points.append(data['marital_status'])
		points.append(str(data['haschildren']))
		points.append(str(data['haselders']))
		for point in points:
			if checkSQL(point):
				return jsonify({'error': 'Invalid input'}), 400
			
		encoded = data['password'].encode('utf-8')
		hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
		cursor = mysql.connection.cursor()
		cursor.execute("INSERT INTO users (name, last_name, birthdate, email, password, address, phone_number, marital_status, children, elders) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (data["name"], data["last_name"], data["birthdate"], data["email"], hashed_password.decode(), data["address"], data["phone_number"], data["marital_status"], data["haschildren"], data["haselders"],))
		
		mysql.connection.commit()
		cursor.close()
		cursor2 = mysql.connection.cursor()
		cursor2.execute("SELECT id, name_last_name FROM users WHERE email = %s", (data["email"],))
		res = cursor2.fetchone()
		id = res[0]
		first_last_name = res[1]
		cursor2.close()
		
		return jsonify({'message': 'User registered successfully', 'jwt' : jwt.encode({"id" : id, "email" : data["email"], "first last name" : first_last_name}, 'secret', algorithm="HS256") }), 201

	except Exception as err:
		print(f"Error registering user: {err}")
		return jsonify({'error': 'Error registering user'}), 500

@app.route('/homepage', methods=['GET'])
def home():
	if request.method == 'GET':
		try:
			data = request.get_json()
			decod = data['jwt']
			encoded = decod.encode('utf-8')
			try:
				id = jwt.decode(encoded, 'secret', algorithms=['HS256'])
				id_user = id["id"]
			except Exception as err:
				print(f"Error decoding jwt: {err}")
				return jsonify({'error': 'Invalid input'}), 400
			if checkSQL(str(id_user)):
				return jsonify({'error': 'Invalid input'}), 400
			cursor = mysql.connection.cursor()
			cursor.execute("SELECT fk_id_interest, priority FROM user_interests WHERE fk_id_user = %s", (id_user,))
			interests = cursor.fetchall()
			cursor.close()
			cursor2 = mysql.connection.cursor()
			cursor2.execute("SELECT fk_id_aoi, priority FROM user_aoi WHERE fk_id_user = %s", (id_user,))
			areas = cursor2.fetchall()
			cursor2.close()
			valore_WellHub = areas[0][1] + interests[5][1]
			valore_4Books = areas[1][1] + interests[0][1]
			valore_Stimulus = areas[1][1] + interests[1][1]
			valore_JoJob = areas[2][1] + interests[2][1]
			valore_FlexibleBenefits = areas[3][1] + interests[3][1]
			Valore_Agreements = areas[3][1] + interests[4][1]
			return jsonify({"WellHub": valore_WellHub, "4Books": valore_4Books, "Stimulus": valore_Stimulus, "JoJob": valore_JoJob, "FlexibleBenefits": valore_FlexibleBenefits, "Agreements": Valore_Agreements}), 200

		except Exception as err:
			print(f"Error getting home page: {err}")
			return jsonify({'error': 'Error getting home page'}), 500


# Login
@app.route('/user/login', methods=['POST'])
def login():
	try:
		data = request.get_json()
		email = data['email']
		if checkSQL(email):
			return jsonify({'error': 'Invalid input'}), 400
		password = data['password']

		cursor = mysql.connection.cursor()
		cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
		result = cursor.fetchall()
		cursor.close()

		if not result:
			return jsonify({'error': 'Invalid email or password'}), 401

		if bcrypt.checkpw(password.encode('utf-8'), result[0][6].encode('utf-8')):
			token = jwt.encode({"id" : result[0][0], "email" : email, "first last name" : result[0][3]}, 'secret', algorithm='HS256')
			return jsonify({'message': 'User logged in sucessfully', 'jwt': token}), 200

		else:
			return jsonify({'error': 'Invalid email or password'}), 401

	except Exception as err:
		print(f"Error logging in: {err}")
		return jsonify({'error': 'Error logging in'}), 500

if __name__ == "__main__":
	app.run(debug=True, host='localhost', port=5000)

