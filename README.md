# USS Enterprise Computer
Raspberry Pi software to control the speech recognition and lighting aboard the model USS Enterprise NCC-1701-A

:globe_with_meridians: Enterprise: Shields up! :globe_with_meridians:

Powered by [SnowBoy](https://pypi.org/project/SpeechRecognition/) offline hotword recognition

## Raspberry Pi Installation
Within the cloned repository folder, run the following commands:

    sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev flac build-essential swig libpulse-dev python-pyaudio python3-pyaudio sox libatlas-base-dev
    pip3 install -r requirements.txt


## Hotword Models

SnowBoy hotword recognition works using pre-trained models. I have trained them on my voice, but please consider recording yourself and downloading the models at the following links for more accurate results.

- [Enterprise: Shields up!](https://snowboy.kitt.ai/hotword/57534)
- [Enterprise: Yellow alert!](https://snowboy.kitt.ai/hotword/57535)
- [Enterprise: Red alert!](https://snowboy.kitt.ai/hotword/57536)
- [Enterprise: Fire phasers!](https://snowboy.kitt.ai/hotword/57537)

