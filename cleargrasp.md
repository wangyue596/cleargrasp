#ClearGrasp复现
[参考](https://github.com/JinraeKim/cleargrasp/blob/master/README.md)

##下载仓库代码复现
### 1. pip install -r requirements.txt报错
could not fetch URL

解决方法：
`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U  --trusted-host pypi.tuna.tsinghua.edu.cn`

### 2. command 
command "python stup.py egg_info"failed with error code 1 in ...

解决方法：
`pip install setuptools_scm、pip install --upgrade setuptools`

### 3. openexr版本报错
[链接](https://blog.csdn.net/m0_49800270/article/details/132438753)
### 4. torch版本报错：
`pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f` [官方库](https://download.pytorch.org/whl/cu111/torch_stable.html)