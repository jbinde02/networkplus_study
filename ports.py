import random

port_dict = {
    "FTP":{
        "port/s": (20,21),
        "spelled_out": "File Transfer Protocol",
        "definition": "Used in the transfer of files from a server to a client over a network. Authentication in plain-text.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "SFTP":{
        "port/s": 22,
        "spelled_out": "Secure File Transfer Protocol",
        "definition": "Like FTP but was designed as an extension of SSH (Secure Shell) to provide for secure file transfer.",
        "primary_layer_4_protocol/s": ""
    },
    "SSH":{
        "port/s": 22,
        "spelled_out": "Secure Shell",
        "definition": "Encrypted networking protocol designed for operating network services over an unsecure network. Notable applications include remote login and command-line execution.",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "Telnet":{
        "port/s": 23,
        "spelled_out": "Telecommunications Network",
        "definition": "Provides access to virtual terminals of remote systems over a network. Transmits all information in plain-text.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "SMTP":{
        "port/s": 25,
        "spelled_out": "Simple Mail Transfer Protocol",
        "definition": "Internet standard protocol for email transmission. Used by servers for send and receive while clients only use for sending to mail server.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "DNS":{
        "port/s": 53,
        "spelled_out": "Domain Name System",
        "definition": "Hierarchical and distributed directory service primarly for translating domain names to IP addresses.",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "DHCP":{
        "port/s": (67,68),
        "spelled_out": "Dynamic Host Configuration Protocol",
        "definition": "Distributes IP addresses and other parameters to devices connected to a network automatically.",
        "primary_layer_4_protocol/s": "UDP"
    },
    "TFTP":{
        "port/s": 69,
        "spelled_out": "Trivial File Transfer Protocol",
        "definition": "Like FTP but uses UDP. Very simple to implemenet.",
        "primary_layer_4_protocol/s": "UDP"
    },
    "HTTP":{
        "port/s": 80,
        "spelled_out": "Hypertext Transfer Protocol",
        "definition": "Foundation for data communication on the World Wide Web. Request-response protocol in a client-server model where the client sends a request to the server and the server provides a resource or performs an action on behalf of the client.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "POP3":{
        "port/s": 110,
        "spelled_out": "Post Office Protocol version 3",
        "definition": "Internet Standard protocol for clients retrieving emails from a mail server. Gets all messages from the server, stores them locally, and deletes them from the server.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "NTP":{
        "port/s": 123,
        "spelled_out": "Network Time Protocol",
        "definition": "Hierarchical system for providing clock synchronization between computers over a packet-switched, variable-latency network.",
        "primary_layer_4_protocol/s": "UDP"
    },
    "NetBios":{
        "port/s": (137,138,139),
        "spelled_out": "Network Basic Input/Output System",
        "definition": "Provides services releated to the session layer (5) allowing applications on serparate computers to communicate over a LAN. Has a name service (NetBIOS-NS) for name registration and resolution, a datagram distribution service (NetBIOS-DGM) for connectionless communication, and a session service (NetBIOS-SSN) for connection-oriented communication.",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "IMAP":{
        "port/s": 143,
        "spelled_out": "Internet Message Access Protocol",
        "definition": "Internet Standard protocol for clients retrieving emails from a mail server. Messages are left on the server until the user explicity deltes them.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "SNMP":{
        "port/s": (161,162),
        "spelled_out": "Simple Network Management Protocol",
        "definition": "Internet standard protocol for collecting and organizing information about managed devices on a network. Also can be used to modify device behavior and set event triggered messages called traps.",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "LDAP":{
        "port/s": 389,
        "spelled_out": "Lightweight Directory Access Protocol",
        "definition": "Open and vendor-neutral protocol for accessing and mainting distributed directory information services over an network. These services map names of network resources to network addresses",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "HTTPS":{
        "port/s": 443,
        "spelled_out": "Hypertext Transfer Protocol Secure (HTTPS)",
        "definition": "Extension of HTTP that implements encryption using Transport Layer Security (TLS), formerly, Secure Sockets Layer (SSL).",
        "primary_layer_4_protocol/s": "TCP and UDP"
    },
    "SMB":{
        "port/s": 445,
        "spelled_out": "Server Message Block",
        "definition": "Enables file sharing, printer sharing, network browsing, and inter-process communication over a network.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "Syslog":{
        "port/s": 514,
        "spelled_out": "Syslog",
        "definition": "Standard for message logging that separates the system that generates messages, the system that stores messages, and the system that reports/analyzes on messages.",
        "primary_layer_4_protocol/s": "UDP"
    },
    "SMTPS":{
        "port/s": 587,
        "spelled_out": "Simple Mail Transfer Protocol Secure",
        "definition": "Secure version of SMTP that uses TLS. Traditionally used on port 465 but is used on a different port when using STARTTLS encryption.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "LDAPS":{
        "port/s": 636,
        "spelled_out": "Lightweight Directory Access Protocol over SSL",
        "definition": "Extends LDAP by integrating it with TLS/SSL.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "IMAPS":{
        "port/s": 993,
        "spelled_out": "Internet Message Access Protocol over TLS/SSL",
        "definition": "Extends IMAP by integrating it with TLS/SSL.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "POP3S":{
        "port/s": 995,
        "spelled_out": "Post Office Protocol 3 over TLS/SSL",
        "definition": "Extends POP3 by integrating it with TLS/SSL.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "SQL Server":{
        "port/s": 1433,
        "spelled_out": "Microsoft Structured Query Language Server",
        "definition": "Microsoft SQL Server database management system.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "Oracle Database":{
        "port/s": 1521,
        "spelled_out": "Oracle Database",
        "definition": "Oracle database management system and Oracle Autonomous Database are also names for this DBMS service.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "RADIUS":{
        "port/s": (1812, 1813),
        "spelled_out": "Remote Authentication Dial-In User Service",
        "definition": "Provides centralized authentication, authorization, and accounting (AAA) for users connected to a network. Often the back-end for 802.1X authentication.",
        "primary_layer_4_protocol/s": "UDP"
    },
    "MySQL":{
        "port/s": 3306,
        "spelled_out": "MySQL",
        "definition": "Open-source SQL database management system.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "MariaDB":{
        "port/s": 3306,
        "spelled_out": "MariaDB",
        "definition": "Open source fork of MySQL",
        "primary_layer_4_protocol/s": "TCP"
    },
    "RDP":{
        "port/s": 3389,
        "spelled_out": "Remote Desktop Protocol",
        "definition": "Also known as Terminal Services, this service allows users to create and control an interactive session on a remote computer or virtual machine over a network.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "SIP":{
        "port/s": (5060, 5061),
        "spelled_out": "Session Initiation Protocol",
        "definition": "Used for initiating, maintaining, and terminating communication sessions that include voice, video, and messaging applications. Often used in VoIP and mobile phone calling over LTE.",
        "primary_layer_4_protocol/s": "TCP, UDP, and SCTP"
    },
    "PostgreSQL":{
        "port/s": 5432,
        "spelled_out": "POSTGRES SQL",
        "definition": "Open-source SQL database management system.",
        "primary_layer_4_protocol/s": "TCP"
    },
    "IBM Db2":{
        "port/s": 50000,
        "spelled_out": "IBM Db2",
        "definition": "Family of data management products including a database management system. Newer versions use port 25000 to stay out of the ephemeral port range.",
        "primary_layer_4_protocol/s": "TCP"
    }
}

if __name__ == "__main__":
    print("Type in the port number/s associated with each protocol or service."\
    "\nIf multiple ports are required use spaces, periods, or commas to delimit them."\
    "\nType hint to get a range for the port number in lengths of 100."\
    "\nType define to get the name spelled out, the definition, and the layer 4 protocol typically used with the protocol or service."\
    "\nType skip to go to another random question."\
    "\nType quit to end the program.\n")
    port_dict_keys = list(port_dict.keys())
    quit = False
    while True:
        if quit:
            break
        random_service = port_dict_keys[random.randint(0, len(port_dict_keys)-1)]
        ports = port_dict[random_service]["port/s"]
        print(f"What is the port number for {random_service}")
        while True:
            x = input()
            y = None
            
            if not x:
                continue
            if x.lower() == "skip":
                print("Skipping to next")
                break
            elif x.lower() == "define":
                print(f'{port_dict[random_service]["spelled_out"]} : {port_dict[random_service]["primary_layer_4_protocol/s"]} : {port_dict[random_service]["definition"]}')
                continue
            elif x.lower() == "hint":
                if type(ports) is tuple:
                    print(f'{ports[0]//100*100} - {(ports[0]//100*100) + 100}')
                else:
                    print(f'{ports//100*100} - {(ports//100*100) + 100}') # type: ignore
                continue
            elif x.lower() == "quit":
                quit = True
                break
            
            try:
                if "," in x:
                    x, y = x.split(",")
                    x = int(x.strip())
                    y = int(y.strip())
                elif "." in x:
                    x, y = x.split(".")
                    x = int(x.strip())
                    y = int(y.strip())
                elif " " in x:
                    x, y = x.split(" ")
                    x = int(x.strip())
                    y = int(y.strip())
                else:
                    x = int(x.strip())
            except:
                print("Invalid input")
                continue

            if type(ports) is tuple:
                if (x and y):
                    if x == ports[0]:
                        if y == ports[1]:
                            print("Correct!")
                            break
                        else:
                            print(f"Second port is wrong. Difference is {abs(y - ports[1])}")
                    else:
                        print(f"First port is wrong. Difference is {abs(x - ports[0])}")
                elif len(ports) == 2:
                    print("Need two ports in answer")
            else:
                if x == ports:
                    print("Correct!")
                    break
                else:
                    print(f"Wrong. Difference is {abs(x - ports)}") # type: ignore
            continue

