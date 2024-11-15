#!/bin/bash

# Define the base folder and subfolders
druid_data_logs_folder="./data_logs/druid_data_logs"
data_logs_folders=("druid_shared" "coordinator_var" "broker_var" "historical_var" "middle_var" "router_var")

# Check if the base folder exists
if [ -d "$druid_data_logs_folder" ]; then
    # If it exists, remove it
    sudo rm -rf "$druid_data_logs_folder"
fi

# Create the base folder
sudo mkdir -p "$druid_data_logs_folder"

# Create the subfolders within the base folder
for folder in "${data_logs_folders[@]}"; do
    sudo mkdir -p "$druid_data_logs_folder/$folder"
done

# Set permissions for the base folder and subfolders
sudo chmod -R 777 "$druid_data_logs_folder"

