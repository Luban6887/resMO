#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
bool Flip = true;
void setup()
{
  lcd.begin();
  lcd.print("  WELCOME SIR");
  lcd.setCursor(0,1);
  lcd.print("run-app-to-start");
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
    int my_arr[2];
    for (int i = 0; i<2;i++){
      my_arr[i] = Serial.parseInt();
    }
    if (Flip == true){
      lcd.clear();
      Flip = false;
    }
    DISP(my_arr[0], my_arr[1]);
  }  
}

void DISP(int ram,int cpu){
  lcd.setCursor(0,0);
  lcd.print("RAM IN USE ");
  lcd.setCursor(11, 0);
  lcd.print(ram);
  //lcd.setCursor(14, 0);
  lcd.print("%   ");
  lcd.setCursor(0,1);
  lcd.print("CPU IN USE ");
  lcd.setCursor(11, 1);
  lcd.print(cpu);
  //lcd.setCursor(14, 1);
  lcd.print("%   ");
}