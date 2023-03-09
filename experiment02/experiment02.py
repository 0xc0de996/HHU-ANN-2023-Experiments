try:
    import torch
except ImportError as e:
    os.system("pip install torch -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import torch

try:
    import torchvision
except ImportError as e:
    os.system("pip install torchvision -i https://pypi.tuna.tsinghua.edu.cn/simple")
    import torchvision
    
def main():
    return torch.tensor(0)
    