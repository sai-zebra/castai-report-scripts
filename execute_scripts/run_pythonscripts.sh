#!/bin/bash

BASE_DIR=$(dirname "$0")/..
SCRIPT_DIR="$BASE_DIR/python_scripts"

for file in "$SCRIPT_DIR"/*.py; do
    if [ -f "$file" ]; then
        echo "Executing $file..."
        python "$file"
    fi
done

echo "All Python scripts executed Successfully."