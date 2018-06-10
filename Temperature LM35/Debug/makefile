################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
LSS += \
fatmaaaaaaaaas_25r_7aga.lss \

FLASH_IMAGE += \
fatmaaaaaaaaas_25r_7aga.hex \

SIZEDUMMY += \
sizedummy \

AVRDUDEDUMMY += \
avrdudedummy \


# All Target
all: fatmaaaaaaaaas_25r_7aga.elf secondary-outputs

# Tool invocations
fatmaaaaaaaaas_25r_7aga.elf: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: AVR C Linker'
	avr-gcc -Wl,-Map,fatmaaaaaaaaas_25r_7aga.map -mmcu=atmega32 -o "fatmaaaaaaaaas_25r_7aga.elf" $(OBJS) $(USER_OBJS) $(LIBS)
	@echo 'Finished building target: $@'
	@echo ' '

fatmaaaaaaaaas_25r_7aga.lss: fatmaaaaaaaaas_25r_7aga.elf
	@echo 'Invoking: AVR Create Extended Listing'
	-avr-objdump -h -S fatmaaaaaaaaas_25r_7aga.elf  >"fatmaaaaaaaaas_25r_7aga.lss"
	@echo 'Finished building: $@'
	@echo ' '

fatmaaaaaaaaas_25r_7aga.hex: fatmaaaaaaaaas_25r_7aga.elf
	@echo 'Create Flash image (ihex format)'
	-avr-objcopy -R .eeprom -R .fuse -R .lock -R .signature -O ihex fatmaaaaaaaaas_25r_7aga.elf  "fatmaaaaaaaaas_25r_7aga.hex"
	@echo 'Finished building: $@'
	@echo ' '

sizedummy: fatmaaaaaaaaas_25r_7aga.elf
	@echo 'Invoking: Print Size'
	-avr-size --format=avr --mcu=atmega32 fatmaaaaaaaaas_25r_7aga.elf
	@echo 'Finished building: $@'
	@echo ' '

avrdudedummy: fatmaaaaaaaaas_25r_7aga.elf
	@echo 'Invoking: AVRDude'
	C:\WinAVR-20100110\bin\avrdude -pm32 -cusbasp -Uflash:w:fatmaaaaaaaaas_25r_7aga.hex:a
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(OBJS)$(C_DEPS)$(ASM_DEPS)$(FLASH_IMAGE)$(ELFS)$(LSS)$(AVRDUDEDUMMY)$(S_DEPS)$(SIZEDUMMY)$(S_UPPER_DEPS) fatmaaaaaaaaas_25r_7aga.elf
	-@echo ' '

secondary-outputs: $(LSS) $(FLASH_IMAGE) $(SIZEDUMMY) $(AVRDUDEDUMMY)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
