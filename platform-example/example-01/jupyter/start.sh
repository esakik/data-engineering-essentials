#!/usr/bin/env bash

mkdir -p /app/notebooks
jupyter notebook --no-browser --allow-root --ip 0.0.0.0 --notebook-dir ./notebooks
