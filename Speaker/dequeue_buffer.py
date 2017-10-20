# -✳- coding: utf-8 -✳-

import time
import os
import subprocess
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from time import sleep

# 監視したいフォルダへのパス
target_dir = '/var/log/fluentd/speakText/'
BUFFER_NAME = target_dir + 'text.txt'

def speakContent():
  with open(BUFFER_NAME, mode = 'r', encoding = 'utf-8') as file:
    lines = file.readlines()
    file.close()
    if len(lines) < 1:
      print("empty!")
      return # 発話するものが無いので早期return

    speakContent = lines[0].rstrip() # 発話対象は、1番目の行
    speakContent = speakContent.replace(" ", "")
    # subprocess.Popen(['/root/AquesTalkPi %s | aplay -Dhw:1,0 &> /dev/null &' % speakContent], stdout=subprocess.PIPE, shell=True)
    # ----- Start 2017/10/20 変更 (喋るスペースを開ける) ---
    splitSpeakContent = speakContent.split(".")
    for index in range(len(splitSpeakContent)-1):
        print(splitSpeakContent[index])
        subprocess.Popen(['/root/AquesTalkPi %s | sox -t wav -c1 - -t wav -c2 /dev/stdout | aplay -Dhw:2,0 &> /dev/null &' % splitSpeakContent[index]], stdout=subprocess.PIPE, shell=True)
        sleep(3)
    # --- End -----
       
  with open(BUFFER_NAME, mode = 'w', encoding = 'utf-8') as next_file:
    next_file.writelines(lines[1:])
    print("delete line")


def checkSpeaking():
  while True:
    jobsResults = res_cmd('ps | grep aplay').decode('utf-8')
    # print(type(jobsResults))
    # print(jobsResults)
    if jobsResults.find('aplay') > -1:
      time.sleep(2)
      continue
    else:
      speakContent()
      break



def res_cmd(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0]


class ChangeHandler(FileSystemEventHandler):
  def on_created(self, event):
    filepath = event.src_path
    filename = os.path.basename(filepath)
    print('%sができた' %filename)
  def on_modified(self, event):
    filepath = event.src_path
    filename = os.path.basename(filepath)
    print('%sを変更しました' % filename)
    #BUFFER_NAME = target_dir + '/' + filename
    checkSpeaking()

  def on_deleted(self, event):
    filepath = event.src_path
    filename = os.path.basename(filepath)
    print('%sを削除しました' % filename)
    print("kotti")


if __name__ == '__main__':
  checkSpeaking()
  while 1:
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, target_dir , recursive=True)
    observer.start()
    try:
      while True:
        time.sleep(0.1)
    except KeyboardInterrupt:
      observer.stop()
    observer.join()
