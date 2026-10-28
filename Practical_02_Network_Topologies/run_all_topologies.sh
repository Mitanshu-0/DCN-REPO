#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
for topo in bus star ring mesh; do
  case "$topo" in bus) src=0;dst=10;tr=bus.tr;; star) src=1;dst=7;tr=star.tr;; ring) src=0;dst=4;tr=ring8.tr;; mesh) src=0;dst=7;tr=mesh.tr;; esac
  echo "========== ${topo^^} TOPOLOGY =========="
  ns "$topo.tcl"
  awk -v src="$src" -v dst="$dst" -f performance.awk "$tr"
done
