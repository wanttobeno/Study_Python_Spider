

#### 简书交友帖子图片下载

例子百度到的，来自
https://www.jianshu.com/p/7ba9c90ff12d
稍微修改了下。添加重复下载判断，添加路径字符串去除非法字符串。


#### 说明
下载的图片保存在row_img文件夹下

注释掉了print，在window下某些字符串打印会报错'gbk' codec can't encode character XXXX。

#### 颜值打分

首先，进入百度人脸识别官网（http://ai.baidu.com/tech/face），点击立即使用，登陆百度账号（没有就注册一个）

创建应用，完成后，点击管理应用，就能看到AppID等，这些在调用API时需要使用的。