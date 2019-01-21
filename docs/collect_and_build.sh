#!/bin/sh

# Auto-collect modules
sphinx-apidoc -o . ../app


# Build Documentation
make html

# Open the documentation
open ./build/html/index.html