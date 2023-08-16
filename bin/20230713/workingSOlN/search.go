package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func searchFileForKeyword(filePath string, keyword string) ([]string, error) {
	var results []string

	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lineNumber := 1

	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, keyword) {
			absPath, err := filepath.Abs(filePath)
			if err != nil {
				return nil, err
			}

			result := fmt.Sprintf("Keyword found in file: %v - Filename: %v - Line %d: %s", true, filepath.Base(filePath), lineNumber, absPath)
			results = append(results, result)
		}
		lineNumber++
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return results, nil
}

func searchFilesInDirectory(dirPath string, keyword string) ([]string, error) {
	var results []string

	err := filepath.Walk(dirPath, func(filePath string, info os.FileInfo, err error) error {
		if err != nil {
			// Handle error accessing file or directory
			return filepath.SkipDir // Skip the current directory and proceed to the next one
		}

		if !info.IsDir() {
			fileResults, err := searchFileForKeyword(filePath, keyword)
			if err != nil {
				return err
			}
			results = append(results, fileResults...)
		}
		return nil
	})

	if err != nil {
		return nil, err
	}

	return results, nil
}

func main() {
	keyword := os.Args[1] // Get the keyword from command-line argument
	dirPath := "/Users/mikemonokandilos/TESTING"

	results, err := searchFilesInDirectory(dirPath, keyword)
	if err != nil {
		log.Fatal(err)
	}

	if len(results) == 0 {
		fmt.Println("No results found.")
	} else {
		for _, result := range results {
			fmt.Println(result)
		}
	}
}

