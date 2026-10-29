#!/bin/bash

echo "========================================"
echo "     DCN EXPERIMENT 2 - ALL TOPOLOGIES"
echo "========================================"

echo ""
echo "========== BUS TOPOLOGY =========="
cd /home/jarvis/DCN_LAB/practical_2/bus
ns bus.tcl
awk -v src=0 -v dst=7 -f ../performance.awk bus.tr

echo ""
echo "========== STAR TOPOLOGY =========="
cd /home/jarvis/DCN_LAB/practical_2/star
ns star.tcl
awk -v src=1 -v dst=7 -f ../performance.awk star.tr

echo ""
echo "========== RING TOPOLOGY =========="
cd /home/jarvis/DCN_LAB/practical_2/ring
ns ring.tcl
awk -v src=0 -v dst=4 -f ../performance.awk ring8.tr

echo ""
echo "========== MESH TOPOLOGY =========="
cd /home/jarvis/DCN_LAB/practical_2/mesh
ns mesh.tcl
awk -v src=0 -v dst=7 -f ../performance.awk mesh.tr

echo ""
echo "========================================"
echo "          ALL RESULTS COMPLETED"
echo "========================================"
