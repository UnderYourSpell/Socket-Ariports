# Socket-Ariports
For Computer Netowrks A365

Information about directories/files:
Socket-Airports holds all Client and Server Files needed to run this.
You will need to run all of them
libs holds the code that servers and clients are based on
libs also holds a file that contains airport code server information
logs holds logs of a comprehensive test run as well as a list of the tests I did (passenger list)
rescources holds python files of code I used to help me write this, much of it is unused as I went along
my code got much more specific to the purpose of this assignment.


Instructions to Run:

Python version 3.11.5
Written in VSCode on Windows 11

1. Open main directory in a powershell/terminal.  Do this 13 times total.
2. start the servers by running > py ./xxx_server.py do this for all servers
3. To start sending messages, run the client files by typing > py ./xxx_client.py
4. Type destination as uppercase 3 character airport code (example: ANC,SEA,OTZ etc.)
5. Type a name or whatever message you want to send
6. Now you can see in your destination server the message that was sent
7. It is possible to end the server processes by running the Dummy Client and sending !END_SERVER twice to the target server you want to close
8. to close the clients, type . then hit enter twice
More information in YouTube video linked in  iii)

i) I did a test run using the passenger list in the logs folder.  The server logs appear in the logs folder as well.

ii) The goal for writing code for this project was to not have to write server's or clients more than once which is why I spent time making sure the server and client classes worked well with the network I was building.
The server and client class code can be found in the libs folder.  Each client and server file calls these objects and passes them specific paramteres about which airport is using them.  If configuring my files to work
with classes was step 1, step 2 was figuring out how to communicate and forward messages between clients and servers.  At first I tried to have a server forward a message to a client with an open connection to the server but I
realized socket does not really like this and its too hard.  So i figured that each airport shall have a client and a server.  The client sends out messages to servers, and servers either forward that message to another server
or save the information received from the client.  Servers and clients have hardcoded parameters telling them which servers they can or cannot connect to.  This was a key part of my design and I put a lot of checks in for it.  

My submission meets every aspect desired from this assignment.  I have a few hubs like ANC and SEA who provide layovers.  Smaller airports that are only connected to ANC.  The system runs as a client-server architecture.
The system seamlessly transfers passenger information, with options to scale that information easily.  Hub servers like ANC route traffic to and from smaller airports.  What I am happy about with this code was its scalability.
In testing I wiuld use only 2 or 3 airports to test my code.  And once I got that working, it was very easy to scale up.  I even added PDX to my model to demonstrate the scalability of the code in this project.

iii) I uploaded a video to YouTube of me running the programs: https://www.youtube.com/watch?v=km9C_vZvr0A

Thoughts/Reflections/Assumptions

I think this simulation reflects how internet traffic works in how the larger hubs like ANC and SEA have much more traffic flowing into them, and through them than smaller 'airports'.
Like IXP's, they need to be configured in a way that allows them to prefrom these actions.  IXP's are more powerful routing ASes than normal, and in this assignment I initialize SEA and
ANC with larger accetping arrays which kind of mimics the greater power IXP's have in the internet.  In my project for this class we are learning about border gateway protocol.  I want
to draw the parallel of BGP to how ANC server works.  Anchorage's server holds information about how to send information to FAI, and OTZ does not.  This is where BGP would 
come into play and allow OTZ route to FAI via the routing information stored in Anchorage.  I kind of used a DNS for this as well, one of the first things I did was try and think
of a way to store airport information alongside server host and port information.  I solved this by creating an AirportCode class (in the libs folder) that stores this information.
Every connection, message sent, and message forwarded uses this lookup system.  It was much easier to keep track of airport codes instead of port numbers when coding this excercise.
Of course I had each server and client store this information locally by importing the class, but it functions similar to how a DNS might as it is a central authority for the naming
scheme used in this assignment.  The system architecture was designed with the hub and spoke topology in mind, I also tried to think of it how email's are sent.  We connect to a server,
that server determines if it can connect to the destination, if it does, then it sends the message.  I found that in socket client's don't do well with receiving informatio, it is hard
for a server to have a consistent connection to a particular client.  I shifted my effort to thinking of the client/server relationship in this excersise as clients being the depature terminal
and servers being the arrivals/connections terminal in an airport.  








