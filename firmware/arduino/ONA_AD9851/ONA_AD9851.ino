char incmd[10];
int cindex = 0;
long freq = 0;
char ch;
int AD8307 = A0;
int WCLK = A4;
int DATA = A5;
int FQ_UD = 8;
long FTW;
int sum;

void powerOff()
{
  long pointer = 1;
  int pointer2 = 0b10000000;
  int lastByte = 0b10100000;

  digitalWrite(DATA, LOW);

  for (int i=0; i<32; i++)
  {
    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
  }

  for (int i=0; i<8; i++)
  {
    if ((lastByte & pointer2) > 0) digitalWrite(DATA, HIGH);
    else digitalWrite(DATA, LOW);
    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
    pointer2 = pointer2 >> 1;
  }

  digitalWrite(FQ_UD, HIGH);
  digitalWrite(FQ_UD, LOW);
}

void SetFreq(long frequency)
{
  FTW = (frequency*pow(2,24))/(179999563/256);
  long pointer = 1;
  int pointer2 = 0b10000000;
  int lastByte = 0b10000000;

  for (int i=0; i<32; i++)
  {
    if ((FTW & pointer) > 0) digitalWrite(DATA, HIGH);
    else digitalWrite(DATA, LOW);
    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
    pointer = pointer << 1;
  }

  for (int i=0; i<8; i++)
  {
    if ((lastByte & pointer2) > 0) digitalWrite(DATA, HIGH);
    else digitalWrite(DATA, LOW);
    digitalWrite(WCLK, HIGH);
    digitalWrite(WCLK, LOW);
    pointer2 = pointer2 >> 1;
  }

  digitalWrite(FQ_UD, HIGH);
  digitalWrite(FQ_UD, LOW);

  FTW = 0;
}

void setup()
{
  Serial.begin(9600);
  pinMode(AD8307, INPUT);
  pinMode(WCLK, OUTPUT);
  pinMode(DATA, OUTPUT);
  pinMode(FQ_UD, OUTPUT);

  // Enter serial mode
  digitalWrite(WCLK, HIGH);
  digitalWrite(WCLK, LOW);
  digitalWrite(FQ_UD, HIGH);
  digitalWrite(FQ_UD, LOW);

  SetFreq(10000000);
}

void loop()
{
  while(Serial.available())
  {
    ch = (char)Serial.read();
    
    if (((ch >= '0') && (ch <='9')) || (ch == 'p')) incmd[cindex++] = ch;
    if (ch == '\n')
    {
      incmd[cindex] = '\n';
      freq = atol(incmd);
      cindex = 0;
//      Serial.print("Input command: ");
//      Serial.println(freq);

      if ((freq > 0) && (freq <= 72000000)) SetFreq(freq);
//      {
//        if (freq == 1) powerOff();
//        else SetFreq(freq);
//      }
      else //Serial.println(analogRead(AD8307));
      {
        sum = 0;
        
        for (int n = 0; n < 16; n++)
        {
          sum += analogRead(AD8307);
        }
        sum = sum >> 2;
        Serial.println(sum);
      }
    }
  }
}
