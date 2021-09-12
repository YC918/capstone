#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pyautogui as py 
import pandas as pd
import time
from threading import Thread


# In[2]:


from pynput import keyboard


# In[ ]:


browser = webdriver.Chrome(executable_path=r'/Users/Yew Choong/Downloads/chromedriver_win32/chromedriver')
browser.maximize_window()
browser.get("https://popcat.click/")
time.sleep(3)


# In[ ]:


def exit_program():
    def on_press(key):
        if str(key) == 'Key.esc':
            main.status = 'pause'
            user_input = input('Program paused, would you like to continue? (y/n) ')

            while user_input != 'y' and user_input != 'n':
                user_input = input('Incorrect input, try either "y" or "n" ')

            if user_input == 'y':
                main.status = 'run'
            elif user_input == 'n':
                main.status = 'exit'
                exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# In[ ]:


def main():
    main.status = 'run'

    while True:
        py.click(x=705,y=400,interval=0.005)

        while main.status == 'pause':
            time.sleep(1)

        if main.status == 'exit':
            print('Main program closing')
            break


# In[ ]:


Thread(target=main).start()
Thread(target=exit_program).start()

