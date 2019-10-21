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

