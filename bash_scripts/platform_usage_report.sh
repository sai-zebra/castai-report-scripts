#!/bin/bash

OUTPUT_DIR="json_output/platform_usage_report"
TOKEN="${API_TOKEN}"

mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/platform_usage_report.json"

RESPONSE=$(curl --request GET \
     --url https://api.cast.ai/v1/billing/platform-usage-report \
     --header 'accept: application/json' \
     --header "authorization: Bearer $TOKEN")

echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"

echo "Saved output to: $OUTPUT_FILE"
echo " "
echo "Platform usage report retrieved successfully!"