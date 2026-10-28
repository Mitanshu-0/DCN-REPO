BEGIN { sent=0; received=0 }
$1=="+" && $5=="tcp" && $3=="0" { sent += $6 }
$1=="r" && $5=="tcp" && $4=="3" { received += $6 }
END { if (sent > 0) printf "%.2f", (received/sent)*100; else printf "0.00" }
