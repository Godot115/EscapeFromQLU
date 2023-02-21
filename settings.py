# -*- coding: utf-8 -*-
# @Time    : 11/16/22 00:44
# @Author  : godot
# @FileName: settings.py
# @Project : escapeFromQLU
# @Software: PyCharm
import datetime
import random

stu_no = "111111111"  # 学号
os_password = "111111111"  # 一网通密码

mentor_name_Pinyin = "wangyinglong"  # 导师姓名拼音
mentor_rank = int("1")  # 请假页面中输入导师姓名拼音后，导师在搜索结果列表中的排名
communist_ideological_assistant_name_Pinyin = "abc"  # 导员姓名拼音
communist_ideological_assistant_rank = int("1")  # 请假页面中输入导员姓名拼音后，导员在搜索结果列表中的排名

health_status = "xx"  # 当前健康状况
family_contact = "xxx"  # 家庭联系人
family_contact_phone = "111"  # 家庭联系人电话
excuses = ["买东西", "去吃饭", "去看电影", "买生活用品", "购物", "去健身"]
target_locations = ["商业街", "恒大绿洲", "佳佳悦", "银座"]  # 目的地详细地址
stu_class = "xxx"  # 班级
campus_id = "1"  # 校区
# 1: "长清校区", 2: "千佛山校区", 3: "历城校区", 4:"彩石校区"
# random hour:min after 21:45 before 23:59
end_times = ["21:45", "21:56", "22:14", "22:23", "22:34", "22:45", "22:56", "23:14", "23:23", "23:34", "23:45", "23:56"]