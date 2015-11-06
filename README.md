# 为知笔记python-sdk

由于公司业务需要,需要从为知上同步数据过来,就做了这个功能还不全的sdk.(要做全也很简单,只不过现在这个已经满足我们需要了).

`开发/测试环境: ubuntu 12.04 python2.7.3`

## 安装

> sudo python setup.py install

> sudo pip install wiz

## 使用

### 创建client

 > client = Wiz('youremail', 'yourpassword')


### 列出所有笔记本

> notebooks = client.ls_notebooks()

### 列出某一笔记本上的所有笔记

> notebook.ls()

### 查看某一笔记html内容和text内容

> note.data.body

> note.data.text

### 查看某一笔记中的图片

> note.data.images

### 下载某一笔记上的第一张图片

> note.data.images[0].data # 返回图片二进制数据

### 查看某一笔记上带的附件

> note.data.attachments

### 下载某一笔记上的第一个附件

> note.data.attachments[0].data # 下载下来是附件本身的二进制数据,非web版上下载的zip


## 其他功能

还有删除笔记本,重命名笔记本.由于我只需要这些功能 就行了,其他的接口,比如对笔记本做增加,删除,修改. **如果您需要,告诉我,我可以给您加上去.**
