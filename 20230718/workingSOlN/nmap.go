package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	ipAddress := "172.17.16.1" // Replace this with the IP address you want to scan

	// Create the Nmap command with the desired options
	nmapCmd := exec.Command("nmap", "-p", "1-100", ipAddress) // Replace "1-100" with the desired range of ports

	// Run the Nmap command and capture its output
	output, err := nmapCmd.Output()
	if err != nil {
		log.Fatalf("failed to run nmap scan: %v", err)
	}

	// Display the Nmap scan results
	fmt.Printf("Nmap scan results for %s:\n", ipAddress)
	fmt.Println(string(output))
}

