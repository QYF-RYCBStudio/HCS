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
    eg_res_ = []
    eg_res_name = ""
    eg_res_pwd = ""
    if eg_res != choice[0]:
        if eg_res == choice[2]:
            eg_res_ = util.multenterbox(user_type="管理员")
            if util.isAdmin(eg_res_[0]):
                eg_res_name = eg_res_[0]
                eg_res_pwd = eg_res_[1]
                print(eg_res_name, eg_res_pwd)
            else:
                eg.msgbox("输入的管理员账户名称不合法", "警告")
                exit(0xFFFFFF)
        elif eg_res == choice[1]:
            eg_res_ = util.multenterbox()
            if util.isAdmin(eg_res_[0]):
                eg_res_name = eg_res_[0]
                eg_res_pwd = eg_res_[1]
                print(eg_res_name, eg_res_pwd)
            else:
                eg.msgbox("输入的教师账户名称不合法", "警告")
                exit(0xFFFFFF)
        else:
            exit(0xFFFFFF)
    elif eg_res == choice[0]:
        pass
    else:
        exit(0xFFFFFF)
    if not util.isSimilar(".\\", "users.info", str(eg_res_)):
        eg.msgbox("账户已保存！", "提示")
        if not util.saveInfo(str(eg_res_)+"\n", ".\\", "users.info"):
            eg.msgbox("错误：保存用户信息失败，请重试！", "错误")
            return



if __name__ == "__main__":
    main()
