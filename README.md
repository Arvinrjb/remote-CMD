# remote-CMD

This is a script for remote execution of operating system command line commands within the local network.

### Installing packages:
Install [python3](https://www.python.org/downloads/)
```
pip install colorama
pip install platform
pip install socket
```

### How to use?

In the first step, to run this script, you need to know the IP that the operating system got from the DHCP server. To do this, use the `ipconfig` command in Windows and the `ifconfig` command in Linux.
<br>
<h2>In Windows:</h2>
  <a href="https://github.com/Arvinrjb/remote-CMD"><img src="imgs/img1.png" alt="remote-CMD"></a>
<hr>
<h2>In Linux:</h2>
  <a href="https://github.com/Arvinrjb/remote-CMD"><img src="imgs/img2.png" alt="remote-CMD"></a>
<hr>

In the first step, run the main.py script on your host system and enter the IP you found in the previous step.
And here the work with the first system ends!

Now run the client.py program on the system you want to send your commands to and enter the ip on which the first system is listening, and now it's the turn of your desired command, which commands according to the operating system you are using Run yourself and finally type 'e' and enter to exit the program.


# Warning!!

Avoid running it when you don't need it because this program can create security problems for your system and be subject to external attacks
