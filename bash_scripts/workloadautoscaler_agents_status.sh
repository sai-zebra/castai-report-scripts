#!/bin/bash

OUTPUT_DIR="../json_output/workloadautoscaler_agents_status"
TOKEN="b4a8f0f6ea194af7c629ffa3e66aad487401d9a392be90b25dfd0446b963e2ef"
ORGANIZATION_ID="fae4a07d-d873-47fa-b5bf-6f2a8e3750ba" # Replace with child organization ID (platform)

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