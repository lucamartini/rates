#!/bin/bash

python readcsv.py
python csv2tex.py
cd news/
pdflatex news
