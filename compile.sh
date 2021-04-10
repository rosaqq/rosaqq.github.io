#!/bin/bash
# script for JetBrains IDE run configs
# because I couldn't get WebStorm to run a python script
# yes I am dumb maybe
python compile.py
# take out the trash
purgecss --css css/main.css --content index.html --output css/