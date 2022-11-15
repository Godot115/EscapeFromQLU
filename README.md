# Escape From QLU

> 西郊有密林，助君出重围

## 服务器部署

以  Ubuntu 20.04 为例

### 服务器环境

- Python 3.x

### 安装依赖

- Chrome 浏览器

  ~~~bash
  # 下载安装包
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  #安装dpkg
  sudo apt-get install dpkg
  #安装xvfb
  sudo apt-get install xvfb
  #安装Chrome
  sudo dpkg -i google-chrome*.deb
  #如安装Chrome时报错，执行如下命令自动安装依赖
  sudo apt-get install -f
  ~~~

- Chrome Driver

  ~~~bash
  #安装unzip
  sudo apt-get install unzip
  #切换到用户路径
  cd ~
  #安装Chrome Driver
  wget -N https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
  #解压压缩包
  unzip chromedriver_linux64.zip
  #将驱动移动到软件路径
  sudo mv -f chromedriver /usr/local/share/chromedriver
  #建立软链接
  sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
  sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
  ~~~

### 下载脚本

~~~bash
#切换到用户路径
cd ~
wget https://github.com/Godot115/EscapeFromQLU/archive/refs/heads/main.zip
#解压缩
unzip main.zip
~~~

### 执行脚本

~~~Bash
#将信息替换为使用者信息
vim EscapeFromQLU-main/stu_info.py
#执行脚本
python3 EscapeFromQLU-main/main.py
~~~

### 使用crontab设置脚本每天自动执行

~~~bash
#编辑cron任务（第一次执行此任务时需选择默认编辑器）
crontab -e
#将如下文本写入文件末尾
0 0 * * * python3 EscapeFromQLU-main/main.py
#每天0点0时自动执行脚本。第一位为分钟，第二位为小时，建议自行修改时间以免出现高峰。
#服务器时区非东八区需要自行换算时间
~~~

### LICENSE
MIT LICENSE

