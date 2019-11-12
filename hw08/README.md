Blinking an LED

	first run setup.sh then to start the running use the command make start
	in order to stop use the command make stop	

PWM Generator
	
	run the following commands
		config-pin P9_31 pruout
		export PRUN=0	
		make
		
	as can be seen the frequency is 50MHz and the waveform is symmetrical

![](hw08_part2_E.png)

Controlling the PWM Frequency

	P9_28-P9_31 are being driven
	There is jitter

![](tek00002_4channel_E.png)

Reading an Input at Regular Intervals

	The delay can be seen on the scope and is 56.6 nanoseconds

![](tek00004_reading_input_E.png)

	

## Prof. Yoder's comments

Looks good.  

Late: -1
Grade:  9/10
