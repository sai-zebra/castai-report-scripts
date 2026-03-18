#!/bin/bash

set -e

BASE_DIR=$(dirname "$0")/..
SCRIPT_DIR="$BASE_DIR/bash_scripts"

for file in "$SCRIPT_DIR"/*.sh; do
    if [ -f "$file" ]; then
        echo "Executing $file..."
        bash "$file"
    fi
done

echo "All bash scripts executed Successfully."