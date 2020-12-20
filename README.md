<p align="center">
  <img src="enterprise.png" alt="USS Enterprise" />
</p>
<p align="center">
  <strong>:globe_with_meridians: Enterprise: Shields up! :globe_with_meridians:</strong></br>
  <em>Raspberry Pi software to control the speech recognition and lighting aboard the model USS Enterprise NCC-1701-A</em></br>
  <sub>Powered by <a href="https://pypi.org/project/SpeechRecognition/">SnowBoy</a> offline hotword recognition</sub>
</p>

<<<<<<< Updated upstream
=======
:globe_with_meridians: Enterprise: Shields up! :globe_with_meridians:

Powered by [SnowBoy](https://snowboy.kitt.ai/) offline hotword recognition
>>>>>>> Stashed changes

## Raspberry Pi Installation
Clone the repository folder, and run:

<<<<<<< Updated upstream
```bash
 sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev flac build-essential swig libpulse-dev python-pyaudio python3-pyaudio sox libatlas-base-dev
 
 pip3 install -r requirements.txt
```
=======
    sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev flac build-essential swig libpulse-dev python-pyaudio python3-pyaudio sox libatlas-base-dev
    pip3 install -r requirements.txt
    python3 enterprise.py
>>>>>>> Stashed changes

You may need to update your ~/.asoundrc file to help portaudio find your mic, as documented [here](http://docs.kitt.ai/snowboy/#running-on-pi)

## Hotword Models 🔥

SnowBoy hotword recognition works using pre-trained models. I have trained them on my voice, but consider recording yourself and downloading the models at the following links for more consistent results.

- [Enterprise: Shields up!](https://snowboy.kitt.ai/hotword/57534)
- [Enterprise: Yellow alert!](https://snowboy.kitt.ai/hotword/57535)
- [Enterprise: Red alert!](https://snowboy.kitt.ai/hotword/57536)
- [Enterprise: Fire phasers!](https://snowboy.kitt.ai/hotword/57537)
