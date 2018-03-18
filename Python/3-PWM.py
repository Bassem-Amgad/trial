# PWM FREQUENCY ISN'T ACCUARATE USING STANDARD LIBRARY DUE TO OS
# Mark pin for pwm GPIO.PWM(pin_number,frequency)
pwm_obj= GPIO.PWM(18,400)
# Start generating pwm signal object.start(duty_cycle)
# duty_cycle ranges from 0 to 100
pwm_obj.start(100)
# Assign new duty cycle object.ChangeDutyCycle(new_duty_cycle)
pwm_obj.ChangeDutyCycle(50)

# Frequency control
# do it manually
while True:
    GPIO.output(13,True)
    time.sleep(0.5)
    GPIO.output(13,False)
    time.sleep(0.5)
