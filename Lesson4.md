# 第 4 节：XTuner 大模型单卡低成本微调实战

## 课程资料
- 课程文档链接：https://github.com/InternLM/tutorial/blob/main/xtuner/README.md
- 课程视频链接：https://www.bilibili.com/video/BV1yK4y1B75J
- 作业提交地址：https://github.com/InternLM/tutorial/discussions/229 (https://zhuanlan.zhihu.com/p/679609413)
- 笔记提交地址：https://github.com/InternLM/tutorial/discussions/224

## 课程作业
- 基础作业：
  - 构建数据集，使用 XTuner 微调 InternLM-Chat-7B 模型, 让模型学习到它是你的智能小助手，效果如下图所示，本作业训练出来的模型的输出需要将“不要葱姜蒜大佬”替换成自己名字或昵称！(参考答案：https://github.com/InternLM/tutorial/blob/main/xtuner/self.md)
- 进阶作业：
  - 将训练好的Adapter模型权重上传到 OpenXLab、Hugging Face 或者 MoelScope 任一一平台。
  - 将训练好后的模型应用部署到 OpenXLab 平台，参考部署文档请访问：https://aicarrier.feishu.cn/docx/MQH6dygcKolG37x0ekcc4oZhnCe

## 课程笔记
- 1 概述
  - 1.1 XTuner
  - 1.2 支持的开源LLM (2023.11.01)
  - 1.3 特色
  - 1.4 微调原理
- 2 快速上手
  - 2.1 平台：Ubuntu + Anaconda + CUDA/CUDNN + 8GB nvidia显卡
  - 2.2 安装：
    - xtuner：https://github.com/InternLM/xtuner
  - 2.3 微调：
    - 准备配置文件
    - 模型下载（internlm-chat-7b）：https://modelscope.cn/Shanghai_AI_Laboratory/internlm-chat-7b.git
    - 数据集下载（）：https://huggingface.co/datasets/timdettmers/openassistant-guanaco/tree/main
    - 修改配置文件
    - 开始微调
    - 将得到的 PTH 模型转换为 HuggingFace 模型，即：生成 Adapter 文件夹（hf 文件夹即为我们平时所理解的所谓 “LoRA 模型文件”）
  - 2.4 部署与测试：
    - 将 HuggingFace adapter 合并到大语言模型
    - 与合并后的模型对话
    - Demo运行
- 3 自定义微调
  - 3.1 概述：基于 InternLM-chat-7B 模型，用 MedQA 数据集进行微调，将其往医学问答领域对齐。
  - 3.2 数据准备(Medication QA)：https://github.com/abachaa/Medication_QA_MedInfo2019
    - 将数据转为 XTuner 的数据格式
    - 划分训练集和测试集
  - 3.3 开始自定义微调
    - 准备配置文件
    - XTuner！启动！
    - pth 转 huggingface
    - 部署与测试
- 4【补充】用 MS-Agent 数据集赋予 LLM 以 Agent 能力
  - 概述
  - 微调步骤
    - 准备工作
    - 开始微调
  - 直接使用
    - 下载 Adapter
    - 添加 serper 环境变量（https://serper.dev/login，区别于google的serpapi：https://serpapi.com/）：去 serper.dev 免费注册一个账号，生成自己的 api key。这个东西是用来给 lagent 去获取 google 搜索的结果的。等于是 serper.dev 帮你去访问 google，而不是从你自己本地去访问 google 了。
    - 报错处理
- 5 注意事项
  - 本教程使用 xtuner 0.1.9 版本 若需要跟着本教程一步一步完成，建议严格遵循本教程的步骤!
  - 若出现莫名其妙报错，请尝试更换为以下包的版本：（如果有报错再检查，没报错不用看）
```
torch                         2.1.1
transformers                  4.34.0
transformers-stream-generator 0.0.4

pip install torch==2.1.1
pip install transformers==4.34.0
pip install transformers-stream-generator=0.0.4
```
  - CUDA 相关：（如果有报错再检查，没报错不用看）
```
NVIDIA-SMI 535.54.03              
Driver Version: 535.54.03    
CUDA Version: 12.2

nvidia-cuda-cupti-cu12        12.1.105
nvidia-cuda-nvrtc-cu12        12.1.105
nvidia-cuda-runtime-cu12      12.1.105
```