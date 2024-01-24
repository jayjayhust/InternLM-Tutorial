# pip install -U huggingface_hub

import os 
from huggingface_hub import hf_hub_download  # Load model directly 

hf_hub_download(repo_id="internlm/internlm2-chat-7b", filename="config.json")