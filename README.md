# Starlink Plot

Set your Jupyter Lab kernel timeout config in `~/.jupyter/jupyter_lab_config.py` to a high number such as 3 hours:
```
c.MappingKernelManager.kernel_info_timeout = 10800
```

## Simplified Steps

Install `pipenv`:
```bash
pip install pipenv
```

Install all packages in Pipfile.lock
```bash
pipenv install
```

Start Jupyter Lab instance.
```bash
pipenv shell
jupyter lab
```

Access through the browser.
