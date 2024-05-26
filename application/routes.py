from application import app
from flask import render_template,request,send_from_directory,send_file
import os
folderpath='put the path of the folder where the videos are stored in the static folder here'
@app.route('/')
def index():
    return render_template('index.html')
ALLOWED_EXTENSIONS = {'mp4', 'avi'}
def allowed_file(filename):
    savedFilename= '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    # save the filename to text file don't delete the past filenames uploaded
    if savedFilename:
        with open('videosName.txt', 'a') as f:
            f.write(filename + '\n')
    
    return savedFilename
@app.route('/upload', methods=['POST'])
def upload():
    print(request.files)
    if 'video' not in request.files:
        return 'No file part'
    video = request.files['video']
    print(type(video))
    if video.filename == '':
        return 'No selected file'
    if video and allowed_file(video.filename):
        video.save(
            'static/' + video.filename
         )
        return 'Upload successful'
    return 'Upload failed'


@app.route("/videosName")
def getVideoName():
    with open('videosName.txt', 'r') as f:
        # remove the last '\n' character from the string and return the string in a list
        return f.read().splitlines()


@app.route("/returnVideo/<videoName>", methods=['GET'], strict_slashes=False)
def returnVideo(videoName):
    print(videoName)
    # return the video file from static folder with the videoName requested by the user 
    return send_from_directory(folderpath, videoName)