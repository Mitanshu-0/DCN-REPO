#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
: > result1.log
for bw in 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0; do
  echo "Running simulation for ${bw}Mb..."
  ns ring_network.tcl "${bw}Mb"
  rate=$(awk -f packet_delivery.awk testout.tr)
  echo "$bw $rate" >> result1.log
  echo "Bandwidth = ${bw} Mb, Rate = ${rate}%"
done
cat result1.log
