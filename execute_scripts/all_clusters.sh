#!/bin/bash

OUTPUT_DIR="../json_output/all_clusters"
TOKEN="b4a8f0f6ea194af7c629ffa3e66aad487401d9a392be90b25dfd0446b963e2ef"

mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="$OUTPUT_DIR/all_clusters.json"

RESPONSE=$(curl --request GET \
     --url https://api.cast.ai/v1/kubernetes/external-clusters \
     --header 'accept: application/json' \
     --header "authorization: Bearer $TOKEN")

echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"

echo "Saved output to: $OUTPUT_FILE"
echo " "
echo "All Clusters retrieved successfully!"