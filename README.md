
> **注意**:  本人博客已更改域名至 http://andrewliu.in , 所有博客文章都已经迁移至新域名, 抱歉.

# Overview

**The Tutorial ** which guild how to develop a Blog by Django, It will update with learing.

# Requirements

- Mac OS X 10.10.1  #非必要
- Python3.4.2
- Django1.7.1 
- Bootstrap3.3.0 or Pure  #非必要
- Sublime Text 3  #非必要
- virtualenv  1.11.6


# Install 

```
$ git clone https://github.com/Andrew-liu/my_blog_tutorial

or

$ git clone git@github.com:Andrew-liu/my_blog_tutorial.git
```

# Usage

You can use the example of blog simply, just to do below:

```
$ cd my_blog_tutorial
$ pip install -r requirements.txt  #安装所有依赖
$ python manage.py migrate
$ python manage.py runserver

open the website(chrome best) and input
http://127.0.0.1:8000/

关于在windows环境下依赖项的安装注意项：
1.windows环境下，psycopg2需要安装对应的windows版本
    http://pythonhosted.org//psycopg2/install.html#install-from-a-package
2.django-toolbelt依赖于psycopg和其它的几个包，注意安装顺序
    https://pypi.python.org/pypi/django-toolbelt/0.0.1
```



# More Detail

整个博客开发过程, 已经整理成书, 欢迎阅读

- Gitbook开源图书[Django搭建简易博客教程](http://andrew-liu.gitbooks.io/django-blog/content/)

- 极客学院wiki[Django搭建博客简易教程](http://wiki.jikexueyuan.com/project/django-set-up-blog/)

# Done

1. Django-bootstrap-admin优化后台管理, Pure只做前端
2. markdown和代码高亮
3. 多说评论
4. aboutme功能建设完成
5. 分类
6. 标签（需要完善）
6. 归档
7. 搜索
8. read more功能
9. RSS功能
10. 分页功能

# TO DO

如果您觉得我的文章对您有帮助欢迎微信扫码捐助.

![捐赠](http://7rfjyu.com1.z0.glb.clouddn.com/Snip20150611_11.png)

# License

Copyright (c) 2014 [Andrew Liu](http://andrewliu.in)

Licensed under the MIT License

