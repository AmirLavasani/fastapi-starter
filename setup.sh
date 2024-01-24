#!/bin/bash

# change ai-service-template to your service name
conda create --name ai-service-template python=3.11 && source activate ai-service-template

make install-deps
make install-dev-deps

export PYTHONPATH=`pwd`

make all

make run