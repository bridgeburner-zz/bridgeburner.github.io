# My Blog
---

The source used to create my blog, using
[Pelican](http://getpelican.com).

The pre-bundled theme is a minimally modified version of
[pelican-cait](https://github.com/hdra/pelican-cait).

Searches ../third_party/pelican-plugins/ for the sitemap plugin.

## Instructions
1. Clone/download this.
2. Use virtualenv to create a new environment, and pip to install
   needed libraries from requirements.txt.
```bash
virtualenv env
source env/bin/activate (or env/Scripts/activate for Windows)
pip install -r requirements.txt
```

3. Remove and add your own content in the `content` directory.

4. Generate the site using pelican (using `-r` if you want pelican to
   auto-regenerate the site when it detects changes)
```bash
pelican -r -s pelicanconf.py
```

5. Create a simple http server using python (or serve them elsehow) to
   browse the generated site using a browser.
