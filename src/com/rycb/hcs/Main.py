# Author RYCBStudio
# License MIT & GNU GPLv3
# Create Time 2022/2/1 20:18
# Location HCS-Python/Main.py
# Use the PyCharm
# Encoding UTF-8
# Do not change the code without special needs

import configparser
import time as t

import easygui as eg
from tqdm import tqdm

cfpr = configparser.ConfigParser()


class Main:
    def __init__(self):
        pass

    def __str__(self):
        with tqdm(total=500) as p_bar:
            for i in range(500):
                t.sleep(0.01)
                p_bar.update(1)
                p_bar.set_description("Loading resources")

    @staticmethod  # 静态方法声明
    def progress_bar_error():
        with tqdm(total=100) as p_bar:
            for i in range(99):
                t.sleep(0.01)
                p_bar.update(1)
                p_bar.set_description("Try")
            print("Error: trying to reload...")
        main.__str__()
        main.progress_bar()

    @staticmethod
    def progress_bar():
        with tqdm(total=100) as p_bar:
            for i in range(50):
                t.sleep(0.01)
                p_bar.update(2)
                p_bar.set_description("Try")

    @staticmethod
    def loading_resources(langLocation, langFileName, license1Location, license1FileName, license2Location,
                          license2FileName):
        cfpr.read(langLocation + "\\" + langFileName, encoding='utf-8')
        with open(license1Location + "\\" + license1FileName) as l1:
            global lcs1
            lcs1 = l1.read()
        with open(license2Location + "\\" + license2FileName) as l2:
            global lcs2
            lcs2 = l2.read()


if __name__ == "__main__":
    main = Main()
    eg.msgbox("若出现穿模、加载不全等问题，请停止程序后重启！", "提示")
    eg.msgbox("英语外其他语言可能有汉化不全等问题，请忽视或报告！", "提示")
    eg.codebox("（第一行）反馈&报告网址；（第二、三行）反馈&报告邮箱", "提示", '''
    
    ''')
    _return0 = None
    choices = ["简体中文", "繁體中文", "English"]
    return0 = eg.choicebox("Choose your program language: (选择你的语言)", "rycbstudio.github.io", choices)
    if return0 == "简体中文":
        _return0 = "zh-CN"
    elif return0 == "繁體中文":
        _return0 = "zh-TW&zh-HK"
    elif return0 == "English":
        _return0 = "en-US"
    else:
        eg.msgbox("您已撤销操作！")
        exit(0x5181)
    def startUp():
        print("Program is loading resources...")
        main.__str__()
    main.loading_resources("./lang", "{}.lang".format(_return0), "./license", "GPLv3.lcs", "./license", "MIT.lcs")
    if _return0 == "zh-CN":
        print("资源已成功加载。", end="\n")
        print("初始化中...", end="\n")
        try:
            startUp()
            print("程序初始化成功。", end="\n")
        except:
            eg.msgbox("")
    elif _return0 == "zh-TW&zh-HK":
        print("資源已成功加載。", end="\n")
        print("初始化中...", end="\n")
        try:
            startUp()
            print("程式初始化成功。", end="\n")
        except:
            eg.msgbox("⚠警告⚠： ")
    else:
        print("Resources has beed loaded successfully", end="\n")
        print("Initializing...")
        try:
            startUp()
            print("Program initialization succeeded.", end="\n")
        except:
            eg.msgbox("")
    main.progress_bar_error()
