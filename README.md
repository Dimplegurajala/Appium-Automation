# Appium-Automation
Python + Appium E2E Automation Framework for Android Retail App using Page Object Model (POM).

#  Android E2E Automation Framework | Sauce Labs Demo App

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-2.0-purple?style=for-the-badge&logo=appium&logoColor=white)
![Pytest](https://img.shields.io/badge/Framework-Pytest-yellow?style=for-the-badge&logo=pytest&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Android_Native-green?style=for-the-badge&logo=android&logoColor=white)

##  Overview
This repository contains a robust **End-to-End (E2E) Native Mobile Automation Framework** built to test the **Sauce Labs MyDemoApp (React Native)** on Android.

The project demonstrates a professional implementation of the **Page Object Model (POM)** design pattern, ensuring code reusability and maintainability. It specifically addresses the challenges of **Native Mobile Automation**, such as handling keyboard overlays, managing specific payment screen transitions, and implementing robust synchronization strategies.


##  Application Under Test (AUT)
The automation is built for the **Sauce Labs My Demo App (React Native)**.
* **App Source:** [Sauce Labs GitHub Releases](https://github.com/saucelabs/my-demo-app-rn/releases)
* **demo .apk Used:** `Android-MyDemoAppRN.1.3.0.build-244.apk` (or latest version)
* **Platform:** Android Emulator (Pixel API 35)

##  Key Features
* **Page Object Model (POM):** Strict separation between test scripts and page logic (`pages/` vs `tests/`).
* **Native UI Handling:**
    * **Smart Scrolling:** Implemented `UiScrollable` to find buttons hidden off-screen (e.g., "To Payment" button).
    * **Keyboard Management:** Explicit handling of `hide_keyboard()` to prevent UI crashes during page transitions.
* **Stability over Speed:** Implemented a mix of **Explicit Waits** and strategic `time.sleep` to handle complex page load animations (Payment Page transitions) where standard waits failed.

##  Tech Stack
* **Language:** Python 3.3.x(latest)
* **Mobile Driver:** Appium 
* **Test Runner:** Pytest
* **Locators:** Appium Inspector (Accessibility ID, XPath, Android UIAutomator)
* **IDE:** VS Code 

##  Project Structure
```text
├── pages/
│   ├── base_page.py        # Wrapper for common driver actions (click, fill, wait)
│   ├── login_page.py       # Login logic
│   ├── product_listing_page.py # Catalog interactions (Add to cart)
│   ├── cart_page.py        # Cart verification
│   ├── checkout_page.py    # Shipping logic (Scroll & Keyboard handling)
│   ├── payment_page.py     # Payment logic (Card entry & validations)
│   └── review_page.py      # Final assertions & Logout
├── tests/
│   ├── test_e2e_page1.py   # The main E2E execution script
├── requirements.txt        # Project dependencies
└── README.md

