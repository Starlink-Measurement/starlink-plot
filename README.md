# Starlink Plot

Set the Jupyter Notebook kernel timeout config in `~/.jupyter/jupyter_notebook_config.py` to a high number such as 3 hours:
```
c.MappingKernelManager.kernel_info_timeout = 10800
```

Set the buffer or memory to the maximum available (Eg. 24 GB):
```
c.ServerApp.max_buffer_size = 25769803776
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
