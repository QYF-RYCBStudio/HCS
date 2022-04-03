# Author RYCBStudio
# License MIT & GNU GPLv3
# Create Time 2022/2/1 20:18
# Location HCS-Python/Main.py
# Use the PyCharm
# Encoding UTF-8
# Do not change the code without special needs

import configparser
import time as t
import datetime as dt

import easygui as eg
from tqdm import tqdm

cfpr = configparser.ConfigParser()
Dt = dt.datetime.now()


class Main:
    def __str__(self):
        main.log("Loading resources...", "INFO", "Client")
        t.sleep(0.5)
        main.log("Start to load resources...", "INFO", "Client")
        with tqdm(total=500) as p_bar:
            for i in range(500):
                t.sleep(0.01)
                p_bar.update(1)
                p_bar.set_description("Loading resources")

    @staticmethod  # 静态方法声明
    def progress_bar_error():
        main.log("The progress bar module has been evoked.", "INFO", "Client")
        t.sleep(0.5)
        with tqdm(total=100) as p_bar:
            main.log("The progress bar has been evoked.", "INFO", "Client")
            for i in range(99):
                t.sleep(0.01)
                p_bar.update(1)
                p_bar.set_description("Try")
            t.sleep(0.5)
            print("\nError: trying to reload...")
            t.sleep(0.5)
            for j in range(51):
                print("Reloading: {}%".format(j*2))
                main.log("Error: Failed to loading resources, repairing: {}%".format(j*2), "ERROR", "Client")
                t.sleep(0.025)
            t.sleep(0.5)
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

    @staticmethod
    def log(data, type, port, fmt=None):
        with open("./logs/Runtime_" + Dt.strftime("%Y-%m-%d") + "_Log.log", "a+") as file:
            if data is not None:
                if type is not None and port is not None:
                    if fmt == "A" or fmt == "a" or fmt == 0 or fmt is None:
                        file.write("[" + Dt.strftime("%Y-%m-%d %H:%M:%S") + "] [{}/{}] ".format(port, type) + str(data) + "\n")
                    elif fmt == "LA" or fmt == "la" or fmt == "L" or fmt == "l" or fmt == 1:
                        file.write("[" + Dt.strftime("%Y-%m-%d %H:%M") + "] [{}/{}] ".format(port, type) + str(data) + "\n")
                    elif fmt == "S" or fmt == "s" or fmt == 2:  # Not commonly used
                        file.write("[" + Dt.strftime("%Y-%m-%d") + "] [{}/{}] ".format(port, type) + str(data) + "\n")
                    else:
                        file.write("[{}/{}][".format(port, type) + "] " + str(data) + "\n")
                else:
                    if fmt == "A" or fmt == "a" or fmt == 0:
                        file.write("[" + Dt.strftime("%Y-%m-%d %H:%M:%S") + "] " + str(data) + "\n")
                    elif fmt == "LA" or fmt == "la" or fmt == "L" or fmt == "l" or fmt == 1:
                        file.write("[" + Dt.strftime("%Y-%m-%d %H:%M") + "] " + str(data) + "\n")
                    elif fmt == "S" or fmt == "s" or fmt == 2:
                        file.write("[" + Dt.strftime("%Y-%m-%d") + "] " + str(data) + "\n")
                    else:
                        file.write(str(data) + "\n")

    @staticmethod
    def startUp():
        main.log("Loading resources...", "INFO", "Client")
        print("Program is loading resources...")
        main.log("Evoke progress bar module", "INFO", "Client")
        main.progress_bar_error()

    @staticmethod
    def main():
        pass


