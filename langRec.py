from pytube import YouTube
import pytube
import ffmpeg
import moviepy.editor as mp
import torchaudio
#import pycountry
from speechbrain.pretrained import EncoderClassifier



def downloadVideo(link):
    try:
        yt=YouTube(link)
    except pytube.exceptions.PytubeError:
        return None
    #if (yt):
    else:
        #t = yt.get('mp4')
        t = yt.streams.filter(only_audio=True).all()
        t[0].download()
        return yt.title
   # else:
        #return None

def convertToAudio(fileName):
    clip = mp.AudioFileClip(fileName+".mp4")
    clip.write_audiofile(fileName+".mp3")
    clip.close()
    return fileName

def recLang(fileName):
    import torchaudio
    from speechbrain.pretrained import EncoderClassifier
    language_id = EncoderClassifier.from_hparams(source="speechbrain/lang-id-voxlingua107-ecapa", savedir="tmp")

    signal = language_id.load_audio(fileName+".mp3")
    prediction =  language_id.classify_batch(signal)

    #print(prediction[3])
    name = str(prediction[3])[2:4]
    #ans = pycountry.countries.get(alpha_2=name)

    return name

