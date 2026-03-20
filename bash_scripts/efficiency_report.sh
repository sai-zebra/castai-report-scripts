#!/bin/bash

CLUSTER_FILE="cluster_details/clusters_list.txt"
OUTPUT_DIR="json_output/efficiency_report"
TOKEN="${API_TOKEN}"

if [ -z "$START_TIME" ] || [ -z "$END_TIME" ]; then
    echo "ERROR: START_TIME and END_TIME must be provided 
    in ISO format(YYYY:MM:DDTHH:MM:SS.000000Z)"
    exit 1
fi

#debug
echo "Start Time: $START_TIME"
echo "End Time: $END_TIME"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

while IFS=',' read -r CLUSTER_ID CLUSTER_NAME || [[ -n "$CLUSTER_ID" ]]; do

    CLUSTER_ID=$(echo "$CLUSTER_ID" | xargs)
    CLUSTER_NAME=$(echo "$CLUSTER_NAME" | xargs)

    [ -z "$CLUSTER_ID" ] && continue

    echo "Processing Cluster: $CLUSTER_NAME ($CLUSTER_ID)"

    OUTPUT_FILE="$OUTPUT_DIR/${CLUSTER_NAME}.json"

    RESPONSE=$(curl --silent --location \
        --request GET \
        --url "https://api.cast.ai/v1/cost-reports/clusters/$CLUSTER_ID/efficiency?startTime=$START_TIME&endTime=$END_TIME" \
        --header "accept: application/json" \
        --header "authorization: Bearer $TOKEN")

    echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"

    echo "Saved output to: $OUTPUT_FILE"
    echo ""

done < "$CLUSTER_FILE"

echo "All clusters processed!"