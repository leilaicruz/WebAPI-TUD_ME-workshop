#!/bin/bash
echo "Installing jq and curl if not available"
apt-get update && apt-get install -y curl jq
