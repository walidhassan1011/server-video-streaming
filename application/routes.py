from application import app
from flask import render_template,request
@app.route('/')
def index():
    return render_template('index.html')
ALLOWED_EXTENSIONS = {'mp4', 'avi'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/upload', methods=['POST'])
def upload():
    
    if 'video' not in request.files:
        return 'No file part'
    video = request.files['video']
    print(video,"video")
    if video.filename == '':
        return 'No selected file'
    if video and allowed_file(video.filename):
        video.save(
            'static/' + video.filename
         )
        return render_template('preview.html', video_name=video.filename)
    return 'Upload failed'


