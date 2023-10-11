# 🍀️——>🌲customize-rime-cloverpinyinyin
![IMAGE](images/IMAGE.png)

在🍀️四叶草拼音输入方案的基础上进行定制:
- 增加了英语的输入;
- 增加emoji_catagory中的简体中文对应的符号；
- 增加了一些其他输入法词库；
- 皮肤默认为mac绿色，可以在输入法设定里面选择其他的皮肤；
- 删除了其他输入法，有需要可以自己在加进去；
- 添加修改后的【雾凇拼音】词库tencent.dict.yaml文件（[腾讯词向量百万词库](https://ai.tencent.com/ailab/nlp/zh/download.html)）作为tencent_nlp_pinyin.yaml文件；
- 添加一个python脚本，给nlp词库添加拼音，权重全部设为1
---
## 感谢以下项目
- [四叶草输入法](https://github.com/fkxxyz/rime-cloverpinyin)
- [中文NLP资源库](https://github.com/fighting41love/funNLP#%E8%AF%AD%E6%96%99%E5%BA%93)  里面有各种语料库，可以把这些语料库添加上拼音加入词库里面
- [Rime 鼠须管输入法皮肤效果展示](https://github.com/NavisLab/rime-pifu)
- [小狼毫P站配色主题分享](https://tieba.baidu.com/p/6870494952)
- [小狼毫晒皮肤……](https://tieba.baidu.com/p/5849361297)

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
  以windows10为例：

1. 在任务栏中rime输入法图标上右键，点击【用户文件夹】，将全部文件备份到其他文件夹下，清空setting文件夹；

2. 再次，点击【程序文件夹】；

3. 打开任务管理器，找到【小狼毫算法服务】，右键【结束任务】；

4. 下载【setting】压缩文件，解压到【用户文件夹】中（setting文件夹）；

5. 到【程序文件夹】中，依次点击“WeaselServer.exe", "WeaselSetup.exe", "WeaselDeployer.exe";
6. 在任务栏中rime输入法图标上右键，点击【重新部署】
