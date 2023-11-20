package core

import (
	"fmt"
	"log"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/clarketm/json"
	"github.com/go-kafka-json-parser/config"
)

var targetField = []string{config.NameKey, config.IndexKey}

const ()

// Parse JsonString and return UnMarshaled Map
func parseString(str string) (error, map[string]interface{}) {
	var j map[string]interface{}
	if err := json.Unmarshal([]byte(str), &j); err != nil {
		return fmt.Errorf("cannot parse jsonMap"), nil
	}
	return nil, j
}

// Check if the key exists in the Map
func checkField(field map[string]interface{}, key string) error {
	_, ok := field[key]
	if !ok {
		return fmt.Errorf("no such field %v", strings.ToLower(key))
	}
	return nil
}

// Get Metadata from JsonMap, If the JsonMap doesn't have the keys, the time and site will be 0
func extractMetaData(j map[string]interface{}, headerKey, timeKey, siteKey string) [2]int64 {
	var res [2]int64

	if err := checkField(j, headerKey); err != nil {
		log.Printf("Cannot Find %v in JsonMap", headerKey)
		return [2]int64{0, 0}
	}

	tmp := j[headerKey].(map[string]interface{})

	if time, err := time.Parse(config.TimeFormat, tmp[timeKey].(string)); err != nil {
		log.Printf("Error in Parsing Time %v\n", err)
		res[0] = 0
	} else {
		res[0] = time.Unix()
	}

	if siteId, err := strconv.Atoi(tmp[siteKey].(string)); err != nil {
		log.Printf("Error in Parse %v", err)
		res[1] = 0
	} else {
		res[1] = int64(siteId)
	}

	return res
}

// Extract Data from Single Big Map and return into []interface{}
func extractFieldsFromJsonString(j map[string]interface{}, key string) (error, []interface{}) {
	var res = make([]interface{}, 0, config.MemKB)

	if err := checkField(j, key); err != nil {
		return fmt.Errorf("error in parse fields"), nil
	}

	for _, val := range j[key].(map[string]interface{}) {
		res = append(res, val)
	}

	return nil, res
}

// Extract Field
func extractDataFromSlice(j []interface{}, msgCh chan map[string]string, metadata [2]int64) error {

	// j = Arrays of Fields
	for _, val := range j {

		field, ok := val.(map[string]interface{})
		if !ok {
			return fmt.Errorf("error in convert field into map")
		}

		service, ok := field[config.ServiceKey].([]interface{})
		if !ok {
			return fmt.Errorf("error in convert field")
		}

		for _, sensor := range service {
			valMap := make(map[string]interface{}, config.MemKB)
			resMap := make(map[string]string, config.MemKB)
			// Insert Tag Data
			for _, key := range targetField {
				if err := checkField(field, key); err != nil {
					log.Printf("no such field in fields %v, set into 0\n", key)
					valMap[key] = 0
				} else {
					if key == config.IndexKey {
						valMap[key] = fmt.Sprintf("%v%v", "field", field[key])
					} else {
						valMap[key] = field[key]
					}
				}
			}

			// Insert Metadata
			valMap[config.TimeKey] = metadata[0]
			valMap[config.SiteKey] = fmt.Sprintf("%v%v", "site", metadata[1])

			checkField(field, config.ServiceKey)

			sensor, ok := sensor.(map[string]interface{})
			if !ok {
				log.Printf("error in convert sensor into map\n")
				continue
			}

			for key, val := range sensor {
				// If value type is not Atomic, Skip
				if reflect.TypeOf(val) == reflect.TypeOf(sensor) {
					continue
				}

				// Need to Distinguish Each Sensor
				if key == config.IndexKey || key == config.IdKey {
					valMap[config.ServiceKey] = val
					continue
				}
				valMap[key] = val
			}

			if err := checkField(valMap, config.ServiceKey); err != nil {
				log.Printf("no such field in fields %v, set into 0\n", config.ServiceKey)
				valMap[config.ServiceKey] = 0
			}
			// Generate Key
			key := fmt.Sprintf("%v-%v-%v-%v", valMap[config.TimeKey], valMap[config.SiteKey], valMap[config.IndexKey], valMap[config.ServiceKey])

			resMap["key"] = key
			resMap["value"] = convertMapToString(valMap)

			// Insert Into Channel
			msgCh <- resMap

			log.Printf("Json Parser : Successfully Parsed Message, Current Messages in Channel %v", len(msgCh))
		}
	}
	return nil
}

func convertMapToString(valMap map[string]interface{}) string {
	// Convert Map into Json
	jsonByte, err := json.Marshal(valMap)
	if err != nil {
		log.Println("Error in Marshal Map into Json")
		return ""
	}
	// Convert to String
	jsonString := string(jsonByte)
	return jsonString
}

func ParseJson(ch chan string, msgCh chan map[string]string, wg *sync.WaitGroup) {
	log.Println("Start Parsing")
	var str string
	defer wg.Done()
	for {
		// Get Message
		str = <-ch
		// Convert Raw String into Map
		err, jsonMap := parseString(str)
		if err != nil {
			log.Println("Cannot Parse Json Message")
			continue
		}
		// Parse Metadata from Map
		metadata := extractMetaData(jsonMap, config.HeaderKey, config.TimeKey, config.SiteKey)
		// Get Field Data from Map
		err, fieldSlice := extractFieldsFromJsonString(jsonMap, config.FieldKey)
		if err != nil {
			log.Println("Cannot Extract Field from JsonMap")
			continue
		}
		// Parse Maps in Slice and Insert Msg into Channel
		err = extractDataFromSlice(fieldSlice, msgCh, metadata)
		if err != nil {
			log.Println("Cannot Extract Data from Fields")
			continue
		}
	}
}
