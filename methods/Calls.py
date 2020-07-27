import ffmpeg


def encode_ffmpeg(source: str = "input.mp3", dest: str = "input.raw") -> None:
    audio = ffmpeg.input(source)
    audio.output(dest, ac=1, ar=480000, acodec="pcm_s16le", f="s16le").run()


def decode_ffmpeg(source: str = "output.mp3", dest: str = "output.raw") -> None:
    audio = ffmpeg.input(source, ac=1, ar=480000, acodec="pcm_s16le", f="s16le")
    audio.output(dest).run()
