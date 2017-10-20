from time import sleep
text = "こんにちはムアクさん.心拍は50で.呼吸は70です."

textSplited = text.split(".")

print(textSplited)

# for txt in textSplited:
#     print(txt)
#     sleep(3)

for index in range(len(textSplited)-1):
    print(textSplited[index])
    sleep(3)