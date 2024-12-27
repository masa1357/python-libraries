import os
import random
import time
from argparse import ArgumentParser
from contextlib import contextmanager
from logging import Formatter, StreamHandler, getLogger
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from sklearn.model_selection import train_test_split



# version取得関数
def version():
    return "0.0.2"

#? loggerの設定
def set_logger(name: str = __name__):

    logger = getLogger(name)
    logger.setLevel("INFO")

    #? ハンドラが既に追加されているかをチェック
    if not logger.hasHandlers():
        #? 出力されるログの表示内容を定義
        formatter = Formatter(
            "%(asctime)s : %(name)s : %(levelname)s : %(lineno)s : %(message)s"
        )

        #? 標準出力のhandlerをセット
        stream_handler = StreamHandler()
        stream_handler.setLevel("INFO")
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    logger.info("Test_message")

    return logger

#? seedの固定
def set_seed(seed: int = 42):
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # 複数GPU対応
        torch.backends.cudnn.deterministic = True 
        torch.backends.cudnn.benchmark = False  

#? 時間計測関数
@contextmanager
def timer(name: str):
    t0 = time.time()
    print(f"[{name}] start")
    yield
    print(f"[{name}] done in {time.time() - t0:.2f} s")
