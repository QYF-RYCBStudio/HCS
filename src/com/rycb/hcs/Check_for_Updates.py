# Author RYCBStudio
# License MIT
# Create Time 2022/4/3 13:55
# Location HCS-Python/Check_for_Updates.py
# Use the PyCharm
# Encoding UTF-8
# Do not change the code without special needs

import urllib.request as ur
from configparser import ConfigParser
import easygui as eg
import webbrowser as wb

cfps = ConfigParser()


def checkingUpdates(serverName=None):
    cfps.read("update\\version_check\\update.ucf")
    ur.urlretrieve("https://raw.githubusercontent.com/QYF-RYCBStudio/HCS/main/Update.ucf", "version")
    humanReadableVersion = cfps.get("Version", "version")
    machineReadableVersion = cfps.get("programSelfCheck", "version")
    with open("version", "r") as v:
        v = v.readline().strip()
        if humanReadableVersion == v or machineReadableVersion == v:
            eg.msgbox("Congratulations! Your program version is the latest version!\n恭喜！您的程序版本是最新版本！")
        else:
            cc = eg.choicebox("Oops! Your program version is not the latest version. You have two options:\n抱歉！您的程序版本不是最新版，您有两种选择：",
                              "qyf-rycbstudio.github.io", ["Download the latest version\t下载最新版本", "No, thanks\t不了，谢谢"])
            if cc == "Download the latest version\t下载最新版本":
                cc1 = eg.choicebox("You have two options:",
                                   "qyf-rycbstudio.github.io",
                                   ["Let the program download the latest version\t让程序下载最新版本", "Manual Download\t手动下载"])
                if cc1 == "Let the program download the latest version\t让程序下载最新版本":
                    pass
                else:
                    eg.msgbox("Please go to the website to download\n请前往网页下载")
                    wb.open("https://github.com/QYF-RYCBStudio/HCS/releases")
            else:
                pass

if __name__ == "__main__":
    checkingUpdates()
