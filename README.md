# Integrating Real-World Distractions into Virtual Reality
This repository contains hardware design files and VR scenes presented in the paper [Integrating Real-World Distractions into Virtual Reality](https://lab.plopes.org/published/2022-UIST-IntegratingDistractions.pdf), which appeared at UIST 2022. In this work, we explore a new concept, where we directly integrate the distracting stimuli from the user’s physical surroundings into their virtual reality experience to enhance presence. This work was done by Yujie Tao and Pedro Lopes at the University of Chicago's Human Computer Integration Lab.

[Paper](https://lab.plopes.org/published/2022-UIST-IntegratingDistractions.pdf) | [Video](https://youtu.be/PO8ZlQGYMY8) | [UIST'22 Talk](https://youtu.be/COlRRy4sugs)

## Proof of Concept Prototype
![Group 1061](https://user-images.githubusercontent.com/32469005/205561758-1b62ec20-eec8-4dec-9b68-ce030c90f136.jpg)
In this paper, we proposed a proof-of-concept device that detects a small set of distractive stimuli: wind, temperature change, door closing sound, car engine sound, and talking sound. 

### Prototype Components
* Microphone - [Link](https://www.amazon.com/gp/product/B082M9W4G1/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
* Wind sensor (Wind Sensor Rev. C) - [Link](https://moderndevice.com/products/wind-sensor)
* Temperature sensor (DS18B20) - [Link](https://www.amazon.com/SunFounder-DS18B20-Temperature-Arduino-Raspberry/dp/B013GB27HS/ref=sr_1_19?keywords=DS18B20&qid=1670220883&sr=8-19)

### Sensing
* Audio classification -  [Ubicoustics](https://github.com/FIGLAB/ubicoustics) by Laput et.al.
* Temperature/wind sensing - [this file]()

## VR Demo Presented at UIST 2022
At UIST 2022, we demoed this project using a VR room escape experience. In this demo, the audience, while finding keys in the mysterious VR room, experienced four different distractions: wind, touch, temperature change, and drilling sound. In the scene, we mapped these four distractions with curtain movement, bat appearance, fire, and debris fall accordingly. While we adopted the wizard-of-oz approach in this demo (i.e., both distractions and mapping were triggered manually) to ensure demo quality, we see future iterations of the sensing system could robustly detect all of these distractions. Here we provided the VR scene used in this demo and a simple script to connect with sensor results from the current prototype system (e.g., the mapping to be triggered automatically when certain distractions are detected). 

## Citation

When using or building upon this device/work in an academic publication, please consider citing as follows:

Tao, Y., & Lopes, P. (2022, October). Integrating Real-World Distractions into Virtual Reality. In Proceedings of the 35th Annual ACM Symposium on User Interface Software and Technology (pp. 1-16).

## Contact

For questions or if something is wrong with this repository, contact yjtao@stanford.edu.
