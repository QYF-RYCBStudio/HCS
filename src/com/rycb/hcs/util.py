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


def multenterbox(msgs="请输入{}账号与密码：（未注册的自动注册）", user_type="教师", title="信息", fields=["账号", "密码"], values=[]):
    msgs = msgs.format(user_type)
    ret = easygui.multpasswordbox(msgs, title, fields, values)
    return ret


def saveInfo(data, location, file, mode="a+", status=True):
    try:
        with open((location + file), mode) as f:
            f.write(data)
    except:
        status = False
    return status


def isSimilar(location, file, searchStr):
    try:
        with open((location + file), "r+") as f:
            res = f.read().split("\n")
        for i in res:
            if i.__eq__(searchStr):
                return True
            else:
                return False
    except:
        return False
