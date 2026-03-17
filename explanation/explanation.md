data extraction for each script
all_clusters                     = [API_TOKEN]
cluster_details                  = [API_TOKEN] #mapping
cluster_security                 = cluster_id #excluded from final report
efficiency_report                = cluster_id [along with time period startTime and endTime] #startTime is excluded
evictor_advconfig                = cluster_id   #need clarification on the output
hibernation_schedules            = [organization_id] #mapping
node_templates                   = cluster_id
nodes_list                       = cluster_id
platform_usage_report            = [API_TOKEN]
problematic_nodes                = cluster_id
problematic_workloads            = cluster_id
rebalancing_plan                 = cluster_id
rebalancing_schedules            = [API_Token]   #python script pending
unscheduled_pods                 = cluster_id
workload_scalingpolicies         = cluster_id
workloadautoscaler_agents_status = [organization_id] #mapping

[API_TOKEN]: api_token can be generated at child organization level/parent organization level
