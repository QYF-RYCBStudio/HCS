import datetime
import re
import easygui

dt = datetime.datetime.now()


def getNowTimeWithSecond():
    return dt.strftime("%H:%M:%S")


def getNowDate():
    return dt.strftime("%Y-%m-%d")


def isAdmin(ref):
    try:
        ret = str(ref)
    except:
        return False
    pattern = r"^[A|Admin|Administrator]\d{1,10}$"
    pattern = re.compile(pattern)
    if pattern.match(ret):
        return True
    else:
        return False


def isTeacher(ref):
    try:
        ret = str(ref)
    except:
        return False
    pattern = r"^[T|Teacher|t|teacher]\d{1,10}$"
    pattern = re.compile(pattern)
    if pattern.match(ret):
        return True
    else:
        return False


def multenterbox(msgs = "请输入教师账号与密码：", title = "信息", fields = ["账号", "密码"], values = []):
    ret = easygui.multenterbox(msgs, title, fields, values)
    return ret