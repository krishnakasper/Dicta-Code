import socket

import speech_recognition as sr


class SpeechToText:
    r = sr.Recognizer()
    text = ""
    recordingtime = 1
    silenttime = 1
    energythreshold = 0
    listening = 0

    def __init__(self):
        print("In SpeechToText class")

    def listen(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            self.energythreshold = self.r.energy_threshold
            self.r.pause_threshold = self.silenttime
            print("Say Something")
            audio = self.r.listen(source)
            self.converter(audio)


    def changeRecording(self, value=1):
        self.recordingtime = value

    def changeSilentTime(self, value=1):
        self.silenttime = value

    def converter(self, audio):
        self.text = ""
        print("converter")
        if self.is_connected():
            try:
                self.text = self.r.recognize_google(audio)

            except sr.UnknownValueError:
                self.text = ""
        else:
            self.text = "noInternet"
        self.returnString()

    def is_connected(self):
        print("connected")
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def returnString(self):
        # print(self.text)
        return self.text

    def returnEnergyThreshold(self):
        print(self.energythreshold)
        return self.energythreshold
