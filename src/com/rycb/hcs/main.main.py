# Author RYCBStudio
# License MIT
# Create Time 2022/6/25 14:14
# Location HCS/main.main.py
# Use the PyCharm
# Encoding UTF-8
# Do not change the code without special needs


# Import sth
import easygui as eg
import util


def main():
    choice = ["学生模式", "教师模式", "管理员模式"]
    eg_res = eg.choicebox("请选择模式：", "提示", choice, 0)
    if eg_res != choice[0]:
        if eg_res == choice[1]:
            util.multenterbox()


if __name__ == "__main__":
    main()
