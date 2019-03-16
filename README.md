# Elespike's publisher script

Creates an HTML and a PDF file from several markdown files/chapters with pretty CSS.

Have a look at the following files in this directory:
- `publisher.pdf`
- `publisher.html`

## Prerequisites

Tested on Debian:
```bash
apt-get install pandoc

# Requirements for weasyprint according to https://weasyprint.readthedocs.io/en/latest/install.html#linux
apt-get install \
build-essential \
python3-dev \
python3-pip \
python3-setuptools \
python3-wheel \
python3-cffi \
libcairo2 \
libpango-1.0-0 \
libpangocairo-1.0-0 \
libgdk-pixbuf2.0-0 \
libffi-dev \
shared-mime-info

pip3 install weasyprint

# Tell the system where the weasyprint binary is
export PATH=$PATH:$HOME/.local/bin
```

## Operation

1. `git clone https://github.com/elespike/publisher`
2. `cd publisher`
3. Edit the `metadata.yaml` file with your desired values, leaving unused ones empty.
4. Have a look at the included examples and use them to guide your content creation.  
  a. Create as many markdown files as you need; files whose name starts with `_` will be ignored by `publisher.py`.  
  b. File names should begin with a numerical value, and will be compiled into the final document in numerical order.
5. When ready, run `python3 ./publisher.py`!  
  a. Have a look at the files created by the script: `publisher.pdf` and `publisher.html`.

## Feeling adventurous?

- Have a look at `template.html`, as it contains the default CSS and layout of the document, and edit it to your liking.
- Create your own CSS (feel free to use the provided `./static/css` directory for storage) and add a `link rel` directive within `template.html` to reference it.

