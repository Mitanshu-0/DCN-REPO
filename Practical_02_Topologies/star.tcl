set ns [new Simulator]

set nf [open star.nam w]
$ns namtrace-all $nf

set tf [open star.tr w]
$ns trace-all $tf

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]

$ns duplex-link $n0 $n1 5Mb 20ms DropTail
$ns duplex-link $n0 $n2 5Mb 20ms DropTail
$ns duplex-link $n0 $n3 5Mb 20ms DropTail
$ns duplex-link $n0 $n4 5Mb 20ms DropTail
$ns duplex-link $n0 $n5 5Mb 20ms DropTail
$ns duplex-link $n0 $n6 5Mb 20ms DropTail
$ns duplex-link $n0 $n7 5Mb 20ms DropTail

$ns queue-limit $n0 $n1 10
$ns queue-limit $n0 $n2 10
$ns queue-limit $n0 $n3 10
$ns queue-limit $n0 $n4 10
$ns queue-limit $n0 $n5 10
$ns queue-limit $n0 $n6 10
$ns queue-limit $n0 $n7 10

set tcp [new Agent/TCP]
$ns attach-agent $n1 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n7 $sink

$ns connect $tcp $sink

$tcp set fid_ 1
$ns color 1 Red

set ftp [new Application/FTP]
$ftp attach-agent $tcp

$ns at 0.5 "$ftp start"
$ns at 4.5 "$ftp stop"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exec nam star.nam &
    exit 0
}

$ns at 5.0 "finish"
$ns run
