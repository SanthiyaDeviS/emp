from flask import Flask, request, jsonify
import logging
import json
from datetime import datetime, timedelta, date
from collections import defaultdict
import getpass

app = Flask(__name__)


logging.basicConfig(filename='emp_checkin.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

with open('user_credentials.json') as f:
    user_credentials = json.load(f)


@app.route('/login', methods=['GET'])

def login():
    # username = request.form.get('username')
    # password = request.form.get('password')
    username="pooja"
    password="123"

    if username in user_credentials and user_credentials[username]['password'] == password:
        logging.info(f"User {username} logged in.")
        return jsonify({'message': 'You have successfully logged in', 'is_admin': user_credentials[username]['is_admin']}), 200
        return jsonify("You have successfully logged in")
    else:
        logging.error("Invalid username or password")
        return jsonify({'error': 'Invalid username or password'}), 401
        return jsonify("Invalid username or password")

@app.route('/logs', methods=['GET']) 
def logs():
    return jsonify("Hii")



# @app.route('/', methods=['POST'])
# def logout():
#     username = request.json.get('username')
#     with open('emp_checkin.log', 'r') as log_file:
#         logged_in = False
#         for line in log_file:
#             if f"User {username} logged in" in line:
#                 logged_in = True
#             elif f"User {username} logged out" in line:
#                 logging.info(f"User {username} logged out.")
#                 return jsonify({'message': 'You have logged out successfully'}), 200
#         if not logged_in:
#             logging.warning(f"User {username} attempted to logout without logging in")
#             return jsonify({'error': 'User has not logged in'}), 400

# @app.route('/')
# def admin_summary():
#     user_sessions = defaultdict(list)
#     with open('emp_checkin.log', 'r') as log_file:
#         for line in log_file:
#             if "User" in line and "logged in" in line:
#                 username = line.split("User ")[1].split()[0]
#                 login_time = datetime.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f')
#                 user_sessions[username].append({'login_time': login_time, 'logout_time': None})
#             elif "User" in line and "logged out" in line:
#                 username = line.split("User ")[1].split()[0]
#                 logout_time = datetime.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f')
#                 if user_sessions[username]:
#                     user_sessions[username][-1]['logout_time'] = logout_time

#     summary = {}
#     for user, sessions in user_sessions.items():
#         if user_credentials.get(user, {}).get('is_admin'):
#             continue
#         user_summary = {}
#         consolidated_hours = calculate_consolidated_hours(sessions)
#         for date, duration in consolidated_hours.items():
#             formatted_duration = format_timedelta(duration)
#             user_summary[date.strftime('%Y-%m-%d')] = formatted_duration
#         summary[user] = user_summary
#     return jsonify(summary), 200

# @app.route('//<username>')
# def user_summary(username):
#     present_date = date.today()
#     present_day_sessions = []
#     all_sessions = defaultdict(list)

#     with open('emp_checkin.log', 'r') as log_file:
#         for line in log_file:
#             if f"User {username} logged in" in line:
#                 login_time = datetime.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f')
#                 all_sessions[login_time.date()].append(login_time)
#                 if login_time.date() == present_date:
#                     present_day_sessions.append(login_time)
#             elif f"User {username} logged out" in line:
#                 logout_time = datetime.strptime(line.split(' - ')[0], '%Y-%m-%d %H:%M:%S,%f')
#                 all_sessions[logout_time.date()].append(logout_time)
#                 if logout_time.date() == present_date:
#                     present_day_sessions.append(logout_time)

#     summary = {}
#     present_day_sessions = sorted(present_day_sessions)
#     for i in range(0, len(present_day_sessions), 2):
#         session_summary = {}
#         session_summary['login_time'] = present_day_sessions[i].strftime('%Y-%m-%d %H:%M:%S')
#         if i+1 < len(present_day_sessions):
#             session_summary['logout_time'] = present_day_sessions[i+1].strftime('%Y-%m-%d %H:%M:%S')
#         else:
#             session_summary['logout_time'] = 'Not logged out yet'
#         summary[f'Session {i//2 + 1}'] = session_summary

#     if len(present_day_sessions) % 2 != 0:
#         summary['Last session'] = 'Not logged out yet'

#     all_sessions_summary = {}
#     for login_date, sessions in all_sessions.items():
#         hours = 0
#         minutes = 0
#         for i in range(0, len(sessions), 2):
#             login_time = sessions[i]
#             if i + 1 < len(sessions):
#                 logout_time = sessions[i + 1]
#                 duration = (logout_time - login_time).total_seconds()
#                 hours += int(duration // 3600)
#                 minutes += int((duration % 3600) // 60)
#         all_sessions_summary[login_date.strftime('%Y-%m-%d')] = f"{hours} hours {minutes} minutes"

#     return jsonify({'daily_summary': summary, 'all_sessions_summary': all_sessions_summary}), 200

# def calculate_consolidated_hours(sessions):
#     consolidated_hours = defaultdict(timedelta)
#     for session in sessions:
#         login_time = session['login_time']
#         logout_time = session['logout_time'] or datetime.now()
#         session_duration = logout_time - login_time
#         consolidated_hours[login_time.date()] += session_duration
#     return consolidated_hours

# def format_timedelta(delta):
#     total_seconds = delta.total_seconds()
#     hours = int(total_seconds // 3600)
#     minutes = int((total_seconds % 3600) // 60)
#     return f"{hours} hours {minutes} minutes"

if __name__ == '__main__':
    app.run(debug=True)
