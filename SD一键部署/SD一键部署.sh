sudo apt update
sudo apt install git
sudo apt install python3-pip
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install torch torchvision torchaudio
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui/
pip install -r requirements_versions.txt
pip install -r requirements.txt
python3 launch.py