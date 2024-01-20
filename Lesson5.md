# 第 5 节：LMDeploy 大模型量化部署实践

## 课程资料
- 课程文档链接：https://github.com/InternLM/tutorial/blob/main/lmdeploy/lmdeploy.md
- 课程视频链接：https://www.bilibili.com/video/BV1iW4y1A77P
- 作业提交地址：https://github.com/InternLM/tutorial/discussions/230
- 笔记提交地址：https://github.com/InternLM/tutorial/discussions/225

## 课程作业
- 基础作业：
  - 使用 LMDeploy 以本地对话、网页Gradio、API服务中的一种方式部署 InternLM-Chat-7B 模型，生成 300 字的小故事（需截图）
- 进阶作业（可选做）
  - 将第四节课训练自我认知小助手模型使用 LMDeploy 量化部署到 OpenXLab 平台。
  - 对internlm-chat-7b模型进行量化，并同时使用KV Cache量化，使用量化后的模型完成API服务的部署，分别对比模型量化前后和 KV Cache 量化前后的显存大小（将 bs设置为 1 和 max len 设置为512）。
  - 在自己的任务数据集上任取若干条进行Benchmark测试，测试方向包括：
    - （1）TurboMind推理+Python代码集成
    - （2）在（1）的基础上采用W4A16量化
    - （3）在（1）的基础上开启KV Cache量化
    - （4）在（2）的基础上开启KV Cache量化
    - （5）使用Huggingface推理(how?)
  - 备注：由于进阶作业较难，完成基础作业之后就可以先提交作业了，在后续的大作业项目中使用这些技术将作为重要的加分点！

## 课程随记
- TurboMind（推理(加速)引擎）：https://github.com/InternLM/lmdeploy/blob/main/docs/en/inference/turbomind.md
- Triton Inference Server（Nvida开源的机器学习推理引擎）：https://zhuanlan.zhihu.com/p/594107043

## 课程笔记

