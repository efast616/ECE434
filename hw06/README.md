
1. Julia Cartwright works at National instruments

2. PREEMT_RT is a real time kernel patch that embedded projects use for a real time operating system

3. mixed criticallity is running tasks where some are time critical while others are not

4. drivers can misbehave because the stacks are shared between the real time tasks and the non real time tasks

5. The delta in figure 5 is the time between the external event and the time of the application

6. cyclictest is a test which takes a time stamp, sleeps for a set duration and then takes another time stamp

   when the sleep is over the difference between the time stamps can be used to characterize the delta

7. Figure 2 shows the difference between the preempt and the preempt_rt patch

8. dispatch latency is the amount of time it takes between the hardware actually firing to the interrupt for the 

   relevant thread to be woken up  scheduling latency is the amount of time it takes after the scheduler has been 

   made aware that a high priority task needs to be run

9. mainline is a model to show how tasks will be run

10. the low priority interupt is keeping the external event from firing

11. the external event can start sooner because of the irq threads this is due to threads being able to be preempted


HEAD output 

	real	1m40.190s
	
	user	0m0.503s

	sys	0m3.421s

=======
For the plots I used the folowing command as a load
	
	stress --cpu 1 --io 1 --vm 1

The RT kernel does have a bounded latency and this can be seen by the spikes that are farther along the x axis in teh loaded case

## Prof. Yoder's comments
Looks good.  You loaded plot doesn't look right.  I'd expect the RT kernel to be
much more bounded.

Late: -1
Grade:  9/10

Project Wiki is started  10/10