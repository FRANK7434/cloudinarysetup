from flask import Flask,Response,request
import cloudinary
from dotenv import load_dotenv
import os
import cloudinary.uploader
# from flask_ import Resource,Api


app= Flask(__name__)
# api=Api(app=app)

load_dotenv()
# cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv("cloudinary_cloud_name"),
    api_key=os.getenv("cloudinary_api_key"),
    api_secret=os.getenv("cloudinary_api_secret")
)

@app.route("/upload",methods=["POST"])
def upload_image():
    url_arr=[]
    data=request.files.getlist("file")
    for file in data:
        # Upload the image to cloudinary and get the URL
        result=cloudinary.uploader.upload(file)
        url_arr.append(result.get('url'))
    print(url_arr)
    return Response(status=200, response=url_arr)

@app.route("/")
def home():
    return Response(status=200, response=["Success"])

if __name__ == '__main__':
    app.run(port=5555,debug=True)