#!/bin/bash

OUTPUT_DIR="json_output/hibernation_schedules"
TOKEN="<API_TOKEN>"
ORGANIZATION_ID="<ORG_ID>" # Replace with child organization ID (platform)

mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="$OUTPUT_DIR/hibernation_schedules.json"

RESPONSE=$(curl --request GET \
     --url https://api.cast.ai/cluster-autoscaler/v1beta/organizations/$ORGANIZATION_ID/hibernation-schedules \
     --header 'accept: application/json' \
     --header "authorization: Bearer $TOKEN")

echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"

echo "Saved output to: $OUTPUT_FILE"
echo " "
echo "Hibernation schedules retrieved successfully!"