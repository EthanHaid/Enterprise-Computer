<p align="center">
  <img src="enterprise.png" alt="USS Enterprise" />
</p>
<p align="center">
  <strong>:globe_with_meridians: Enterprise: Shields up! :globe_with_meridians:</strong></br>
  <em>Raspberry Pi software to control the speech recognition and lighting aboard the model USS Enterprise NCC-1701-A</em></br>
  <sub>Powered by <a href="https://snowboy.kitt.ai/", target="_blank">SnowBoy</a> offline hotword recognition</sub>
</p>


## Raspberry Pi Installation
Clone the repository folder, and run:

```bash
sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev flac build-essential swig libpulse-dev python-pyaudio python3-pyaudio sox libatlas-base-dev
pip2 install -r requirements.txt
python2 enterprise.py
```

You may need to update your ~/.asoundrc file to help portaudio find your mic, as documented [here](http://docs.kitt.ai/snowboy/#running-on-pi)

## Hotword Models 🔥

SnowBoy hotword recognition works using pre-trained models. I have trained them on my voice, but consider recording yourself and downloading the models at the following links for more consistent results.

- <a href="https://snowboy.kitt.ai/hotword/57534", target="_blank">Enterprise: Shields up!</a>
- <a href="https://snowboy.kitt.ai/hotword/57535", target="_blank">Enterprise: Yellow alert!</a>
- <a href="https://snowboy.kitt.ai/hotword/57536", target="_blank">Enterprise: Red alert!</a>
- <a href="https://snowboy.kitt.ai/hotword/57739", target="_blank">Enterprise: Stand Down!</a>
- <a href="https://snowboy.kitt.ai/hotword/57537", target="_blank">Enterprise: Fire phasers!</a>
- <a href="https://snowboy.kitt.ai/hotword/57740", target="_blank">Enterprise: Power Off!</a>
- <a href="https://snowboy.kitt.ai/hotword/57741", target="_blank">Enterprise: Power On!</a>
