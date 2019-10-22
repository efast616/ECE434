#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const button = 'P9_23';
const LED1 = 'P9_14';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);
b.pinMode(LED1, b.OUTPUT);

const AUTH = 'N1px31-__MUtyURliOoGUridpQrAvlc3';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v2 = new blynk.VirtualPin(2);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v2.on('write', function(param) {
    var duty_cycle = param[0];
    console.log('V2:', duty_cycle);
    b.analogWrite(LED1, duty_cycle);
});


v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();
}
