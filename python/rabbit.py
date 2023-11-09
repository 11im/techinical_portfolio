import pika
import time
import schedule
from datetime import datetime


data = {
    "header": {
            "site_id": "000001",
            "EnergyPlatformLayer": 1,
            "FieldDeviceLayer": 6,
            "timestamp": datetime.datetime.strptime(time.time(), '%Y-%m-%d %H:%M:%SZ')
    },
    "EnergyPlatformLayer": {
            "Name": "Mirae building Microgrid",
            "Protocol": "AMQP-0-9-1",
            "Security": "SSL/TLS1.3",
            "Cipher Algorithm": "AES256_GCM",
            "Routing key": "abcd"
    },
    "FieldDeviceLayer": {
            "field1": {
                    "index": 1,
                    "Name": "Battery",
                    "component": {
                            "Device1": "Rack",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01",
                            "id2": "02",
                            "id3": "03"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "StorageDevice",
                                    "role2": "ControlDevice"
                            }
                    },
                    "service": [
                            {
                                    "id": "01",
                                    "communication_error": false,
                                    "stop": false,
                                    "run": true,
                                    "charge": false,
                                    "discharge": true,
                                    "warning": false,
                                    "fault": false,
                                    "total_racks": 1,
                                    "soc": 31.5,
                                    "soh": 100.0,
                                    "dc_voltage": 733.4,
                                    "dc_current": 14.0,
                                    "max_cell_voltage": 3.6,
                                    "min_cell_voltage": 3.6,
                                    "max_module_temperature": 32.7,
                                    "min_module_temperature": 28.7,
                                    "racks": {
                                            "index": 1,
                                            "communication_error": false,
                                            "stop": false,
                                            "run": true,
                                            "charge": false,
                                            "discharge": true,
                                            "warning": false,
                                            "fault": false,
                                            "soc": 31.5,
                                            "soh": 100.0,
                                            "dc_voltage": 733.4,
                                            "dc_current": 13.3,
                                            "max_cell_voltage": 3.6,
                                            "min_cell_voltage": 3.6,
                                            "max_module_temperature": 32.7,
                                            "min_module_temperature": 28.7
                                    }
                            },
                            {
                                    "id": "02",
                                    "communication_error": false,
                                    "stop": false,
                                    "run": true,
                                    "charge": false,
                                    "discharge": true,
                                    "warning": false,
                                    "fault": false,
                                    "total_racks": 1,
                                    "soc": 31.2,
                                    "soh": 100.0,
                                    "dc_voltage": 734.5,
                                    "dc_current": 12.7,
                                    "max_cell_voltage": 3.6,
                                    "min_cell_voltage": 3.6,
                                    "max_module_temperature": 33.2,
                                    "min_module_temperature": 28.5,
                                    "racks": {
                                            "index": 1,
                                            "communication_error": false,
                                            "stop": false,
                                            "run": true,
                                            "charge": false,
                                            "discharge": true,
                                            "warning": false,
                                            "fault": false,
                                            "soc": 31.2,
                                            "soh": 100.0,
                                            "dc_voltage": 734.5,
                                            "dc_current": 12.7,
                                            "max_cell_voltage": 3.6,
                                            "min_cell_voltage": 3.6,
                                            "max_module_temperature": 33.2,
                                            "min_module_temperature": 28.5
                                    }
                            },
                            {
                                    "id": "03",
                                    "communication_error": false,
                                    "stop": false,
                                    "run": true,
                                    "charge": false,
                                    "discharge": true,
                                    "warning": false,
                                    "fault": false,
                                    "total_racks": 1,
                                    "soc": 31.4,
                                    "soh": 100.0,
                                    "dc_voltage": 733.4,
                                    "dc_current": 13.6,
                                    "max_cell_voltage": 3.6,
                                    "min_cell_voltage": 3.6,
                                    "max_module_temperature": 29.1,
                                    "min_module_temperature": 24.6,
                                    "racks": {
                                            "index": 1,
                                            "communication_error": false,
                                            "stop": false,
                                            "run": true,
                                            "charge": false,
                                            "discharge": true,
                                            "warning": false,
                                            "fault": false,
                                            "soc": 31.4,
                                            "soh": 100.0,
                                            "dc_voltage": 733.4,
                                            "dc_current": 13.6,
                                            "max_cell_voltage": 3.6,
                                            "min_cell_voltage": 3.6,
                                            "max_module_temperature": 32.7,
                                            "min_module_temperature": 28.6
                                    }
                            }
                    ]
            },
            "field2": {
                    "index": 2,
                    "Name": "DC/DC_Convertor",
                    "component": {
                            "Device1": "Controller",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01",
                            "id2": "02",
                            "id3": "03"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "LoadDevice",
                                    "role2": "ControlDevice",
                                    "role3": "GensetDevice"
                            }
                    },
                    "service": [
                            {
                                    "index": 1,
                                    "communication_error": false,
                                    "stop": false,
                                    "run": true,
                                    "charge": false,
                                    "discharge": true,
                                    "warning": false,
                                    "fault": false,
                                    "frequency": 60.0,
                                    "ac_active_power": 18.5,
                                    "igbt_max_temperature": 32.0,
                                    "ac_voltage_rs": 433.0,
                                    "ac_voltage_st": 436.0,
                                    "ac_voltage_tr": 432.0,
                                    "ac_current_r": 25.0,
                                    "ac_current_s": 25.0,
                                    "ac_current_t": 23.0,
                                    "dc_voltage": 751.0,
                                    "dc_current": 26.0
                            },
                            {
                                    "index": 2,
                                    "communication_error": false,
                                    "stop": false,
                                    "run": true,
                                    "charge": false,
                                    "discharge": true,
                                    "warning": false,
                                    "fault": false,
                                    "frequency": 60.0,
                                    "ac_active_power": 9.0,
                                    "igbt_max_temperature": 28.0,
                                    "ac_voltage_rs": 432.0,
                                    "ac_voltage_st": 436.0,
                                    "ac_voltage_tr": 431.0,
                                    "ac_current_r": 13.0,
                                    "ac_current_s": 13.0,
                                    "ac_current_t": 11.0,
                                    "dc_voltage": 750.0,
                                    "dc_current": 9.0
                            },
                            {
                                    "index": 3,
                                    "communication_error": false,
                                    "stop": false,
                                    "run": false,
                                    "charge": false,
                                    "discharge": false,
                                    "warning": false,
                                    "fault": false,
                                    "frequency": 60.03,
                                    "ac_active_power": 222.2,
                                    "igbt_max_temperature": 56.4,
                                    "ac_voltage_rs": 381.2,
                                    "ac_voltage_st": 382.2,
                                    "ac_voltage_tr": 380.1,
                                    "ac_current_r": 888.8,
                                    "ac_current_s": 888.8,
                                    "ac_current_t": 888.8,
                                    "dc_voltage": 890.4,
                                    "dc_current": 432.1
                            }
                    ]
            },
            "field3": {
                    "index": 3,
                    "Name": "AC/DC_Invertor",
                    "component": {
                            "Device1": "Controller",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01",
                            "id2": "02"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "LoadDevice",
                                    "role2": "ControlDevice",
                                    "role3": "GensetDevice"
                            }
                    },
                    "service": [
                            {
                                    "index": 1,
                                    "AC_ACTIVE": 18.5,
                                    "AC_CNT1": 25.0,
                                    "AC_CNT2": 25.0,
                                    "AC_CNT3": 23.0,
                                    "AC_FREQ": 60.0,
                                    "AC_REACTIVE": 0.7,
                                    "AC_VOLT1": 433.0,
                                    "AC_VOLT2": 436.0,
                                    "AC_VOLT3": 432.0,
                                    "COMM_FAULT": 0.0,
                                    "COMM_WARN": 0.0,
                                    "DC_CURRENT": 26.0,
                                    "DC_POWER": 19.0,
                                    "DC_VOLTAGE": 751.0,
                                    "FAULT1": 0.0,
                                    "FAULT2": 0.0,
                                    "FAULT3": 0.0,
                                    "FAULT4": 0.0,
                                    "FAULT5": 0.0,
                                    "FAULT6": 0.0,
                                    "FAULT7": 0.0,
                                    "FAULT8": 0.0,
                                    "FAULT9": 0.0,
                                    "IGBT_TEMP1": 32.0,
                                    "IGBT_TEMP2": 30.0,
                                    "IGBT_TEMP3": 27.0,
                                    "WARN1": 0.0,
                                    "WARN2": 0.0
                            },
                            {
                                    "index": 2,
                                    "AC_ACTIVE": 9.0,
                                    "AC_CNT1": 13.0,
                                    "AC_CNT2": 13.0,
                                    "AC_CNT3": 11.0,
                                    "AC_FREQ": 60.0,
                                    "AC_REACTIVE": 0.3,
                                    "AC_VOLT1": 432.0,
                                    "AC_VOLT2": 436.0,
                                    "AC_VOLT3": 431.0,
                                    "COMM_FAULT": 0.0,
                                    "COMM_WARN": 0.0,
                                    "DC_CURRENT": 13.0,
                                    "DC_POWER": 9.0,
                                    "DC_VOLTAGE": 750.0,
                                    "FAULT1": 0.0,
                                    "FAULT2": 0.0,
                                    "FAULT3": 0.0,
                                    "FAULT4": 0.0,
                                    "FAULT5": 0.0,
                                    "FAULT6": 0.0,
                                    "FAULT7": 0.0,
                                    "FAULT8": 0.0,
                                    "FAULT9": 0.0,
                                    "IGBT_TEMP1": 28.0,
                                    "IGBT_TEMP2": 26.0,
                                    "IGBT_TEMP3": 25.0,
                                    "WARN1": 0.0,
                                    "WARN2": 0.0
                            }
                    ]
            },
            "field4": {
                    "index": 4,
                    "Name": "TR",
                    "component": {
                            "Device1": "Controller",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01",
                            "id2": "02"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "LoadDevice",
                                    "role2": "ControlDevice",
                                    "role3": "GensetDevice"
                            }
                    },
                    "service": [
                            {
                                    "index": 1,
                                    "ACTIVEPOWERCONSUMPTION": 1927341568.0,
                                    "FREQUENCY": 60.04,
                                    "IA": 86.75,
                                    "IB": 90.5,
                                    "IC": 110.09,
                                    "PF": 0.81,
                                    "REACTIVEPOWERCONSUMPSION": 197824.78,
                                    "TOTALACTIVEPOWER": 44166.32,
                                    "TOTALAPPARENTPOWER": 54508.18,
                                    "TOTALREACTIVEPOWER": 31944.9,
                                    "VA": 218.77,
                                    "VAB": 380.13,
                                    "VB": 220.04,
                                    "VBC": 380.54,
                                    "VC": 218.35,
                                    "VCA": 377.49
                            },
                            {
                                    "index": 2,
                                    "ACTIVEPOWERMAX": 436533.81,
                                    "CTRATIO": 600.0,
                                    "FREQUENCY": 60.04,
                                    "IINVERSE": 0.0,
                                    "IA": 52.87,
                                    "IB": 36.56,
                                    "IC": 42.9,
                                    "INVERSEACTIVEPOWERMAX": 317356.47,
                                    "INVERSEREACTIVEPOWERMAX": 556029.88,
                                    "IZERO": 0.24,
                                    "IZEROMAX": 14.44,
                                    "LOADPERCENT": 0.0,
                                    "PTRATIO": 380.0,
                                    "PRIMARYNCTRATIO": 5.0,
                                    "TOTALACTIVEPOWERCONSUMPTION": 88130312.0,
                                    "TOTALACTIVEPOWER": 0.0,
                                    "TOTALINVERSEACTIVEPOWERCONSUMPTION": 44325720.0,
                                    "TOTALINVERSEACTIVEPOWER": 26615.26,
                                    "TOTALPOWERFACTOR": 0.0,
                                    "TOTALREACTIVEPOWER": 6749.68,
                                    "TOTALREACTIVEPOWERCONSUMPTION": 0.0,
                                    "VA": 218.69,
                                    "VAB": 379.81,
                                    "VB": 219.37,
                                    "VBC": 379.8,
                                    "VC": 218.42,
                                    "VCA": 377.35,
                                    "VOB": 0.0
                            }
                    ]
            },
            "field5": {
                    "index": 5,
                    "Name": "PhotoVolatic Equipment",
                    "component": {
                            "Device1": "Controller",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "LoadDevice",
                                    "role2": "ControlDevice",
                                    "role3": "GensetDevice"
                            }
                    },
                    "service": [
                            {
                                    "index": 1,
                                    "AC_Power": 0.0,
                                    "CumulativeCO2Saving": 97.15,
                                    "CumulativePowerGeneration": 208354.98,
                                    "DC_Power": 0.0,
                                    "InverterCapacity": 67.0,
                                    "Outsidetemperature": 0.0,
                                    "SolarAltitudeAngle": 8.53,
                                    "SolarAzimuthAngle": 299.74,
                                    "ToDayCO2Saving": 185.72,
                                    "ToDayPerPowerGeneration": 398.33,
                                    "ToDaySunRisingTime_HHMM": 519.0,
                                    "ToDaySunSetTime_HHMM": 1948.0,
                                    "ToMonthPerPowerGeneration": 2692.2,
                                    "ToYearPoerPowerGeneration": 37424.54,
                                    "HorizontalInsolation": 0.0,
                                    "Latitude": 35.31,
                                    "Longitude": 126.19,
                                    "ModuleTemperature": 0.0,
                                    "PowerGenerationEfficiency": 0.0,
                                    "SlopeInsolation": 0.0,
                                    "StringCapacity": 66.36,
                                    "SystemDate_YYYYMMDD": 20230609.0,
                                    "SystemHours_HHMMSS": 203357.0
                            }
                    ]
            },
            "field6": {
                    "index": 6,
                    "Name": "EVCharger Equipment",
                    "component": {
                            "Device1": "Controller",
                            "Device2": "Switch",
                            "Device3": "Measure_Sensor1"
                    },
                    "id": {
                            "id1": "01",
                            "id2": "02",
                            "id3": "03"
                    },
                    "role": {
                            "DC_Microgrid": {
                                    "role1": "LoadDevice",
                                    "role2": "ControlDevice",
                                    "role3": "GensetDevice"
                            }
                    },
                    "service": [
                            {
                                    "index": 1,
                                    "ActivePowerConsumption": 1863255.0,
                                    "ActivePowerConsumptionGigaCounter": 0.0,
                                    "ApparantPowerConsumption": 1884160.0,
                                    "ApparantPowerConsumptionGigaCounter": 0.0,
                                    "CT_Ratio": 30.0,
                                    "DI1_Counter": 0.0,
                                    "DI2_Counter": 0.0,
                                    "DI_DebounceTime": 0.0,
                                    "DemandTime": 20.0,
                                    "Frequency": 60.25,
                                    "Ia": 0.0,
                                    "Iavg": 0.0,
                                    "Ib": 0.0,
                                    "Ic": 0.0,
                                    "Load_Factor_of_Phase_A": 0.0,
                                    "Load_Factor_of_Phase_B": 0.0,
                                    "Load_Factor_of_Phase_C": 0.0,
                                    "PT_Ratio": 1.0,
                                    "Pf": 0.0,
                                    "ReactivePowerCounsumption": 384.39,
                                    "ReactivePowerCounsumptionGigaCounter": 0.0,
                                    "TotalActivePower": 0.0,
                                    "TotalApparentPower": 0.0,
                                    "TotalReactivePower": 0.0,
                                    "Va": 216.7,
                                    "Vab": 377.84,
                                    "Vavg": 216.0,
                                    "Vb": 217.92,
                                    "Vc": 217.92,
                                    "Vca": 217.92
                            },
                            {
                                    "index": 2,
                                    "ActivePowerConsumption": 2757764.0,
                                    "ActivePowerConsumptionGigaCounter": 0.0,
                                    "ApparantPowerConsumption": 8257536.0,
                                    "ApparantPowerConsumptionGigaCounter": 0.0,
                                    "CT_Ratio": 40.0,
                                    "DI1_Counter": 0.0,
                                    "DI2_Counter": 0.0,
                                    "DI_DebounceTime": 0.0,
                                    "DemandTime": 2.0,
                                    "Frequency": 60.2,
                                    "Ia": 0.0,
                                    "Iavg": 0.0,
                                    "Ib": 0.0,
                                    "Ic": 0.0,
                                    "Load_Factor_of_Phase_A": 0.0,
                                    "Load_Factor_of_Phase_B": 0.0,
                                    "Load_Factor_of_Phase_C": 0.0,
                                    "PT_Ratio": 1.0,
                                    "Pf": 0.0,
                                    "ReactivePowerCounsumption": 1454.29,
                                    "ReactivePowerCounsumptionGigaCounter": 0.0,
                                    "TotalActivePower": 0.0,
                                    "TotalApparentPower": 0.0,
                                    "TotalReactivePower": 0.0,
                                    "Va": 215.63,
                                    "Vab": 374.51,
                                    "Vavg": 216.0,
                                    "Vb": 217.29,
                                    "Vc": 217.29,
                                    "Vca": 217.29
                            },
                            {
                                    "index": 3,
                                    "ActivePowerConsumption": 62374.7,
                                    "ActivePowerConsumptionGigaCounter": 0.0,
                                    "ApparantPowerConsumption": 2310144.0,
                                    "ApparantPowerConsumptionGigaCounter": 0.0,
                                    "CT_Ratio": 30.0,
                                    "DI1_Counter": 0.0,
                                    "DI2_Counter": 0.0,
                                    "DI_DebounceTime": 0.0,
                                    "DemandTime": 15.0,
                                    "Frequency": 60.22,
                                    "Ia": 0.0,
                                    "Iavg": 0.0,
                                    "Ib": 0.0,
                                    "Ic": 0.0,
                                    "Load_Factor_of_Phase_A": 0.0,
                                    "Load_Factor_of_Phase_B": 0.0,
                                    "Load_Factor_of_Phase_C": 0.0,
                                    "PT_Ratio": 1.0,
                                    "Pf": 0.0,
                                    "ReactivePowerCounsumption": 1974499.0,
                                    "ReactivePowerCounsumptionGigaCounter": 0.0,
                                    "TotalActivePower": 0.0,
                                    "TotalApparentPower": 0.0,
                                    "TotalReactivePower": 0.0,
                                    "Va": 216.77,
                                    "Vab": 376.61,
                                    "Vavg": 216.0,
                                    "Vb": 217.53,
                                    "Vc": 217.53,
                                    "Vca": 217.53
                            }
                    ]
            }
    },
    "etc": {
            "test1": 111,
            "test2": 111
    }
}

def createConnectionAndQueue(user='guest',pw='guest'):
    cred = pika.PlainCredentials(user,pw)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672,credentials=cred))
    chan = connection.channel()
    try :
        chan.queue_declare(queue='test.queue')
    except(pika.exceptions.ChannelClosedByBroker):
        print("Queue Already Exists!")
        chan = connection.channel()
        return chan
    try : 
        chan.queue_bind(queue='test.queue',exchange='amq.direct',routing_key='test.route')
    except(pika.exceptions.ChannelClosedByBroker):
        chan = connection.channel()
        return chan
    return chan

chan = createConnectionAndQueue('admin','rabbitpassword')

def basicPub():
    chan.basic_publish(exchange='amq.direct',routing_key='test.route',body=data)

schedule.every(0.05).seconds.do(basicPub)

while True:
        schedule.run_pending()
    
