# Basic Code
## 1. Use The Code
Configuration Environment
```bash
conda create -n code_base python=3.6
conda activate code_base
pip install -r requirements.txt -i  https://pypi.doubanio.com/simple/
sh env.sh
```
Train
```bash
python train.py
```
Test
```bash
python test.py
```
## 2. Reconstruction Effect
Left: source image | Right: reconstructed image

<img src="./test_input_folder/xi.jpg" width="256" height="256" />       <img src="./test_results/xi.jpg" width="256" height="256" />

## 3. AI-Broad-casting
Please download checkpoints from [Google drive](https://drive.google.com/drive/folders/12y8Ff-UM4DL0NWYCIPQaiAbXPGCocuvw?usp=sharing)

Usage reference: (https://bytedance.feishu.cn/docx/doxcn646idTDylS6A3zdHoSQmXd)