#include <FastLED.h>

// 白光led，循环， 增加亮灯，降低亮度

#define LED_PIN 5 // Replace with the pin number you used for DATA connection
#define NUM_LEDS 5 // Replace with the number of LEDs in your strip
#define FADE_DELAY 1 // Delay between brightness changes (in milliseconds)
#define MAX_BRIGHTNESS 255 // Maximum brightness value

CRGB leds[NUM_LEDS];

void setup() {
  
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {

  // Increase brightness 增加
  for (int brightness = 0; brightness <= MAX_BRIGHTNESS; brightness++) {

    setBrightness(brightness);
    delay(FADE_DELAY);
  }

  // Decrease brightness 降低
  for (int brightness = MAX_BRIGHTNESS; brightness >= 0; brightness--) {

    setBrightness(brightness);
    delay(FADE_DELAY);
  }

}

void setBrightness(int brightness) {

  for (int i = 0; i < NUM_LEDS; i++) {

    leds[i] = CRGB(brightness, brightness, brightness);
  }
  FastLED.show(); // Update the LED strip
}
