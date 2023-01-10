from pytube import YouTube
import pytube
import ffmpeg
import moviepy.editor as mp
import torchaudio
#import pycountry
from speechbrain.pretrained import EncoderClassifier
import os


def downloadVideo(link):
    try:
        yt=YouTube(link)
    except pytube.exceptions.PytubeError:
        return None
    #if (yt):
    else:
        t = yt.streams.filter(file_extension = "mp4", only_audio=True).all()
        t[0].download(filename = "video.mp4")
        return yt.title
   # else:
        #return None

def convertToAudio(fileName):
    clip = mp.AudioFileClip("video.mp4")
    if  (clip.duration > 20):
         clip = clip.cutout(0, 20)

    clip.write_audiofile("audio.mp3")
    clip.close()
    return fileName

def recLang(fileName):
    language_id = EncoderClassifier.from_hparams(source="speechbrain/lang-id-voxlingua107-ecapa", savedir="tmp")

    signal = language_id.load_audio("audio.mp3")
    prediction =  language_id.classify_batch(signal)

    #print(prediction[3])
    name = str(prediction[3])[2:4]
    #ans = pycountry.countries.get(alpha_2=name)

    return name

