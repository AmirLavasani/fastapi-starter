#!/bin/bash

conda create --name ai-service-template python=3.11

make install-deps
make install-dev-deps

export PYTHONPATH=`pwd`

make run