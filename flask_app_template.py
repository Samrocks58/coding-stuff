import os
from flask import abort, Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "IT WORKS!!"


      
@app.route('/getExpiresSoon', methods=['POST', 'GET'])
def getExpiresSoon():
    counter = 0
    # temp_txt = ""
    # for line in txt.split("\n"):
    #     if ("Expires within 90 Days" in line):
    #         temp_txt += " " + str(line) + "\n"
    #         counter += 1
            
    temp_txt = "\t\t\tNumber of URLS: " + str(counter) + "\n\n" + temp_txt
    
    return temp_txt
    # if not (request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']):
    #     abort(400)

    # return jsonify(
    #     response_type='in_channel',
    #     text=''
    # )
    
@app.route('/getDomainError', methods=['POST', 'GET'])
def getDomainError():
    counter = 0
    temp_txt = ""
    for line in txt.split("\n"):
        if ("Incorrect Domain Configuration" in line):
            temp_txt += " " + str(line) + "\n"
            counter += 1
            
    temp_txt = "\t\t\tNumber of URLS: " + str(counter) + "\n\n" + temp_txt
    
    return temp_txt
