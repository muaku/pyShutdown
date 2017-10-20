#!/usr/bin/env python
# -✳- coding: utf-8 -✳-

import subprocess
import os
import sys
from time import sleep

if __name__=='__main__':
    for i in range(0,3):
        commandText = u'/root/AquesTalkPi \"こんにちははるこおばあさん.今日の笑顔はいいですね.何か良いことありましたか.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText, shell=True)
        sleep(3)
        commandText1 = u'/root/AquesTalkPi \"でも今朝は少しお熱があるみたい.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText1, shell=True)
        sleep(2)
        commandText2 = u'/root/AquesTalkPi \"お熱を計ってもらいましょう.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText2, shell=True)
        sleep(3)
        commandText3 = u'/root/AquesTalkPi \"今日の心拍は64です.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText3, shell=True)
        sleep(2)
        commandText4 = u'/root/AquesTalkPi \"呼吸は14です.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText4, shell=True)
        sleep(3)
        commandText5 = u'/root/AquesTalkPi \"体の調子は良いですね.\" | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0'
        subprocess.call(commandText5, shell=True)
        sleep(10)