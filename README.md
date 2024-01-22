# PNG Inliner

This script looks for any local `.png` files in your HTML and inlines them as bytes.

## Installation

The easiest way to install is using [just](https://github.com/casey/just).
Download the repo and run
```bash
just build
```
and copy outputted `png_inliner` binary into your path.

Now to use simply run
```bash
png_inliner input.html > output.html
```
