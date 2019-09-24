#!/bin/sh
temp=$(i2cget -y 2 0x48 0)
temp=$((temp * 9 / 5 + 32))
echo "Degrees Fahrenheit" $temp
$(i2cset -y 2 0x48 2 70)
$(i2cset -y 2 0x48 3 80)
Thigh=$(i2cget -y 2 0x48 3)
Tlow=$(i2cget -y 2 0x48 2)
echo "Low Temp" $(($Tlow))
echo "High Temp" $(($Thigh))
