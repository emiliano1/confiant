# Coding test

## Get started

### Installation

```bash
virtualenv -p python3 venv
source venv/bin/activate

pip3 install -r requirements.txt
```

### Run the web server

```bash
cd src
export FLASK_DEBUG=1
flask run
```

Visit http://127.0.0.1:5000

### Run the CLI tool

```bash
python3 -m src.cli.pop
```

## API usage

```bash
curl --header "X-Auth-Token: 88d72110d6c27f7d231c4c3197364ef0a17551c5" http://127.0.0.1:5000/get/
{
    "success": true,
    "id": "c837d45d2b674568b9e35b47bd4f3504"
}
```

```bash
curl --header "X-Auth-Token: 88d72110d6c27f7d231c4c3197364ef0a17551c5" http://127.0.0.1:5000/get/c837d45d2b674568b9e35b47bd4f3504
{
    "success": true,
    "pending": true,
    "id": "c837d45d2b674568b9e35b47bd4f3504"
}
```
