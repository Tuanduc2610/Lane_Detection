#include<Wire.h>
//#include<TimerOne.h>
#define PWM2 10
#define DIR12 5
#define DIR22 4
#define PWM1 9
#define DIR11 7
#define DIR21 8

#define Kp 0.0058
#define Kd 0.0048
#define Ki 0.006

boolean x = 0, y = 0;
int a = 9, dem = 0;
int v[2];
int lw=0, rw=0;
String a1;
int al=0,ar=0;
int lw1,rw1;
double banhtrai=0, banhphai=0,vl=0,vr=0;
double banhtrai1 = 0, banhphai1=0;
float xung1=0, xung2=0;
float T = 0.1;
double Etr1=0,Etr2=0; //Etr3,Etr4; 
double Ei1=0,Ei2=0; //Ei3,Ei4;
void Demxung1() //trai

{
  xung1++;
}
void Demxung2() //phai
{
  xung2++;
}
float Tocdo1() {
  float tocdo=((xung1/334)*(1/T)*60);
  xung1=0;
  return tocdo;
}
float Tocdo2() {
  float tocdo=((xung2/334)*(1/T)*60);
  xung2=0;
  return tocdo;
}
void Tocdo(){
  banhtrai = Tocdo1();
  banhphai = Tocdo2();
  lw += PID(vl,banhtrai1,Ei1,Etr1);
  rw += PID(vr,banhphai1,Ei2,Etr2);
}
void setup(){
  pinMode(PWM1,OUTPUT); 
  pinMode(DIR11,OUTPUT);
  pinMode(DIR21,OUTPUT);
  pinMode(PWM2,OUTPUT); 
  pinMode(DIR12,OUTPUT);
  pinMode(DIR22,OUTPUT);
  attachInterrupt(1,Demxung2,FALLING);
  attachInterrupt(0,Demxung1,FALLING);
  Wire.begin(0x02);
  Wire.onReceive(receiveEvent);
//  Wire.onRequest(requestEvent);
//  Timer1.initialize(100000);  //don vi us
//  Timer1.attachInterrupt(Tocdo);
  cli();
  TCCR2A = 0x00;
  TCCR2B = 0x00;
  TIMSK2 = 0x00;
  
  TCCR2B = 0x0F;
  TCNT2=7;
  TIMSK2 = (1<<TOIE2);
  sei();
  Serial.begin(9600);
}
void loop() {
  if(Serial.available()){
    a1 = Serial.readString();
    a = a1.toInt();
  }
  // put your main code here, to run repeatedly:
  if (a == 4){  // thang
    vl = 1500;
    vr = 1500;
    banhtrai1=banhtrai;
    banhphai1=banhphai;
    lw = constrain(lw,80,255);
    rw = constrain(rw,80,255);
    x = 1;
    y = 1;
    analogWrite(PWM1, rw);
    analogWrite(PWM2, lw);
//    delay(5);
  }
  if (a ==5){  //re phai
    vl = 1700;
    vr = 400;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
    //delay(5);
  }
  if (a == 3){  //re trai
    vl = 400;
    vr = 1700;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==2){  //re trai
    vl = 100;
    vr = 1800;
 //    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==6){  //re phai
    vl = 1800;
    vr = 100;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==1){  //re trai
    vl = -300;
    vr = 1600;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==7){  //re phai
    vl = 1600;
    vr = -300;
 //    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==0){  //re trai
    vl = -700;
    vr = 1700;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==8){  //re phai
    vl = 1700;
    vr = -700;
//    x = 0;
//    y = 1;
    lw = constrain(lw,-200,255);
    rw = constrain(rw,-200,255);
    rw1 = constrain(abs(rw),90,255);
    lw1 = constrain(abs(lw),90,255);
    if (lw>=0){y=1; banhtrai1=banhtrai; }
    else if (lw<0){y=0; banhtrai1=-banhtrai; }
    if (rw>=0){x=1; banhphai1=banhphai; }
    else if (rw<0){x=0; banhphai1=-banhphai; }
    analogWrite(PWM1, rw1);
    analogWrite(PWM2, lw1);
//    delay(5);
  }
  if (a==9){  //stop
    analogWrite(PWM1, 0);
    analogWrite(PWM2, 0);
    al =0;
    ar=0;
    digitalWrite(DIR11,LOW);
    digitalWrite(DIR21,LOW);
    digitalWrite(DIR12,LOW);
    digitalWrite(DIR22,LOW);
  }
  dieukhien();
  receiveEvent(4);
  //requestEvent();
  //string = " vl: " + String(vl) + "vr: " + String(vr);
  //Serial.println(string)
  Serial.print("banhtrai1= ");
  Serial.print(banhtrai1);
  Serial.print(",");
  Serial.print("  banhphai1= ");
  Serial.println(banhphai1);
  //Wire.beginTransmission(2);
  //int v[2] = {vl, vr};
  //Wire.write(int(vl));
  //Wire.endTransmission();
//  Serial.print("a = ");
//  Serial.println(a);
//  Serial.print("lw = ");
//  Serial.println(lw);
//  Serial.print("rw = ");
//  Serial.println(rw);
//  Serial.print("x = ");
//  Serial.println(x);
//  Serial.print("y = ");
//  Serial.println(y);
}

void receiveEvent(int h) {
  if(Wire.available()){
    a = Wire.read();
    //Serial.print("a = ");
    //Serial.println(a); 
    delay(2);
  }
}
//void requestEvent(){
//  
//  int v[2]= {vl,  vr};
//  int data = 2;
//  Wire.write(data);
//}
void dieukhien(){
 if (x==1){    // Bánh sau bên phải
    digitalWrite(DIR11,LOW);
    digitalWrite(DIR21,HIGH);
  } else if (x==0) {
    digitalWrite(DIR11,HIGH);
    digitalWrite(DIR21,LOW);
  }
  if (y == 1 ){
    digitalWrite(DIR12,HIGH);
    digitalWrite(DIR22,LOW);
  }
  else if (y==0){
    digitalWrite(DIR12,LOW);
    digitalWrite(DIR22,HIGH);
  } 
//  Serial.println(a);
}
double PID(float tocdodat, float tocdo, double Ei, double Etr){
//  float za = 1000/(abs(tocdodat)-(3*pow(tocdodat,2)/65620)+1400);
//  if (za>2.5){
//    za = 4;
//  }
  double E = (tocdodat - tocdo);
  float zb = (abs(E)+700)/700;
  Ei += E;
  double Output = zb*(Kp*E + Ki*Ei + Kd*(E-Etr));
  Etr = E;
//  Serial.print("E = ");
//  Serial.println(E);
  Output = constrain(Output, -255 ,255);
//  Serial.print("Output = ");
//  Serial.println(Output);
  return Output;
}
ISR(TIMER2_OVF_vect) {
    TCNT2 = 0x0F;
    dem++;
    if (dem == 7) {
      Tocdo();
      dem = 1;
//      if(banhtrai<400){
//        al = al+2;
//      } else if(banhtrai<4000){
//        al=al;
//      } else { al = al -3; }
//      if(banhphai<400){
//        ar = ar+2;
//      } else if(banhphai<4000){
//        ar=ar;
//      } else { ar = ar - 3; }
//      ar = constrain(ar,-5,60);
//      al = constrain(al,-5,60);
    }   
}
