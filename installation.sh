curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > "Miniconda3.sh"
bash Miniconda3.sh

sudo apt install build-essential

conda create -n textgen python=3.10.9
conda activate textgen

pip3 install torch torchvision torchaudio


git clone https://github.com/ubbikk/text-generation-webui/
cd text-generation-webui
pip install -r requirements.txt

curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
cd models
git clone https://huggingface.co/MetaIX/OpenAssistant-Llama-30b-4bit
cd ..


python server.py  --model OpenAssistant-Llama-30b-4bit --auto-devices --model_type LLaMA --listen --api --listen-host hobo1.z.min.org.ua --listen-port 9000