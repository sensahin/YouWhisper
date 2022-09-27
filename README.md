# YouWhisper
Convert YouTube videos to text using openai/whisper

# Demo

Demo here: https://huggingface.co/spaces/sensahin/YouWhisper

# Docker Install

On a local machine you can use `docker-compose up` and then open up http://localhost
Docker hosts like Render.com and DigitalOcean should just work with this repo.

# Usage

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt


You may need [`rust`](http://rust-lang.org) installed as well, in case [tokenizers](https://pypi.org/project/tokenizers/) does not provide a pre-built wheel for your platform. If you see installation errors during the `pip install` command above, please follow the [Getting started page](https://www.rust-lang.org/learn/get-started) to install Rust development environment.

# UI

If you would like to test it with web ui, you can run following and open **http://127.0.0.1:80/** in your browser.

```bash
python webapp.py
```

# Screenshot

![Screenshot5](screenshot5.png)

![Screenshot](screenshot.png)

![Screenshot2](screenshot2.png)

![Screenshot3](screenshot3.png)

# Docker

Live demo: https://whisper-dnrl.onrender.com/

Max memory consumption in tests is around 750mb. Works on Render.com (and probably DigitalOcean) as a Docker app with zero install.

However, the app is slow on a virtual cpu.
