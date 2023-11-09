package core

import (
	"context"
	"log"
	"sync"
	"time"

	"github.com/segmentio/kafka-go"
)

func CreateProducer(hosts []string, topic string) *kafka.Writer {
	w := &kafka.Writer{
		Addr:                   kafka.TCP(hosts...),
		Topic:                  topic,
		RequiredAcks:           1,
		AllowAutoTopicCreation: false,
		BatchSize:              100,
		BatchBytes:             10485760,
		BatchTimeout:           200 * time.Millisecond,
		// Logger
	}

	return w
}

func ProduceMesssage(w *kafka.Writer, msgCh chan map[string]string, wg *sync.WaitGroup) {
	log.Println("Start Producing")
	defer wg.Done()
	for {
		// Get Message
		rawMsg := <-msgCh
		msg := kafka.Message{
			Key:   []byte(rawMsg["key"]),
			Value: []byte(string(rawMsg["value"])),
		}
		log.Printf("Kafka Consumer : Successfully Consumed Message, Current Messages in Channel %v", len(msgCh))
		ctx := context.Background()
		err := w.WriteMessages(ctx, msg)
		if err != nil {
			log.Printf("Unexpected Error %v\n", err)
		}
		rawMsg = nil
	}
}
