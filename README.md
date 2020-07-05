# RPi.GPIO

RPi.GPIO (A Python module to control the GPIO on a Raspberry Pi) for Banana Pi 

## Build

```
apt-get install python3-all python3-all-dev debhelper
./make_deb
```

## Debug

Set env RPIGPIO_DEBUG to debug-level (1-4) to see debug messages, see [pull18_bcm.py](https://github.com/GrazerComputerClub/RPi.GPIO/blob/master/test/pull18_bcm.py) 

## Modifcations by GC2

This is a combination of original [SourceForge v0.7.0](https://sourceforge.net/p/raspberry-gpio-python/code/ci/default/tree/) and [BPI-SINOVOIP/RPi.GPIO](https://github.com/BPI-SINOVOIP/RPi.GPIO) with a couple of bug fixes.
The binary (tools and library) will support both worlds Raspberry Pi and Banana Pi M2 Zero.

Original SourceForge v0.7.0. is available at sf-7.0 brunch.

We provide no support! 

Please contact base repository maintainers if you have problems.


