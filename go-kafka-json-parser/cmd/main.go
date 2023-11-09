package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"os/signal"
	"strings"
	"sync"
	"syscall"

	config "github.com/go-kafka-json-parser/config"
	core "github.com/go-kafka-json-parser/core"
	"github.com/segmentio/kafka-go"
)

func main() {

	prodNum := flag.Int("producer", 15, "Producer Number")
	conNum := flag.Int("consumer", 9, "Consumer Number")
	parserNum := flag.Int("parser", 15, "Parser Number")
	hostArg := flag.String("host", "localhost:9092,localhost:9093,localhost:9094", "List of Hosts, delemited with comma")
	fromTopic := flag.String("fromTopic", config.FromTopic, "Topic to Consume")
	toTopic := flag.String("toTopic", config.ToTopic, "Topic to Produce")
	flag.Parse()

	hosts := strings.Split(*hostArg, ",")

	fmt.Printf("Producer : %v \nConsumer : %v \nParser : %v \nHosts: %v \nFrom Topic : %v \nTo Topic: %v \n", prodNum, conNum, parserNum, hostArg, fromTopic, toTopic)

	var consumers = []*kafka.Reader{}
	var producers = []*kafka.Writer{}

	wg := sync.WaitGroup{}

	// Create Channel
	strCh := make(chan string, 1000)
	msgCh := make(chan map[string]string, 1000)
	end := make(chan os.Signal, 1)

	// create Consumer Group
	for i := 0; i < *conNum; i++ {
		consumers = append(consumers, core.CreateConsumerGroup(hosts, *fromTopic, config.GroupName))
	}
	log.Printf("Created Consumers, Total : %v\n", len(consumers))

	// create Writers
	for i := 0; i < *prodNum; i++ {
		producers = append(producers, core.CreateProducer(hosts, *toTopic))
	}
	log.Printf("Created Writers, Total : %v\n", len(producers))

	// start Consuming
	for _, consumer := range consumers {
		wg.Add(1)
		log.Println("Start Consuming")
		go core.ConsumeGroup(consumer, strCh, &wg)
	}

	// Start Parsing

	for i := 0; i < *parserNum; i++ {
		log.Println("Start Parsing")
		wg.Add(1)
		go core.ParseJson(strCh, msgCh, &wg)
	}

	// Start Producing

	for _, producer := range producers {
		wg.Add(1)
		log.Println("Start Producing")
		go core.ProduceMesssage(producer, msgCh, &wg)
	}

	wg.Wait()

	// Capture Ctrl C
	signal.Notify(end, syscall.SIGINT, syscall.SIGTERM)
	go func() {
		<-end
		for _, consumer := range consumers {
			consumer.Close()
		}
		for _, producer := range producers {
			producer.Close()
		}
	}()
	defer fmt.Println("Finished")
}
