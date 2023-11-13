#include <IRremote.h>
#define  RECV_PIN 11
 
IRrecv irrecv(RECV_PIN);   // 红外遥控初始化
decode_results results;   // 储存接收到的红外遥控信息

bool kgled = true;
 
void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);     
  Serial.begin(9600);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn();     // 启动红外接收
  Serial.println("Enabled IRin");
}
 
void loop() {
  /* 
  decode()库函数用于判断红外接收器所接收到的红外信号是否可以被解析。
  如可以成功解析，则返回非零数值。并将解析结果存储于results中。
  如无法成功解析，则返回零。
  
  每一次解析完成，都需要调用resume()函数从而让Arduino开始准备接收下一个红外
  遥控指令。
  */



  if (irrecv.decode(&results)) {  
    Serial.println(results.value, HEX);  // results.value为红外遥控信号的具体数值
 
    if(results.value == 0xF7C03F) //如果控制信息数值为F7C03F
    {          
        Serial.println("Command Received: Turn On LED.");
        digitalWrite(LED_BUILTIN, HIGH); 
    } 
    
    if(results.value == 0x4AB0F7B6) //如果控制信息数值为F740BF
    {          
        Serial.println("Command Received:  LED state change.");
        kgled = !kgled;
        digitalWrite(LED_BUILTIN, kgled); 
    }
    
    irrecv.resume(); // 恢复接收下一个红外遥控信号
  }
  delay(100);
}
