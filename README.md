# Data Communication and Networking (DCN) Lab

**Course:** 4EC301CC25 · Nirma University · Semester VII

Source files organized by experiment from the supplied lab reports and Cisco Packet Tracer uploads.

## Contents

| Practical | Topic | Files |
|---|---|---|
| 1 | NS2 ring simulation and bandwidth / delivery analysis | `.tcl`, `.awk`, `.sh` |
| 2 | NS2 bus, star, ring, mesh topologies | `.tcl`, `.awk`, `.sh` |
| 3 | Stop-and-Wait simulation | `.tcl` |
| 4 | TCP socket messaging, chat and file transfer | `.py`, example input `.txt` |
| 5 | Packet Tracer LAN simulation | `.pkt` only |
| 6 | RIP routing | `.pkt` only |
| 7 | Packet Tracer topology | `.pkt` only |
| 8 | OSPF routing | **No `.pkt` uploaded** |

## Running

**NS2 (Linux):** Install NS2 + NAM and optionally AWK. From the respective folder, run `ns ring_network.tcl 1Mb` (Practical 1); run `bash run_bandwidth_test.sh` for all bandwidth values. In Practical 2 run `bash run_all_topologies.sh`; Practical 3: `ns stop_and_wait.tcl`. These use graphical NAM (`nam` command) at the end.

**Python sockets:** Start the matching `*_server.py` in one terminal, then the matching `*_client.py` in another (Python 3.8+). For two computers set `HOST` in the client to the server's accessible IP and allow the configured TCP port.

**Packet Tracer:** Open the `.pkt` files with Cisco Packet Tracer. The unlabelled original `EXP.pkt` is retained in Practical 5 pending identification; no claim is made that it belongs there.

## Source fidelity and limitations

- Practical 1 and 2 source scripts were extracted from the text of their `.docx` reports. Adjustments were made to runner scripts to use relative paths, match generated filenames, and calculate packet delivery once without duplicate output.
- Practical 3 TCL and Practical 4 Part 1/2 programs were **reconstructed** from screenshots, not recovered as original editable source. Practical 4 file transfer was adapted from the report's printed code, with portable addressing, filename framing, and safe basename handling.
- Packet Tracer files were renamed for clarity but their binary content was not changed. Several uploads have ambiguous original names; exact contents were not verified in Cisco Packet Tracer.
- A Practical 8 OSPF report was supplied, but **no identifiable Practical 8 Packet Tracer project** was uploaded. Its directory is intentionally empty and thus won't appear on GitHub; add your `.pkt` when available.
- Reports for Practical 9 contain Wireshark screenshots, not source-code or Packet Tracer project files, so Practical 9 is intentionally excluded.

Generated from user-provided lab reports and `.pkt` project files. No runtime simulation verification performed.
