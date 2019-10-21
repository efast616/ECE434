after running build kernel the first time the bone no longer boots from the SD card

Project Idea
Connor and I are planning on building a tank that can potentially be conrolled by a phone app

1. Target = app.o
2. Dependency = app.c
3. Command = gcc

Installing Kernel

I installed the kernel using the ./build_kernel.sh command 
I have kernel version 4.18.20


Cross Compile Hello World

Host Output
	Hello, World! Main is executing at 0x55a47c3796aa
	This address (0x7ffca920c3e0) is in our stack frame
	This address (0x55a47c57a018) is in our bss section
	This address (0x55a47c57a010) is in our data section

Bone Output
	Hello, World! Main is executing at 0x4315ad
	This address (0xbeb3ec48) is in our stack frame
	This address (0x442010) is in our bss section
	This address (0x442008) is in our data section	

Kernel Modules


Part 1
bone$ modinfo hello.ko
bone$ insmod hello.ko name="Eric"
bone$ dmesg -H | tail -2
	[  +0.006429] EBB: Hello Eric from the BBB LKM!
	[ +19.728010] EBB: Goodbye Eric from the BBB LKM!



Part 2
bone$ sudo insmod ebbchar.ko
bone$ dmesg -H | tail -4	
bone$ sudo ./test
bone$ dmesg -H | tail -8
	[Oct21 03:02] EBBChar: Initializing the EBBChar LKM
	[  +0.000100] EBBChar: registered correctly with major number 240
	[  +0.000118] EBBChar: device class registered correctly
	[  +0.000313] EBBChar: device class created correctly
	[ +38.684790] EBBChar: Device has been opened 1 time(s)
	[  +6.450258] EBBChar: Received 14 characters from the user
	[Oct21 03:03] EBBChar: Sent 14 characters to the user
	[  +0.000708] EBBChar: Device successfully closed

Part 3

bone$ make
bone$ sudo insmod gpio_test.ko
bone$ tail -f /var/log/kern.log
	Oct 21 03:02:12 beaglebone kernel: [10426.297824] EBBChar: device class registered correctly
	Oct 21 03:02:12 beaglebone kernel: [10426.298137] EBBChar: device class created correctly
	Oct 21 03:02:51 beaglebone kernel: [10464.982927] EBBChar: Device has been opened 1 time(s)
	Oct 21 03:02:57 beaglebone kernel: [10471.433185] EBBChar: Received 14 characters from the user
	Oct 21 03:03:01 beaglebone kernel: [10475.660179] EBBChar: Sent 14 characters to the user
	Oct 21 03:03:01 beaglebone kernel: [10475.660887] EBBChar: Device successfully closed
	Oct 21 03:52:30 beaglebone kernel: [13444.424681] GPIO_TEST: Initializing the GPIO_TEST LKM
	Oct 21 03:52:30 beaglebone kernel: [13444.424754] GPIO_TEST: The button state is currently: 0
	Oct 21 03:52:30 beaglebone kernel: [13444.424766] GPIO_TEST: The button is mapped to IRQ: 126
	Oct 21 03:52:30 beaglebone kernel: [13444.424865] GPIO_TEST: The interrupt request result is: 0

