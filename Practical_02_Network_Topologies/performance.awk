BEGIN {
    rec=0;
    send=0;
    s=0;
    pr=0;
    t=0;
    tr=0;
}

{
    if($1=="+" && $5=="tcp" && $3==src)
    {
        send++;
        s=send;
    }

    if($1=="r" && $5=="tcp" && $4==dst)
    {
        rec++;
    }

    if($1=="r" && $4==dst && $5=="tcp")
    {
        t=t+$6;
        tr=t*8/$2/1000000;
    }
}

END {
    pr=rec/s;

    printf("Number of packets send to node %d = %d\n",dst,s);
    printf("Number of packets received at node %d = %d\n",dst,rec);
    printf("Packet delivery ratio at node %d is %f\n",dst,pr);
    printf("Throughput of tcp connection to node %d = %f\n",dst,tr);
}
