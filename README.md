# 该项目完成了西北大学晨午检基于程序的填报任务，可以依此程序来定时填报小程序(需要配合定时执行命令，比如crontab)
将程序调用添加到系统定时运行的功能，Linux中具体是crontab命令，Windows请自行探索，请将定时任务时间调整到6:30与12：30，以完成自动填报

## 注意:
  该项目已经不再维护, 因为你可能对该项目的另外一个[版本](https://github.com/san-qi/NWU_web_dailyup)感兴趣

## 第三方库需求：
  1. bs4
  2. requests
  3. pycryptodome

## 项目构成：
  1. main.py:      程序主体
  2. aes_crypt.py: 用于用户登录过程中对密码的加密，保证登录的成功
  3. data.json:    保存要提交的个人信息,以及一些额外信息(注意，该文件中的地址仅适用于西北大学长安校区的用户，或通过修改该文件中的相应msg项来生效,其他人慎用)

## 使用方式:
  1. 安装依赖, pip install -r requirements.txt
  2. 如果是西北大学长安校区的用户，则不需要管data.json的msg项
  3. 将data.json中的user项添加上自己的学号与密码，注意要按照json文件格式
  4. 最后使用crontab命令实现每日定时调用。调用形式为 py main.py dir, 其中dir为该项目的所在位置。
