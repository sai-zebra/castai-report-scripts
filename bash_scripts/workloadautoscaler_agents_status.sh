#!/bin/bash

OUTPUT_DIR="json_output/workloadautoscaler_agents_status"
TOKEN="<API_TOKEN>"
ORGANIZATION_ID="<ORG_ID>" # Replace with child organization ID (platform)

mkdir -p "$OUTPUT_DIR"

OUTPUT_FILE="$OUTPUT_DIR/workloadautoscaler_agents_status.json"

RESPONSE=$(curl --request GET \
     --url https://api.cast.ai/v1/workload-autoscaling/organizations/$ORGANIZATION_ID/components/workload-autoscaler \
     --header 'accept: application/json' \
     --header "authorization: Bearer $TOKEN")

echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"

echo "Saved output to: $OUTPUT_FILE"
echo " "
echo "workloadautoscaler_agents_status retrieved successfully!"