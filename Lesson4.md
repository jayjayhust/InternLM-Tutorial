# 第 4 节：XTuner 大模型单卡低成本微调实战

## 课程资料
- 课程文档链接：https://github.com/InternLM/tutorial/blob/main/xtuner/README.md
- 课程视频链接：https://www.bilibili.com/video/BV1yK4y1B75J
- 作业提交地址：https://github.com/InternLM/tutorial/discussions/229
- 笔记提交地址：https://github.com/InternLM/tutorial/discussions/224

## 课程作业
- 基础作业：
  - 构建数据集，使用 XTuner 微调 InternLM-Chat-7B 模型, 让模型学习到它是你的智能小助手，效果如下图所示，本作业训练出来的模型的输出需要将“不要葱姜蒜大佬”替换成自己名字或昵称！
- 进阶作业：
  - 将训练好的Adapter模型权重上传到 OpenXLab、Hugging Face 或者 MoelScope 任一一平台。
  - 将训练好后的模型应用部署到 OpenXLab 平台，参考部署文档请访问：https://aicarrier.feishu.cn/docx/MQH6dygcKolG37x0ekcc4oZhnCe

## 课程笔记
- 4【补充】用 MS-Agent 数据集 赋予 LLM 以 Agent 能力
  - 添加 serper 环境变量（https://serper.dev/login，区别于google的serpapi：https://serpapi.com/）：去 serper.dev 免费注册一个账号，生成自己的 api key。这个东西是用来给 lagent 去获取 google 搜索的结果的。等于是 serper.dev 帮你去访问 google，而不是从你自己本地去访问 google 了。