# 第 6 节：OpenCompass 大模型评测

## 课程资料
- 课程文档链接：https://github.com/InternLM/tutorial/blob/main/opencompass/opencompass_tutorial.md
- 课程视频链接：
- 作业提交地址：https://github.com/InternLM/tutorial/discussions/231 (https://zhuanlan.zhihu.com/p/679619677)
- 笔记提交地址：https://github.com/InternLM/tutorial/discussions/226 (https://github.com/jayjayhust/InternLM-Tutorial/blob/main/Lesson6.md)

## 课程作业
- 基础作业：
  - 使用 OpenCompass 评测 InternLM2-Chat-7B 模型在 C-Eval 数据集上的性能
    - 模型下载（modelscope）：https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-chat-7b/summary
    ```
    import torch
    from modelscope import snapshot_download, AutoModel, AutoTokenizer
    import os

    # model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm2-chat-7b', cache_dir='/root/model', revision='v1.0.3')
    model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm2-chat-7b', cache_dir='/root/model')
    ```
    - opencompass下载（开发机上下载不了最新的opencompass，然后gitee上的opencompass不是最新的，只能自己镜像一个github的到gitee）：https://gitee.com/hunan_ai_league_jayhust/opencompass
    ```
    git clone https://gitee.com/hunan_ai_league_jayhust/opencompass
    cd opencompass
    ```
    - 数据集下载：https://github.com/open-compass/opencompass?tab=readme-ov-file#-data-preparation
    ```
    cp /share/temp/datasets/OpenCompassData-core-20231110.zip /root/opencompass/
    unzip OpenCompassData-core-20231110.zip
    ```
    - 评测命令：
    ```
    python tools/list_configs.py internlm2 ceval
    ```
    结果如下：
    ```
    +-----------------------+-----------------------------------------------------+
    | Model                 | Config Path                                         |
    |-----------------------+-----------------------------------------------------|
    | hf_internlm2_20b      | configs/models/hf_internlm/hf_internlm2_20b.py      |
    | hf_internlm2_7b       | configs/models/hf_internlm/hf_internlm2_7b.py       |
    | hf_internlm2_chat_20b | configs/models/hf_internlm/hf_internlm2_chat_20b.py |
    | hf_internlm2_chat_7b  | configs/models/hf_internlm/hf_internlm2_chat_7b.py  |
    +-----------------------+-----------------------------------------------------+
    +----------------------------+------------------------------------------------------+
    | Dataset                    | Config Path                                          |
    |----------------------------+------------------------------------------------------|
    | ceval_clean_ppl            | configs/datasets/ceval/ceval_clean_ppl.py            |
    | ceval_gen                  | configs/datasets/ceval/ceval_gen.py                  |
    | ceval_gen_2daf24           | configs/datasets/ceval/ceval_gen_2daf24.py           |
    | ceval_gen_5f30c7           | configs/datasets/ceval/ceval_gen_5f30c7.py           |
    | ceval_ppl                  | configs/datasets/ceval/ceval_ppl.py                  |
    | ceval_ppl_578f8d           | configs/datasets/ceval/ceval_ppl_578f8d.py           |
    | ceval_ppl_93e5ce           | configs/datasets/ceval/ceval_ppl_93e5ce.py           |
    | ceval_zero_shot_gen_bd40ef | configs/datasets/ceval/ceval_zero_shot_gen_bd40ef.py |
    +----------------------------+------------------------------------------------------+
    ```
    (先下载模型到本地：/root/model/Shanghai_AI_Laboratory/internlm2-chat-7b)
    ```
    python run.py --datasets ceval_gen --hf-path /root/model/Shanghai_AI_Laboratory/internlm2-chat-7b/ --tokenizer-path /root/model/Shanghai_AI_Laboratory/internlm2-chat-7b/ --tokenizer-kwargs padding_side='left' truncation='left' trust_remote_code=True --model-kwargs trust_remote_code=True device_map='auto' --max-seq-len 2048 --max-out-len 16 --batch-size 4 --num-gpus 1 --debug
    ```
- 进阶作业（可选做）
  - 使用 OpenCompass 评测 InternLM2-Chat-7B 模型使用 LMDeploy 0.2.0 部署后在 C-Eval 数据集上的性能
  - 备注：由于进阶作业较难，完成基础作业之后就可以先提交作业了，在后续的大作业项目中使用这些技术将作为重要的加分点！

## 课程随记
- 

## 课程笔记

