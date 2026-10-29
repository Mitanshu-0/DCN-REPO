BEGIN{
    rec=1;
    send=1;
    rate=0;
}
{
    if ( $1 == "+" && $5 == "tcp" && $3 == "0")
    {
        send = send + $6
    }
    if ( $1 == "r" && $5 == "tcp" && $4 == "3")
    {
        rec = rec + $6
    }
    rate=(rec/send)*100;
}
END{
    printf("%f %f\n", bw, rate) >> "result1.log";
}
