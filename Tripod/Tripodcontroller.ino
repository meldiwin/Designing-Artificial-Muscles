int POT_1= A0;
int POT_2= A1;
int POT_3= A1;
int actuator_1=3 ; // here will be the first actuator//
int actuator_2=4 ; // here will be the second actuator//
int actuator_3=5 ; // here will be the second actuator//


int analogreadvalue_1;   // this variable to look at the 0-5 volt potentiometer_1 voltage at pin A0//
int analogreadvalue_2;   // this variable to look at the 0-5 volt potentiometer_2 voltage at pin A1//
int analogreadvalue_3;   // this variable to look at the 0-5 volt potentiometer_3 voltage at pin A2//
int analogwritevalue_1; // this variable to write 0-5 v to the actuator_1//
int analogwritevalue_2; // this variable to write 0-5 v to the actuator_2//
int analogwritevalue_3; // this variable to write 0-5 v to the actuator_3//

void setup() {
  serial.begin(9600);
  pinMode(POT_1, INPUT)
  pinMode(POT_2, INPUT)
  pinMode(POT_3, INPUT)
  pinMode(actuator_1, OUTPUT)
  pinMode(actuator_2, OUTPUT)
  pinMode(actuator_3, OUTPUT)
}

void loop(){
  analogreadvalue_1=analogRead(POT_1);  // Reading the value of potentiometer_1//
  analogreadvalue_2=analogRead(POT_2);  // Reading the value of potentiometer_2//
  analogreadvalue_3=analogRead(POT_3);  // Reading the value of potentiometer_3//
  analogwritevalue_1=(255./1023.) * analogreadvalue_1;  // conversion from 1023 scale to 255 scale//
  analogwritevalue_2=(255./1023.) * analogreadvalue_2;  
  analogwritevalue_3=(255./1023.) * analogreadvalue_3;  
  analogWrite(actuator_1, analogwritevalue_1);
  analogWrite(actuator_2, analogwritevalue_2);
  analogWrite(actuator_3, analogwritevalue_3);
  Serial.print("Analog Value to Actuator_1:   ");
  Serial.print("Analog Value to Actuator_2:   ");
  Serial.print("Analog Value to Actuator_3:   ");
  Serial.println("analogwritevalue_1);
  Serial.println("analogwritevalue_2);
  Serial.println("analogwritevalue_3);
  delay(500);
}
  
}
