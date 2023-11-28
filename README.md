# 🍀️——>🌲四叶草输入法个人配置方案
> From Clover to Cypress

![IMAGE](images/IMAGE.png)

## 说明

在🍀️四叶草拼音输入方案的基础上进行定制:

- 增加了英语的输入;

- 增加emoji_catagory中的简体中文对应的符号；

- 增加了一些其他输入法词库；

- 皮肤默认为mac绿色，可以在输入法设定里面选择其他的皮肤；

- 删除了其他输入法，有需要可以自己在加进去；

- 添加修改后的【雾凇拼音】词库tencent.dict.yaml文件（[腾讯词向量百万词库](https://ai.tencent.com/ailab/nlp/zh/download.html)）作为tencent_nlp_pinyin.yaml文件；

- 添加一个python脚本，给nlp词库添加拼音，权重全部设为1；

- 注意：可以拼音首字母快速输入词组；

### update

 默认添加【云飞wainshine】的【公司名称】语料库制作的词库。对于【云飞wainshine】其他的语料库，需要的时候，使用【拼音标注.py】自行制作词库，并添加到库引用中。**不同的行业可以选择性安装部署以下词库，没必要全部加入进去，否则重新部署时会占时间**

包括：

- [Chinese-Names-Corpus ](https://github.com/wainshine/Chinese-Names-Corpus)
-  [Company-Names-Corpus ](https://github.com/wainshine/Company-Names-Corpus)
- [Medical-Names-Corpus ](https://github.com/wainshine/Medical-Names-Corpus)
-  [Book-Names-Corpus ](https://github.com/wainshine/Book-Names-Corpus)
- [Species-Names-Corpus ](https://github.com/wainshine/Species-Names-Corpus)
-  [Food-Names-Corpus ](https://github.com/wainshine/Food-Names-Corpus)

---
## 感谢以下项目
- [四叶草输入法](https://github.com/fkxxyz/rime-cloverpinyin)

- [中文NLP资源库](https://github.com/fighting41love/funNLP#%E8%AF%AD%E6%96%99%E5%BA%93)  里面有各种语料库，可以把这些语料库添加上拼音加入词库里面

- [Rime 鼠须管输入法皮肤效果展示](https://github.com/NavisLab/rime-pifu)

- [小狼毫P站配色主题分享](https://tieba.baidu.com/p/6870494952)

- [小狼毫晒皮肤……](https://tieba.baidu.com/p/5849361297)

- [云飞wainshine词库](https://github.com/wainshine)

  

  ### 其他皮肤链接
  找了其他好看的皮肤，直接替换即可
  - [Rime 鼠须管 皮肤配置详解](https://blog.51cto.com/kylebing/5430702)
  - [微信键盘配色鼠须管皮肤](https://www.v2ex.com/t/930853)

  **这个项目加入了lua脚本，功能更强大**
  [rime-ice](https://github.com/iDvel/rime-ice)

  **这是扩展RIME脚本的链接**
  [Extending RIME with Lua scripts](https://github.com/hchunhui/librime-lua)
---
  ## 用法
### 安装部署

  以windows系统为例：

1. 在任务栏中rime输入法图标上右键，点击【用户文件夹】，将全部文件备份到其他文件夹下，清空setting文件夹；

2. 再次，点击【程序文件夹】；

3. 打开任务管理器，找到【小狼毫算法服务】，右键【结束任务】；

4. 下载【setting】压缩文件，解压到【用户文件夹】中（setting文件夹）；

5. 到【程序文件夹】中，依次点击“WeaselServer.exe", "WeaselSetup.exe", "WeaselDeployer.exe";
6. 在任务栏中rime输入法图标上右键，点击【重新部署】

### 定制添加【云飞wainshine】词库

1. 使用【拼音标注.py】，生成的文件改为【.dict.yaml】后缀命名。

2. 将文件拷贝到【setting】文件夹下，修改clover.dict.yaml文件，添加文件名。
