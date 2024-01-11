# 第 2 节：轻松玩转书生·浦语大模型趣味 Demo 作业

## 课程资料
- 课程文档链接：https://github.com/InternLM/tutorial/blob/main/helloworld/hello_world.md
- 课程视频链接：https://www.bilibili.com/video/BV1Ci4y1z72H
- 作业提交地址：https://github.com/InternLM/tutorial/discussions/227
- 笔记提交地址：https://github.com/InternLM/tutorial/discussions/222

## 课程作业
- 基础作业：
  - 使用 InternLM-Chat-7B 模型生成 300 字的小故事（需截图）。
  - 熟悉 hugging face 下载功能，使用 huggingface_hub python 包，下载 InternLM-20B 的 config.json 文件到本地（需截图下载过程）。

- 进阶作业（可选做）
  - 完成浦语·灵笔的图文理解及创作部署（需截图）
  - 完成 Lagent 工具调用 Demo 创作部署（需截图）

- 整体实训营项目：
  - 时间周期：即日起致课程结束
  - 即日开始可以在班级群中随机组队完成一个大作业项目，一些可提供的选题如下：
    - 人情世故大模型：一个帮助用户撰写新年祝福文案的人情事故大模型
    - 中小学数学大模型：一个拥有一定数学解题能力的大模型
    - 心理大模型：一个治愈的心理大模型
    - 工具调用类项目：结合 Lagent 构建数据集训练 InternLM 模型，支持对 MMYOLO 等工具的调用
  - 其他基于书生·浦语工具链的小项目都在范围内，欢迎大家充分发挥想象力。

## 课程笔记
- 1 大模型及 InternLM 模型简介
  - 1.1 什么是大模型？
  - 1.2 InternLM 模型全链条开源
- 2 InternLM-Chat-7B 智能对话 Demo
  - 2.1 环境准备
  - 2.2 模型下载
  - 2.3 代码准备
  - 2.4 终端运行
  - 2.5 web demo 运行
- 3 Lagent 智能体工具调用 Demo
  - 3.1 环境准备
  - 3.2 模型下载
  - 3.3 Lagent 安装
  - 3.4 修改代码
  - 3.5 Demo 运行
- 4. 浦语·灵笔图文理解创作 Demo
  - 4.1 环境准备
  - 4.2 模型下载
  - 4.3 代码准备
  - 4.4 Demo 运行
- 5. 通用环境配置
  - 5.1 pip、conda 换源
    - 5.1.1 pip 换源
    - 5.1.2 conda 换源
  - 5.2 配置本地端口
  - 5.3 模型下载
    - 5.3.1 Hugging Face
    - 5.3.2 ModelScope
    - 5.3.3 OpenXLab
- 6. 课后作业
  - 初步选择：心理大模型（一个治愈的心理大模型）
    - 6.1 数据集准备
      - 6.1.1 数据集1（172条问答数据，英文）：https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset
    - 6.2 模型训练/微调
    - 6.3 模型部署