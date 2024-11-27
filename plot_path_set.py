import os
import matplotlib.pyplot as plt

# デフォルトの保存パス
DEFAULT_SAVE_DIR = "../fig/"

# 元のplt.savefigを保持
_original_savefig = plt.savefig


# version取得関数
def version():
    return "0.0.1"

def custom_savefig(filename, *args, **kwargs):
    """
    カスタムsavefig関数: デフォルトで指定ディレクトリに保存
    """
    # ディレクトリが存在しない場合は作成
    os.makedirs(DEFAULT_SAVE_DIR, exist_ok=True)
    
    # フルパスを作成
    filepath = os.path.join(DEFAULT_SAVE_DIR, filename)
    
    # 元のsavefigを使用して保存
    _original_savefig(filepath, *args, **kwargs)
    print(f"Figure saved to {filepath}")

def set_default_save_dir(path):
    """
    デフォルト保存ディレクトリを変更
    """
    global DEFAULT_SAVE_DIR
    DEFAULT_SAVE_DIR = path
    print(f"Default save directory changed to {DEFAULT_SAVE_DIR}")

# matplotlibのplt.savefigをオーバーライド
plt.savefig = custom_savefig
