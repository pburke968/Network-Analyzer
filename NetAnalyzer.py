#
#
#           Hello, this is my first Python project. I am building a network analyser. Essentially the goal is to have splash screen that gives you the option to run a network speed test(using Ookla's speedtest)
#           or monitor your network to identify any anomilies (e.g. high ping, high packet loss)
#

import speedtest
from icmplib import ping

def main():
    uip = int(input(''' What would you like to do?
                    1) Speedtest
                    2) Monitor network connectivity
                    
                    Your Choice: '''))
    if uip == 1:
           speed()

    elif uip == 2:
            monitor()

    else:
        print(f"Please select a valid option")
        main()
        

def speed():
        st = speedtest.Speedtest()
        print("Performing a ping test to identify the best server...")
        server = st.get_best_server()

        print("Testing Download Speeds...")
        dl = st.download() / 1_000_000

        print("Testing Upload Speeds...")
        ul = st.upload() / 1_000_000

        print("Testing Ping...")
        ping = st.results.ping

        print(f"Server: {server['name']}")
        print(f"Download Speeds: {dl:.2f}/Mbps")
        print(f"Upload Speeds: {ul:.2f}/Mbps")
        print(f"Ping Results: {ping:.2f}/ms")

def monitor():
    uip = int(input(''' What would you like to do?
                    1) Google
                    2) Cloudfare
                    
                    Your Choice: '''))
    if uip == 1:
           googleping()

    elif uip == 2:
            cloudfareping()

    else:
        print("Please select a valid option")
        monitor()

def googleping():
        ping_history = []
        packet_history = []
        while True:
              print()
              result = ping("8.8.8.8")
              ping_history.append(result.avg_rtt)
              packet_history.append(result.packet_loss)
              pingavg = sum(ping_history)/len(ping_history)
              packetavg = sum(packet_history)/len(packet_history)
              print(f"Current Ping: {result.avg_rtt:.2f} ms -- Current Packet Loss: {result.packet_loss:.2f}")
              print(f"Average Ping: {pingavg:.2f} ms -- Average Packet Loss: {packetavg:.2f}")

        if result.avg_rtt > pingavg * 1.25:
                print(f"ALERT HIGH PING: {result.avg_rtt:.2f} -- PING AVG: {pingavg:.2f} ")
        else: 
                pass
              
        if result.packet_loss > 0:
                print(f"ALERT PACKET LOSS: {result.packet_loss:.2f}")
        else: 
                pass

def cloudfareping():
        ping_history = []
        packet_history = []
        while True:
              print()
              result = ping("1.1.1.1")
              ping_history.append(result.avg_rtt)
              packet_history.append(result.packet_loss)
              pingavg = sum(ping_history)/len(ping_history)
              packetavg = sum(packet_history)/len(packet_history)
              print(f"Current Ping: {result.avg_rtt:.2f} ms -- Current Packet Loss: {result.packet_loss:.2f}")
              print(f"Average Ping: {pingavg:.2f} ms -- Average Packet Loss: {packetavg:.2f}")

        if result.avg_rtt > pingavg * 1.25:
                print(f"ALERT HIGH PING: {result.avg_rtt:.2f} -- PING AVG: {pingavg:.2f} ")
        else: 
                pass
              
        if result.packet_loss > 0:
                print(f"ALERT PACKET LOSS: {result.packet_loss:.2f}")
        else: 
                pass

main()