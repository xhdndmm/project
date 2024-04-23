sudo apt-get update
sudo apt-get install git
sudo apt-get install python3-pip
python3 -m pip install --upgrade pip
pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install torch torchvision torchaudio
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
cd stable-diffusion-webui/
pip3 install -r requirements_versions.txt
pip3 install -r requirements.txt
python3 launch.py