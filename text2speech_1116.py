# import os
# import sys
# import io
# import torch
# from collections import OrderedDict
#
# from TTS.models.tacotron import Tacotron
# from TTS.layers import *
# from TTS.utils.data import *
# from TTS.utils.audio import AudioProcessor
# from TTS.utils.generic_utils import load_config
# from TTS.utils.text import text_to_sequence
# from TTS.utils.synthesis import synthesis
# from utils.text.symbols import symbols, phonemes
# from TTS.utils.visual import visualize
#
# # export PYTHONPATH=/venv/Lib/site-packages
#
# # 设置常量
# MODEL_PATH = './tts_model/best_model.pth.tar'
# CONFIG_PATH = './tts_model/config.json'
# OUT_FILE = 'tts_out.wav'
# CONFIG = load_config(CONFIG_PATH)
# use_cuda = False
#
#
# def tts(model, text, CONFIG, use_cuda, ap, OUT_FILE):
#     waveform, alignment, spectrogram, mel_spectrogram, stop_tokens = synthesis(model, text, CONFIG, use_cuda, ap)
#     ap.save_wav(waveform, OUT_FILE)
#     return alignment, spectrogram, stop_tokens
#
#
# def load_model(MODEL_PATH, sentence, CONFIG, use_cuda, OUT_FILE):
#     # 加载模型
#     num_chars = len(phonemes) if CONFIG.use_phonemes else len(symbols)
#     model = Tacotron(num_chars, CONFIG.embedding_size, CONFIG.audio['num_freq'], CONFIG.audio['num_mels'], CONFIG.r,
#                      attn_windowing=False)
#
#     # 加载音频处理器
#     # CONFIG.audio["power"] = 1.3
#     CONFIG.audio["preemphasis"] = 0.97
#     ap = AudioProcessor(**CONFIG.audio)
#
#     # 加载模型状态
#     if use_cuda:
#         cp = torch.load(MODEL_PATH)
#     else:
#         cp = torch.load(MODEL_PATH, map_location=lambda storage, loc: storage)
#
#     # 加载模型
#     model.load_state_dict(cp['model'])
#     if use_cuda:
#         model.cuda()
#     model.eval()
#
#     model.eval()
#     model.decoder.max_decoder_steps = 1000
#     align, spec, stop_tokens = tts(model, sentence, CONFIG, use_cuda, ap, OUT_FILE)
#
#
# if __name__ == '__main__':
#     sentence = "Hello, how are you doing? My name is Sara"
#     load_model(MODEL_PATH, sentence, CONFIG, use_cuda, OUT_FILE)

# 好了我麻了 什么玩意儿
# Traceback (most recent call last):
#   File "D:/AI_project/rasa_1111/text2speech_1116.py", line 7, in <module>
#     from TTS.models.tacotron import Tacotron
# ModuleNotFoundError: No module named 'TTS.models'
# D:\AI_project\rasa_1111\\venv\\Lib\\site-packages
import zhtts

from playsound import playsound
text = "我是啵啵猫，今天咱俩来唠嗑"
tts = zhtts.TTS() # use fastspeech2 by default

tts.text2wav(text, "demo.wav")

playsound("demo.wav")
# >>> Save wav to demo.wav

# tts.frontend(text)
# >>> ('二零二零年，这是一个开源的端到端中文语音合成系统', 'sil ^ er4 #0 l ing2 #0 ^ er4 #0 l ing2 #0 n ian2 #0 #3 zh e4 #0 sh iii4 #0 ^ i2 #0 g e4 #0 k ai1 #0 ^ van2 #0 d e5 #0 d uan1 #0 d ao4 #0 d uan1 #0 zh ong1 #0 ^ uen2 #0 ^ v3 #0 ^ in1 #0 h e2 #0 ch eng2 #0 x i4 #0 t ong3 sil')

# tts.synthesis(text)

