import os
from flask import abort, Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "IT WORKS!!"

invalidEnds = {}
with open("Results2.txt", 'r') as file:
    lines = file.readlines()
    invalid = lines.index("Invalid Endpoints:\n")
    parking = lines.index("Parked Sites:\n")
    invalidLines = lines[invalid+1:parking]
    invalidEnds = []
    for l in invalidLines:
        if "{" in l:
            invalidEnds.append(eval(l.replace("\n", "")))
            
def make_txt():
    global invalidEnds    
    hzs = []
    sortedLines = []
    txt = ""

    for d in invalidEnds:
        hzName = d['Hosted Zone Name']
        if not (hzName in hzs):
            hzs.append(hzName)
    
    hzs.sort()            
    for h in hzs:
        for d in invalidEnds:
            if d['Hosted Zone Name'] == h:
                sortedLines.append(str(d))
                
    for s in sortedLines:
        if "{" in s:
            d = eval(s.replace("\n", ""))
            lineText = ""
            
            if d['Hosted Zone Name'][-1] == ".":
                d['Hosted Zone Name'] = d['Hosted Zone Name'][:-1]
                
            if hzName != d['Hosted Zone Name']:
                hzName = d['Hosted Zone Name']
                lineText += "\n\n\t\t\t "
                lineText += hzName + ":"
                
            if d['Entry'][-1] == ".":
                d['Entry'] = d['Entry'][:-1]
                
            if "https://" in txt:
                txt = txt.replace("https://", "")
            # d['Entry'] = d['Entry'].removeprefix("https://")
            d['Entry'] = " " + d['Entry']
            lineText += "\n" + d['Entry'] + ": "
                
            first = True
            for key in list(d.keys()):
                if not first:
                    lineText += ", "
                if d[key] and type(d[key]) != str:
                    lineText += key
                    first = False
            
            txt += lineText

    while txt.removeprefix("\n") != txt:
        txt = txt.removeprefix("\n")
        
    txt = f"\t\tTotal Number of URLS: {len(invalidEnds)}\n\n" + txt
    
    return txt
            
txt = make_txt()

@app.route('/reinvoke', methods=['POST', 'GET'])
def reinvoke():
    return "WOW!"
    if not (request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']):
        abort(400)

    return jsonify(
        response_type='in_channel',
        text=''
    )
    
@app.route('/getExpiresSoon', methods=['POST', 'GET'])
def getExpiresSoon():
    counter = 0
    temp_txt = ""
    for line in txt.split("\n"):
        if ("Expires within 90 Days" in line):
            temp_txt += " " + str(line) + "\n"
            counter += 1
            
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

    # if not (request.form['token'] == os.environ['SLACK_VERIFICATION_TOKEN']):
    #     abort(400)

    # return jsonify(
    #     response_type='in_channel',
    #     text=''
    # )
