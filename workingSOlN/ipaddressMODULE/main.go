package main

import (
    "fmt"
    "net"
)

func main() {
    // Specify the network interface name for which you want to get the IP address
    interfaceName := "en0" // Change this to your desired interface name

    // Get a list of network interfaces
    interfaces, err := net.Interfaces()
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    // Find the specified network interface
    var selectedInterface net.Interface
    for _, iface := range interfaces {
        if iface.Name == interfaceName {
            selectedInterface = iface
            break
        }
    }

    // If the selected interface was found, retrieve its IP addresses
    if selectedInterface.Name != "" {
        addrs, err := selectedInterface.Addrs()
        if err != nil {
            fmt.Println("Error:", err)
            return
        }

        fmt.Println("IP addresses for", selectedInterface.Name)
        for _, addr := range addrs {
            ipNet, ok := addr.(*net.IPNet)
            if ok && !ipNet.IP.IsLoopback() {
                fmt.Println("IP:", ipNet.IP)
            }
        }
    } else {
        fmt.Println("Interface not found:", interfaceName)
    }
}
