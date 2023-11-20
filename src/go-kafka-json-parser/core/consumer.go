package core

import (
	"context"
	"log"
	"sync"
	"time"

	"github.com/segmentio/kafka-go"
)

// Create Consumer Group
func CreateConsumerGroup(hosts []string, topic string, groupId string) *kafka.Reader {
	r := kafka.NewReader(kafka.ReaderConfig{
		Brokers:        hosts,
		Topic:          topic,
		GroupID:        groupId,
		MinBytes:       10e3,                   // 10KB
		MaxBytes:       50e6,                   // 50MB
		CommitInterval: 500 * time.Millisecond, // flushes commits to Kafka every second
	})

	return r
}

// Consume as a Group Member
func ConsumeGroup(r *kafka.Reader, ch chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for {
		m, err := r.ReadMessage(context.Background())
		if err != nil {
			log.Fatalf("Error in Consuming Message, %v", err)
			break
		}
		log.Printf("Kafka Consumer : Successfully Consumed Message, Current Messages in Channel %v", len(ch))
		ch <- string(m.Value)
	}
}
