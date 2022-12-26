# print("欢迎来到黑马游乐园")
# if int(input("请输入你的身高：")) > 120:
#     print("您的身高大于120不可以免费")
#     if int(input("请输入您的vip等级")) < 3:
#         print("您的vip等级小于3不可以免费")
#     else:
#         print("恭喜你，您的vip级别大于等于3，可以免费游玩")
# else:
#     print("欢迎你小朋友")

age = int(input("请输入您的年龄"))
if 18 <= age <= 30:
    if int(input("请输入入职年龄")) > 2:
        print("恭喜你满足条件")
    elif int(input("请输入您的级别")) > 3:
        print("恭喜你满足条件")
else:
    print("您不满足条件")