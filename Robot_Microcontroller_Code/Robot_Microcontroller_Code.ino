#include <AFMotor.h>
#include <SoftwareSerial.h>
AF_DCMotor motor01(1);
AF_DCMotor motor02(2);
int MotorSpeed = 255;
#define DEBUG true
#define RXPIN 3
#define TXPIN 4

SoftwareSerial esp8266Serial(RXPIN, TXPIN); //Pin 2 & 3 of Arduino as RX and TX. Connect TX and RX of ESP8266 respectively.


void setup()
{
  motor01.setSpeed(255);
  motor01.run(RELEASE);
  motor02.setSpeed(255);
  motor02.run(RELEASE);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

  esp8266Serial.begin(115200); //Baud rate for communicating with ESP8266. Your's might be different.
  esp8266Data("AT+RST\r\n", 5000, DEBUG); // Reset the ESP8266
  esp8266Data("AT+CWMODE=1\r\n", 5000, DEBUG); //Set station mode Operation

  /*Change the following command as per your requirement i.e. enter the
    SSID and Password of your WiFi Network in the command.*/

  esp8266Data("AT+CWJAP=\"C11.5\",\"don2to3#@\"\r\n", 5000, DEBUG);//Enter your WiFi network's SSID and Password.

  /*while(!esp8266Serial.find("OK"))
    {
    }*/

  esp8266Data("AT+CIFSR\r\n", 5000, DEBUG);//You will get the IP Address of the ESP8266 from this command.

  /* The following statement is to assign Static IP Address to ESP8266.
    The syntax is AT+CIPSTA=<ip>,<gateway>,<netmask>.
    This will assign a Static IP Address of 192.168.1.254 (in my case)
    to the ESP8266 Module. Change this value as per your requirements i.e. this IP address
    shouldn't conflict with any other device.
    Also, the second and third parameters are Gateway and Net Mask values.
    You can get these values from ipconfig command in command prompt*/

  esp8266Data("AT+CIPSTA=\"192.168.52.25\",\"192.168.1.1\",\"255.255.255.0\"\r\n", 3000, DEBUG); // Assign Static IP Address
  esp8266Data("AT+CIFSR\r\n", 5000, DEBUG);//You will get the IP Address of the ESP8266 from this command.

  esp8266Data("AT+CIPMUX=1\r\n", 5000, DEBUG);
  esp8266Data("AT+CIPSERVER=1,5000\r\n", 5000, DEBUG);


  for (int i = 0; i <= 2; i++)
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
  }

}

void loop()
{
  if (esp8266Serial.available() > 0)
  {
    if (esp8266Serial.find("+IPD,"))
    {
      String msg;
      esp8266Serial.find("?");
      msg = esp8266Serial.readStringUntil(' ');
      String command1 = msg.substring(0, 1);
      Serial.println(command1);
      delay(2);

      if (DEBUG)
      {
//        Serial.println(command1); //First 1st char
//        Serial.println(command2); //last char
      }
      delay(2);
      if (command1 == "U")
      {
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println(command1);
        Serial.println("FORWARD");
        forward();
        command1 = "";
      }
      else if (command1 == "B")
      {
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println(command1);
        Serial.println("BACKWARD");
        backward();
        command1 = "";
      }
      else if (command1 == "R")
      {
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println(command1);
        Serial.println("RIGHT");
        right();
        command1 = "";
      }
      else if (command1 == "L")
      {
        digitalWrite(LED_BUILTIN, HIGH);
        Serial.println(command1);
        Serial.println("LEFT");
        left();
        command1 = "";
      }
      else if (command1 == "S")
      {
        digitalWrite(LED_BUILTIN, LOW);
        Serial.println(command1);
        Serial.println("STOPED");
        stopMotor();
        command1 = "";
      }
      else if (command1 == "T")
      {
        stopMotor();
        for (int i = 0; i <= 5; ++i) {
          digitalWrite(LED_BUILTIN, HIGH);
          delay(100);
          digitalWrite(LED_BUILTIN, LOW);
          delay(100);
        }
        Serial.println(command1);
        Serial.println("TESTED");
      }
      else
      {
        digitalWrite(LED_BUILTIN, LOW);
        Serial.println("The Data is this :");
        Serial.println(command1);
        stopMotor();
        command1 = "";
      }
    }
  }
}


void forward()
{
  motor02.run(FORWARD);
  motor01.run(FORWARD);
  motor01.setSpeed(MotorSpeed);
  motor02.setSpeed(MotorSpeed);
}

void search()
{
  motor02.run(FORWARD);
  motor01.run(BACKWARD);
  motor01.setSpeed(MotorSpeed);
  motor02.setSpeed(MotorSpeed);
}


void backward()
{
  motor02.run(BACKWARD);
  motor01.run(BACKWARD);
  motor01.setSpeed(MotorSpeed);
  motor02.setSpeed(MotorSpeed);
}

void right()
{
  motor01.run(FORWARD);
  motor02.run(BACKWARD);
  motor01.setSpeed(MotorSpeed);
  motor02.setSpeed(MotorSpeed);
  
}

void left()
{
  motor01.run(BACKWARD);
  motor02.run(FORWARD);
  motor01.setSpeed(MotorSpeed);
  motor02.setSpeed(MotorSpeed);;
}

void stopMotor()
{
  motor02.run(RELEASE);
  motor01.run(RELEASE);
}

String esp8266Data(String command, const int timeout, boolean debug)
{
  String response = "";
  esp8266Serial.print(command);
  long int time = millis();
  while ( (time + timeout) > millis())
  {
    while (esp8266Serial.available())
    {
      char c = esp8266Serial.read();
      response += c;
    }
  }
  if (debug)
  {
    Serial.print(response);
  }
  return response;
}

