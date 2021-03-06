============================
Labo X: TCP with Packetdrill
============================

Situation
---------


The goal of this lab is to test your comprehension of TCP using the google tool packetdrill (https://code.google.com/p/packetdrill/).

First of all take some times to get familiar with the script language used by packetdrill. You can find some documentation and some example on the site given above.

With packetdrill, you can test the TCP network stack. In other words packetdrill permits you to send packet to an interface an to verify the incoming packets.

Below is a quick example of a TCP connection :
.. code-block::
    // The script starts by setting up a socket and then, establish a connection
    0 socket(..., SOCK_STREAM, IPPROTO_TCP) = 3 //create a socket
    +0 setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0 //avoid binding issues
    +0 bind(3, ..., ...) = 0 // bind socket
    +0 listen(3, 1) = 0 //start listening
    //Establish a connection
    +0 < S 0:0(0) win 32792 <mss 1000>    //inject a SYN into the kernel
    +0 > S. 0:0(0) ack 1 <...>//expect a SYN/ACK from the kernel
    +.1 < . 1:1(0) ack 1 win 100//inject an ACK  
    +0 accept (3, ..., ...) = 4	//accept connection.



Packetdrill has a syntax close to the output of tcpdump. The syntax of the
beginning of each line is given by the following figure.


  .. figure:: ../../png/labs/packetdrill/syntax_packetdrill.png
     :align: center
     :scale: 100

"<" denotes an incoming packet going to the kernel

">" denotes an outgoing packet comming from the kernel

Then you have a synthax close to a tcpdump output. When TCP doesn't behave like
your script, packetdrill raise an error and prints the actual packet and the
desired packet.

Instructions
------------

First, we ask you to understand the tcpdump trace produce by the given scripts.
Use packetdrill in sudo mode to produce the trace. Listen on the interface
[TODO: TUN interface not here => Ask to fabien duchenne]

Now that you are familiar with the packetdrill syntax, we ask you to use it to test all the possible scenario for an etablishment of a TCP connection.
You have the exemple above and an exemple showing how to  initiate a connection
from the kernel (it's slightly different, you have to write a syscall for that)
in the tcp_connection_retransmit.pkt 

Quick reminder :

  .. figure:: ../../png/labs/transport/connection.png
     :align: center
     :scale: 100



Go further
------------


Packetdrill is very interesting to test if you have well understood how tcp
works. Do not hesitate to try other TCP functionalities or experiment situation
you're not sure you have well understood.

Have fun!


