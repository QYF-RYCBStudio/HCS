@rem 点击即可安装

@echo off
chcp 65001
cls
title 安装程序必需模块
echo 请确认您是否已安装Python!
echo 使用Python pip安装
title 安装tqdm
echo 安装tqdm
pip install tqdm
title 模块tqdm安装成功!
echo 模块tqdm安装成功!（不保证一定成功）
title 安装easygui
echo 安装easygui
pip install easygui
title 模块easygui安装成功!
echo 模块easygui安装成功!（不保证一定成功）
title 安装ConfigParser
echo 安装ConfigParser
pip install configparser
title 模块ConfigParser安装成功!
echo 模块ConfigParser安装成功!（不保证一定成功）
echo 安装已完成
pause>nul