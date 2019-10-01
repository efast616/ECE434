// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    volatile unsigned int *button;
    unsigned int reg;
    volatile void *gpio_addr1;
    volatile unsigned int *gpio_oe_addr1;
    volatile unsigned int *gpio_setdataout_addr1;
    volatile unsigned int *gpio_cleardataout_addr1;
    unsigned int reg1;
    volatile unsigned int *button1;

    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO1_START_ADDR, GPIO1_END_ADDR, GPIO1_SIZE);

    gpio_addr = mmap(0, GPIO0_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);
    gpio_addr1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;
    gpio_oe_addr1           = gpio_addr1 + GPIO_OE;
    gpio_setdataout_addr1   = gpio_addr1 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr1 = gpio_addr1 + GPIO_CLEARDATAOUT;
    gpio_datain_addr = gpio_datain_addr + GPIO_DATAIN;
    gpio_datain_addr1 = gpio_datain_addr1 + GPIO_DATAIN;
    

    if(gpio_addr == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    if(gpio_addr1 == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    //printf("GPIO mapped to %p\n", gpio_addr);
    //printf("GPIO OE mapped to %p\n", gpio_oe_addr);
    //printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr);
    //printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr);

    // Set USR3 to be an output pin
    reg = *gpio_oe_addr;
    reg1 = *gpio_oe_addr1;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~USR3;       // Set USR3 bit to 0
    reg1 &= ~USR3;
    *gpio_oe_addr = reg;
    *gpio_oe_addr1 = reg1;
    //printf("GPIO1 configuration: %X\n", reg);
    //printf("GPIO1 configuration: %X\n", reg1);

    //printf("Start blinking LED USR3\n");
    while(keepgoing) {
	if(*gpio_setdataout_addr = GPIO_07){
            // printf("ON\n");
            *gpio_setdataout_addr = USR3;
            // printf("OFF\n");
	}
        if(*gpio_setdataout_addr = GPIO_60){
            // printf("ON\n");
            *gpio_setdataout_addr = USR2;
            // printf("OFF\n");
	}
    }

    munmap((void *)gpio_addr, GPIO0_SIZE);
    munmap((void *)gpio_addr1, GPIO1_SIZE);
    close(fd);
    return 0;
}
