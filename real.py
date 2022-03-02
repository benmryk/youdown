from flask import Flask,render_template,send_file,url_for,redirect,request,session
from io import BytesIO
from pytube import YouTube


app = Flask(__name__)
app.config['SECRET_KEY'] = 'RTBKLJTVUYIFUUYuiftycdtrsdthfyvbweuigpcuUD^$%&^U&y8wq9y'

@app.route('/')
def home():
    session['url']= 'Enter url'
    return render_template('real.html',url_p = session['url'])

@app.route('/youdown',methods = ['POST','GET'])
def youdown():
    if request.method == 'POST':
        url = request.form ['url']
        session['url'] = url
        try:
            my_video  = YouTube(url)
            filename = my_video.title
            filename = str(filename) + ".mp4"
            my_video.check_availability()
            buffer = BytesIO()
            video = my_video.streams.get_by_itag(22)
            video.stream_to_buffer(buffer)
            buffer.seek(0)
            return send_file(buffer, as_attachment = True, download_name = filename )
        except:
            return render_template('real.html',url_p = 'Enter url',error = 'Invalid link')
    else:
        return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug = True)