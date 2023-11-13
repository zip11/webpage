#include <FastLED.h>

// 流水灯 ，第一次从左到右亮灯。第二次 从右往左亮灯

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

  // Turn off all LEDs
  for (int i = 0; i < NUM_LEDS; i++) {
  leds[i] = CRGB::Black;
  }
  
  // Move the LED chaser
  for (int i = 0; i < NUM_LEDS; i++) {

    leds[i] = CRGB::Yellow; // Set the current LED to blue
    FastLED.show(); // Update the LED strip
    delay(DELAY_TIME); // Delay between LED movements
  }

  // Move the LED chaser in reverse
  for (int i = NUM_LEDS - 1; i >= 0; i--) {

    leds[i] = CRGB::Green; // Set the current LED to green
    FastLED.show(); // Update the LED strip
    delay(DELAY_TIME); // Delay between LED movements
  }
}