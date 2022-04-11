# Author RYCBStudio
# License MIT
# Create Time 2022/4/3 13:55
# Location HCS-Python/Check_for_Updates.py
# Use the PyCharm
# Encoding UTF-8
# Do not change the code without special needs
import os
import urllib.request as ur
from configparser import ConfigParser

cfps = ConfigParser()


def checkingUpdates(serverName=None):
    cfps.read("update\\version_check\\update.ucf")
    ur.urlretrieve("https://raw.githubusercontent.com/QYF-RYCBStudio/HCS/main/Update.ucf", "version")


if __name__ == "__main__":
    checkingUpdates()
