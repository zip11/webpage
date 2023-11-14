#include <FastLED.h>

// 全部led，颜色同步变化

#define LED_PIN 5 // Replace with the pin number you used for DATA connection
#define NUM_LEDS 5 // Replace with the number of LEDs in your strip
#define DELAY_TIME 200 // Delay between LED movements (in milliseconds)
CRGB leds[NUM_LEDS];

uint8_t max_bright = 19;
// led 亮度

void setup() {

  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(max_bright);
}


void loop() {

  static uint8_t hue = 0; // Hue value for color shifting
  
  // Set all LEDs to the current hue
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CHSV(hue, 255, 255);
  }
  
  FastLED.show(); // Update the LED strip
  delay(DELAY_TIME); // Delay between color changes
  
  // Shift the hue for the next frame
  hue++;
}


