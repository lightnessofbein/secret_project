# secret_project

# create venv
python3 -m venv .venv

# install libs
pip install -r requirements.txt

# build image
docker build -t secret_backend .

# run image
docker run -p 8000:8000 secret_backend
