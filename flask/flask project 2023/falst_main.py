from flask import render_template, Flask,jsonify,request
app = Flask(__name__)
list_data = { "python":1, "go":2 } 

@app.route('/' , methods=['GET'])
def hello():
    return jsonify({"yes":"1111"})

@app.route('/lang/<string:name>/' , methods=['GET'])
def check_lan(name):
    return jsonify(list_data.get(name))


@app.route('/addlang/' , methods=['POST'])
def add_lan():
    data =  request.json['new']
    return data

@app.route('/editlang/<string:name>/' , methods=['PUT'])
def edit_lan(name):
    data =  request.json
    print("data",name)
    return ""

@app.route('/get_template/' , methods=['GET'])
def get_template_data():
    ll = [ 1,2,3,4,5]
    return render_template("home.html",name="Rahul",flag=True,ll=ll)


@app.before_request
def before_request_func():
    print("Before each request is executed.")
    

@app.after_request
def after_request_func(response):
    print(f"After {request.method} request to {request.url} - Status Code: {response.status_code}")
    return response

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was uploaded in the request
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty part
        if file.filename == '':
            return 'No selected file'

        # Save the uploaded file to the 'uploads' directory
        file.save('uploads/' + file.filename)
        return 'File uploaded successfully'

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
