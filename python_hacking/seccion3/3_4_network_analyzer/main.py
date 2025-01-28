from network_analyzer import NetworkAnalyzer


if __name__=="__main__":
    analyzer = NetworkAnalyzer("192.168.126.132/24")
    hosts_up = analyzer.hosts_scan_arp()
    analyzer.pretty_print(hosts_up)