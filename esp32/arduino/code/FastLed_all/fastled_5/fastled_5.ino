#include <FastLED.h>

// LED 随机亮灯，

#define LED_PIN 5 // Replace with the pin number you used for DATA connection
#define NUM_LEDS 5 // Replace with the number of LEDs in your strip
#define FLICKER_DELAY 200 // Delay between flicker changes (in milliseconds)
CRGB leds[NUM_LEDS];

void setup() {

  FastLED.addLeds<WS2811, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {

  // Set the initial color for the candle蜡烛 flame 火焰
  CRGB flameColor = CRGB::Red;

  // Create a flickering 闪烁 effect
  for (int i = 0; i < NUM_LEDS; i++) {

    // Randomly flicker the LEDs
    if (random(10) < 5) {
      leds[i] = flameColor;
    } else {
      leds[i] = CRGB::Black;
    }
  }
  FastLED.show(); // Update the LED strip
  delay(FLICKER_DELAY); // Delay between flicker changes
  
}