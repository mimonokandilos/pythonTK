package main

import (
	"log"
	"os/exec"
)

func main() {
	url := "https://www.google.com"

	cmd := exec.Command("open", url) // For macOS
	// cmd := exec.Command("xdg-open", url) // For Linux
	// cmd := exec.Command("start", url) // For Windows

	err := cmd.Start()
	if err != nil {
		log.Fatal(err)
	}
}

