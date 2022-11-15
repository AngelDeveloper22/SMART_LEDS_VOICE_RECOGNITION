/*
ASIGNACIÓN #2
TÓPICOS ESPECIALES DE CONTROL
PROFESOR: DR. VONG CHONG
FECHA: 15-11-2022
ESTUDIANTE: ANGEL HURTADO
CÓDIGO: FIRMWARE DE ARDUINO UNO PARA LA CONFIGURACIÓN DE ENCENDIDO
        POR MEDIO DE COMUNICACIÓN SERIAL.
*/
const unsigned int MAX_MESSAGE_LENGTH = 12;

void setup() {
  pinMode(13, OUTPUT);
  pinMode(12,OUTPUT);
  digitalWrite(13,LOW);
  digitalWrite(12,LOW);
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // to check if there is something in the serial buffer
  while (Serial.available() > 0)
  {
  // put your main code here, to run repeatedly:
  static char message[MAX_MESSAGE_LENGTH]; //
  static unsigned int message_pos = 0; // Where in the array to put incoming bites

  //Read the next available byte in the serial receive buffer
  char inByte = Serial.read();

  //Message coming in (check not terminating character)
  if (inByte !='\n' && (message_pos < MAX_MESSAGE_LENGTH -1) )
  {
    message[message_pos] = inByte;
    message_pos++;
  }
  // Full message received
  else
  {
    //Add null chacracter to string
    message[message_pos] = '\0';

    //Print the message
    //Serial.println(message);

    //OR WE COULD...
    int number = atoi(message);
    Serial.print(number);
    Serial.print('\n');
    if (number == 8)
    {
      digitalWrite(13,HIGH);
    }
    else if (number == 9)
    {
      digitalWrite(13,LOW);
    }
    else if (number == 1)
    {
      digitalWrite(12,HIGH);
    }
    else if (number == 0)
    {
      digitalWrite(12,LOW);
    }

    //Reset the position variable
    message_pos = 0;
  }

  }
}