if __name__ == "__main__":
    with open("./logs/Runtime_" + Dt.strftime("%Y-%m-%d") + "_Log.log", "w") as file:
        file.write("")
    Main().log("Program entry found.", "INFO", "Client")
    main = Main()
    main.log("The Main class loading: successful.", "INFO", "Client")
    eg.msgbox("若出现穿模、加载不全等问题，请停止程序后重启！\n\n若出現穿模、加載不全等問題，請停止程式後重啓！", "提示")
    main.log("ShowTipBox showed: type number:001, state: successful.", "INFO", "Client")
    eg.msgbox("英语外其他语言可能有汉化不全等问题，请忽视或报告！\n\n英語外其他語言可能有漢化不全等問題，請忽視或報告！", "提示")
    main.log("ShowTipBox showed: type number:002, state: successful.", "INFO", "Client")
    eg.codebox("（第一行）反馈&报告网址；（第二、三行）反馈&报告邮箱", "提示", "https://github.com/QYF-RYCBStudio/HCS/issues/new/choose"
                                                    "\nRYCBStudio@163.com\nRYCB_Feedback@163.com")
    main.log("ShowIssueFeedbackBox showed: type number:003, state: successful.", "INFO", "Client")
    _return0 = None
    main.log("Set variable: name: _return0, var number: 001, state: successful.", "INFO", "Client")
    choices = ["简体中文", "繁體中文", "English"]
    return0 = eg.choicebox("Choose your program language: (选择你的语言)", "rycbstudio.github.io", choices)
    main.log("ShowChoiceBox showed: type number:004, state: successful.", "INFO", "Client")
    if return0 == "简体中文":
        _return0 = "zh-CN"
        main.log("Reassignment variable: name: _return0, Reassignment content: [string]'zh-CN', var number: 001, "
                 "state: successful.", "INFO", "Client")
    elif return0 == "繁體中文":
        _return0 = "zh-TW&zh-HK"
        main.log("Reassignment variable: name: _return0, Reassignment content: [string]'zh-TW&zh-HK', var number: 001, "
                 "state: successful.", "INFO", "Client")
    elif return0 == "English":
        _return0 = "en-US"
        main.log("Reassignment variable: name: _return0, Reassignment content: [string]'en-US', var number: 001, "
                 "state: successful.", "INFO", "Client")
    else:
        eg.msgbox("您已撤销操作！")
        main.log("Warning: User has exited the program. return value: 0x5181. state: successful.", "WARN", "Client")
        exit(0x5181)

    main.log("Prepare to loading resources. progress: 0%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 10%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 25%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 30%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 45%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 60%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 75%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 95%", "INFO", "Client")
    t.sleep(0.25)
    main.log("Prepare to loading resources. progress: 100%", "INFO", "Client")
    main.log("Prepare to loading resources. state: successful.", "INFO", "Client")
    try:
        main.loading_resources("./lang", "{}.lang".format(_return0), "./license", "GPLv3.lcs", "./license", "MIT.lcs")
    except Exception as e:
        main.log("Error: Some problems have been captured in some places. Please check:" + str(e), "ERROR", "Client")
        eg.msgbox("Error: Some problems have been captured in some places. Please check:" + str(e))
    if _return0 == "zh-CN":
        main.log("Has entered the simplified Chinese environment.", "INFO", "Client")
        print("语言包已成功加载。", end="\n")
        main.log("Language pack loaded successfully.", "INFO", "Client")
        print("初始化中...", end="\n")
        main.log("Initializing...", "INFO", "Client")
        try:
            main.log("Starting up...", "INFO", "Client")
            main.startUp()
            main.log("Start up successfully.", "INFO", "Client")
            print("程序初始化成功。", end="\n")
        except Exception as e:
            main.log("Warn: The program failed to load, please restart!", "WARN", "Client")
            main.log("Show warning box: at"+Dt.strftime("%Y-%m-%d %H:%M:%S"),"INFO", "Client")
            eg.msgbox("⚠警告⚠: 程序未能成功加载，请重启！")
    elif _return0 == "zh-TW&zh-HK":
        print("語言包已成功加載。", end="\n")
        print("初始化中...", end="\n")
        try:
            main.log("Starting up...", "INFO", "Client")
            main.startUp()
            main.log("Start up successfully.", "INFO", "Client")
            print("程式初始化成功。", end="\n")
        except:
            main.log("Warn: The program failed to load, please restart!", "WARN", "Client")
            main.log("Show warning box: at" + Dt.strftime("%Y-%m-%d %H:%M:%S"), "INFO", "Client")
            eg.msgbox("⚠警告⚠: 程式未能成功加載，請重啓！")
    else:
        print("Language pack has benn loaded successfully.", end="\n")
        print("Initializing...")
        try:
            main.startUp()
            print("Program initialization succeeded.", end="\n")
        except:
            main.log("Warn: The program failed to load, please restart!", "WARN", "Client")
            main.log("Show warning box: at" + Dt.strftime("%Y-%m-%d %H:%M:%S"), "INFO", "Client")
            eg.msgbox("⚠WARNING⚠: The program failed to load successfully, please restart!")
