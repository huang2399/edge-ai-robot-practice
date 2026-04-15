import torch
# 新模型：Transformer 实验

# --- Feature Flag 模拟 ---
USE_LR_SCHEDULER = True   # 设为 False 即可关闭新功能

if USE_LR_SCHEDULER:
    print("使用学习率调度器（实验性功能）")
else:
    print("使用默认学习率")