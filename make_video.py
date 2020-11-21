import ffmpeg
import config as c

def make_video():
    (
        ffmpeg
            .input('images/clean%05d.png',  framerate=c.fps)
            .output('test.mp4')
            .run()
    )
