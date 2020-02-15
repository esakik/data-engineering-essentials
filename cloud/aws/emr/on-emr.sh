#!/usr/bin/env bash

python src/mr_word_count.py -r emr input.txt -c config.yaml --output-dir=s3://emr-001/output/