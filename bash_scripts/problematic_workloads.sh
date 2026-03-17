#!/bin/bash
 
CLUSTER_FILE="../cluster_details/clusters_list.txt"
OUTPUT_DIR="../json_output/problematic_workloads"
TOKEN="b4a8f0f6ea194af7c629ffa3e66aad487401d9a392be90b25dfd0446b963e2ef"
 
mkdir -p "$OUTPUT_DIR"
 
while IFS=',' read -r CLUSTER_ID CLUSTER_NAME || [[ -n "$CLUSTER_ID" ]]; do
 
    CLUSTER_ID=$(echo "$CLUSTER_ID" | xargs)
    CLUSTER_NAME=$(echo "$CLUSTER_NAME" | xargs)
 
    [ -z "$CLUSTER_ID" ] && continue
 
    echo "Processing Cluster: $CLUSTER_NAME ($CLUSTER_ID)"
 
    OUTPUT_FILE="$OUTPUT_DIR/${CLUSTER_NAME}.json"
 
    RESPONSE=$(curl --silent --location \
        --request GET \
        --url "https://api.cast.ai/v1/kubernetes/clusters/$CLUSTER_ID/problematic-workloads" \
        --header "accept: application/json" \
        --header "authorization: Bearer $TOKEN")
 
    echo "$RESPONSE" | jq . 2>/dev/null > "$OUTPUT_FILE"
 
    echo "Saved output to: $OUTPUT_FILE"
    echo ""
 
done < "$CLUSTER_FILE"
 
echo "All clusters processed!"
 