
#define HX711_ADC_config_h

//number of samples in moving average dataset, value must be 1, 2, 4, 8, 16, 32, 64 or 128.
#define SAMPLES 					16		//default value: 16

//adds extra sample(s) to the dataset and ignore peak high/low sample, value must be 0 or 1.
#define IGN_HIGH_SAMPLE 			1		//default value: 1
#define IGN_LOW_SAMPLE 				1		//default value: 1

//microsecond delay after writing sck pin high or low. This delay could be required for faster mcu's.
//So far the only mcu reported to need this delay is the ESP32 (issue #35), both the Arduino Due and ESP8266 seems to run fine without it.
//Change the value to '1' to enable the delay.
#define SCK_DELAY					0		//default value: 0

//if you have some other time consuming (>60μs) interrupt routines that trigger while the sck pin is high, this could unintentionally set the HX711 into "power down" mode
//if required you can change the value to '1' to disable interrupts when writing to the sck pin.
#define SCK_DISABLE_INTERRUPTS		0		//default value: 0
