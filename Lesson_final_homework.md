# 书生·浦语大模型实战营大作业

## 大作业介绍
- 可以在班级群中随机组队完成一个大作业项目，一些可提供的选题如下：
  - 人情世故大模型：一个帮助用户撰写新年祝福文案的人情事故大模型
  - 中小学数学大模型：一个拥有一定数学解题能力的大模型
  - 心理大模型：一个治愈的心理大模型
  - 工具调用类项目：结合 Lagent 构建数据集训练 InternLM 模型，支持对 MMYOLO 等工具的调用
- 其他基于书生·浦语工具链的小项目都在范围内，欢迎大家充分发挥想象力。

## 个人选题（组队3~5人）
- 选择一个垂直领域，收集该领域的专业资料构建专业知识库，并搭建专业问答助手，并在 OpenXLab 上成功部署
  - 心理大模型：一个治愈的心理大模型
    - 心理健康数据集：
      - PsyQA（一个中文心理健康问答数据集，完整数据集需申请）：https://github.com/thu-coai/PsyQA
      - 中文心理健康支持对话数据集(SmileChat)与大模型(MeChat)：https://github.com/qiuhuachuan/smile
      - 心理数据集1(172条问答数据，英文)：https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset
      - 心理数据集2(Collection of 33 Psychology Related Datasets)：https://www.kaggle.com/discussions/general/304994
      - 情感常用数据集整理：https://blog.csdn.net/weixin_43765589/article/details/132319745
      - SST 斯坦福情绪树库数据集：https://hyper.ai/datasets/15977（https://nlp.stanford.edu/sentiment/index.html）
      - 中文微博情感分析数据集（NLPCC2014）：https://hyper.ai/datasets/14390
      - ExpW 表情识别数据集：https://hyper.ai/datasets/17382
    - 参考文献：
      - 近期大模型动态：LLaMA-2-7B-32K的训练数据组织情况及面向儿童心理健康领域的微调模型推介：https://mp.weixin.qq.com/s/2_T0VKB_80UmZvW9VqrizQ
      - Falcon-7B大型语言模型在心理健康对话数据集上使用QLoRA进行微调：https://mp.weixin.qq.com/s/Pp1ra5zKn4CEQmrKOkBcjA
      - 人类的悲欢虽不相通，但情感分析模型读得懂：https://hyper.ai/news/14399
      - 心理学开放数据资源汇总 | 心理与行为大数据比赛数据源推荐：https://mp.weixin.qq.com/s/9eCAnjB8tM7ailrxXeCD2A
      - 大模型遇上心理健康咨询：MeChat、QiaoBan、SoulChat、MindChat四大心理健康领域微调模型总结：https://mp.weixin.qq.com/s/vSaHDJ6DxHVREefX8GHp_A
      - 基于百度文心一言ERNIE大模型的中文情感分析实战（自定义数据集）：https://mp.weixin.qq.com/s/oAGo3HMqxbaL4pY1p7qFGg
    - OpenXLab部署：
      - 应用部署：https://openxlab.org.cn/apps
      - 服务器资源申请（GPU，用于应用部署）：https://openxlab.org.cn/docs/apps/%E5%BA%94%E7%94%A8%E5%88%9B%E5%BB%BA%E6%B5%81%E7%A8%8B.html#%E8%B5%84%E6%BA%90%E7%94%B3%E8%AF%B7%E6%B5%81%E7%A8%8B
      - 注意事项：
        - 1.应用默认的启动文件为关联代码仓库根目录下的 app.py 文件 app.py 示例
        - 2.配置应用所需的运行环境，如有 Python 依赖项（pip 安装）可写入 requirements.txt 中，Debian 依赖项（apt-get 安装）可写入 packages.txt 中，并存放至代码仓库的根目录下
        - 3.如需提高应用中模型文件下载速度，建议尝试 模型托管
        - 4.应用默认在 7860 端口启动，请不要占用或改写个人应用的启动端口
      - 部署思路：
        - 先申请开通应用部署服务器
        - 再进入应用部署服务器，使用关联的github中的脚本，下载模型到本地（比如L3_sentence-transformer_download.py等）
        - 安装pip依赖包（pip install -r requirements.txt）
        - 加载向量数据库并持久化
        - 最后，在本地运行app.py文件，即可部署应用
