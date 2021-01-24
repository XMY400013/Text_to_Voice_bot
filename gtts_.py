from gtts import gTTS
from io import BytesIO


def speech_(text):
    # write voice bytes to BytesIO
    with BytesIO() as byte:
        gTTS(text=text, lang='en').write_to_fp(byte)
        byte.seek(0)
        return byte.read()
