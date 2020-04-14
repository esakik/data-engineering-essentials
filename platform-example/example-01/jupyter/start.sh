#!/usr/bin/env bash

mkdir -p /root/.jupyter
mkdir -p /app/notebooks

JUPYTER_CONFIG=/root/.jupyter/jupyter_notebook_config.py
NOTEBOOK_DIR=./notebooks
PASSWORD=`python -c 'from notebook.auth import passwd;print(passwd())'`

echo "c.NotebookApp.password = '$PASSWORD'" > $JUPYTER_CONFIG
jupyter notebook --no-browser --allow-root --ip 0.0.0.0 --notebook-dir $NOTEBOOK_DIR
