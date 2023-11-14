#include <FastLED.h>

// 颜色循环变化

#define LED_PIN 5 // Replace with the pin number you used for DATA connection
#define NUM_LEDS 5 // Replace with the number of LEDs in your strip
#define GRADIENT_DELAY 500 // Delay between gradient color changes (in milliseconds)
#define MOVEMENT_DELAY 500 // Delay between LED movements (in milliseconds)
CRGB leds[NUM_LEDS];

void setup() {

  FastLED.addLeds<WS2811, LED_PIN, GRB>(leds, NUM_LEDS);
}

void loop() {

  // Set the initial color gradient
  CRGB startColor = CRGB::Red;
  CRGB endColor = CRGB::Blue;

  // Calculate color step values
  int colorStepsR = (endColor.r - startColor.r) / NUM_LEDS;
  int colorStepsG = (endColor.g - startColor.g) / NUM_LEDS;
  int colorStepsB = (endColor.b - startColor.b) / NUM_LEDS;

  // Move the gradient effect across the LED strip
  for (int i = 0; i < NUM_LEDS; i++) {

    CRGB gradientColor = CRGB(startColor.r + (colorStepsR * i),
    startColor.g + (colorStepsG * i),
    startColor.b + (colorStepsB * i));
    // Shift the gradient by moving the LEDs

    for (int j = 0; j < NUM_LEDS; j++) {

      int index = (i + j) % NUM_LEDS;
      leds[index] = gradientColor;
    }

    FastLED.show(); // Update the LED strip
    delay(MOVEMENT_DELAY); // Delay between LED movements
  }

  // Shift the colors for the next frame
  startColor = endColor;
  endColor = CRGB::Green;
}