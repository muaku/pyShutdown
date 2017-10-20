#!/usr/bin/ python
# -✳- coding: utf-8 -✳-
import json
import requests
import urllib
import os
import sys
import sqlite3
import subprocess
from fluent import sender
from fluent import event

# create json type text
#url = u'http://192.168.11.154:3000/latest'
#readObj = urllib.urlopen(url);
#response = readObj.read()
#print response
#data = json.loads(response)
#response = json.dumps(r.json(), sort_keys=True, indent=2)
#breath = data['breath']
#heart = data['heart']
#temps = data['temperature']

#print breath
#print heart
#print temps
#humanTemp = 0
#for temp in temps:
#  humanTemp += temp
#humanTemp = humanTemp/16

#text = u'今日の体温は%d度です．心拍数は%dで呼吸数は%dです．' %(humanTemp, heart, breath)
#print text

if __name__=='__main__':
  # get the user id from the JSON file
  args = sys.argv
  jsonFile = open(args[1], 'r')
  jsonData = json.load(jsonFile)
  # sys.stderr.write( ( str(json.dumps(jsonData, sort_keys = True, indent=4))) )
  text = u''
  microKey = 'forMerge.room.001.robo.001.microsensor.data'
  tempsKey = 'forMerge.room.001.robo.001.d6t44l06.data'
  faceKey = 'forMerge.room.001.robo.001.camera.registered.center'
  breath = -1
  heart = -1
  humanTemp = -1.0
  userid = 999
  
  # get the user info from the JSON file
  if faceKey in jsonData:
     userid = int(jsonData[faceKey]['userid'])
     joyEmo = int(jsonData[faceKey]['joyEmo'])
     # sys.stderr.write(str(userid))

  # get the additional user info from user.db
  # here, get the user's name
  con = sqlite3.connect("/root/Mimamori/hvc-p2-sample/code/user.db")
  con.row_factory = sqlite3.Row
  cur = con.cursor()
  cur.execute("select name from users where id = ?;", str(userid))
  count = 0
  username =  ''
  for row in cur:
    username = row['name']
    count = count + 1
  if count > 0:
    text = text + u'こんにちは%sさん.' %(username)
  else:
    text = text + u'はじめまして.'

  
  # get the vital data from the jsonFile
  if tempsKey in jsonData:
    if 'sensor_data' in jsonData[tempKey]:
      temps = jsonData[tempsKey]['sensor_data']
      humanTemp = float(0.0)
      count = 0
      for temp in temps:
        if temp > 31.0:
          humanTemp += float(temp)
          count += 1
      humanTemp = humanTemp/count
      text = text + u'体温は%d度です.' %(humanTemp)
      # sys.stderr.write(str(humanTemp))
  if microKey in jsonData:
    if 'breath' in jsonData[microKey]:
      breath = int(jsonData[microKey]['breath'])
    if 'heart' in jsonData[microKey]:
      heart = int(jsonData[microKey]['heart'])
      text = text + u'心拍数は%dで.呼吸数は%dです.' %(heart, breath)
      # sys.stderr.write(str(humanTemp))
      # sys.stderr.write(str(breath))
  
  # sys.stderr.write(text)
  # let the machine speak
  # commandText = u'/root/AquesTalkPi \"%s\" | aplay -Dhw:1,0' %(text)
  # subprocess.call(commandText, shell=True)
  commandText = u'echo %s >> /var/log/fluentd/speakText/text.txt' %(text)
  subprocess.call(commandText, shell=True)
  jsonFile.close
  sender.setup('speakText',host='localhost', port=24224)
  event.Event('vital', { 
                'breath': breath,
                'heart': heart,
                'temp': humanTemp,
                'text': text })
