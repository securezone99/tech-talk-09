# tech-talk-09
Cursor AI 


### 1. Create a virtual environment

```shell
sudo apt install python3.12-venv
sudo apt-get install python3.12-dev

python3.12 -m venv x_venv
source x_venv/bin/activate
cp .envExample .env
pip install -r requirements.txt
cd cursor/app
python -B -m uvicorn main:app --reload --log-level info
```