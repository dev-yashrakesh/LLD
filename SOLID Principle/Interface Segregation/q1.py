# class MediaDevice:
#
#     def play_audio(self):
#         pass
#
#     def play_video(self):
#         pass
#
#     def record_video(self):
#         pass
#
#     def take_photo(self):
#         pass
#
# class Smartphone(MediaDevice):
#
#     def play_audio(self):
#         return "Playing audio"
#
#     def play_video(self):
#         return "Playing video"
#
#     def record_video(self):
#         return "Recording video"
#
#     def take_photo(self):
#         return "Taking photo"
#
# class MP3Player(MediaDevice):
#
#     def play_audio(self):
#         return "Playing audio"
#
#     def play_video(self):
#         raise Exception("Not supported")
#
#     def record_video(self):
#         raise Exception("Not supported")
#
#     def take_photo(self):
#         raise Exception("Not supported")

class VideoPlayable:
    def play_video(self):
        pass



class VideoRecorder:
    def record_video(self):
        pass

class PictureCapture:
    def take_photo(self):
        pass

class AudioPlayable:
    def play_audio(self):
        pass

class AudioPause:
    def pause_audio(self):
        pass

class Smartphone(VideoPlayable, AudioPlayable, VideoRecorder, AudioPause, PictureCapture):

    def play_audio(self):
        return "Playing audio"

    def play_video(self):
        return "Playing video"

    def record_video(self):
        return "Recording video"

    def take_photo(self):
        return "Taking photo"

class MP3Player(AudioPlayable,AudioPause):

    def play_audio(self):
        return "Playing audio"

    def pause_audio(self):
        return "Pausing audio"