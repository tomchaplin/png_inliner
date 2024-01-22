venv:
	[ -d .venv ] || python -m venv .venv
	[ -d .venv ] || .venv/bin/python -m pip install -r requirements.txt

build: venv
	.venv/bin/python -m nuitka --output-filename=png_inliner --onefile png_inliner.py
