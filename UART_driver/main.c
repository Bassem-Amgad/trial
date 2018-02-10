/*
 * main.c

 *
 *  Created on: 7 Oct 2017
 *      Author: Bassem
 */
//#include <util/delay.h>
#include "Types.h"
#include "utilss.h"
#include "DIO.h"
#include "UART.h"
#include "LCD.h"

#define asci_conv 48

int main (void)
{
	UART_voidInit ();
	LCD_voidInit ();
	extern u8 UART_NewValue;
	extern UART_State UART_CurrentState;
	u8 i=0;
	u8 data_recieve=0;

	DIO_voidSetDirection(DIO_u8PinD1,DIO_u8PinIp);
	DIO_voidSetDirection(DIO_u8PinD0,DIO_u8PinOp);
	DIO_voidSetDirection(DIO_u8PinB3,DIO_u8PinOp);
	DIO_voidWritePIN(DIO_u8PinB3,DIO_u8LOW);
	DIO_voidSetDirection(DIO_u8PinB5,DIO_u8PinIp);

	LCD_voidWriteCommand(0x80);
	LCD_voidDisplay('N');
	LCD_voidDisplay('u');
	LCD_voidDisplay('m');
	LCD_voidDisplay('b');
	LCD_voidDisplay('e');
	LCD_voidDisplay('r');
	LCD_voidDisplay(' ');
	LCD_voidDisplay('i');
	LCD_voidDisplay('s');
	LCD_voidDisplay(' ');
	LCD_voidWriteCommand(0xc0);
	while(1)
	{
		if (DIO_u8ReadPIN(DIO_u8PinB5))
			{
				if (i<9)
					{
						u8 chk = UART_u8Transmit (1+i);
						if (chk ==UART_OK)
						{
							i++;
							//_delay_us(1300);
							if (i==9)
								{
									DIO_voidWritePIN(DIO_u8PinB3,DIO_u8HIGH);
								}
						}
					}
			}
		else
			{
				if (UART_CurrentState == UART_STATE_RX_DONE)
					{
						data_recieve=UART_NewValue;
						UART_CurrentState =UART_STATE_INIT;
						i++;
						LCD_voidDisplay((48+data_recieve));
						if (i==9)
							{
								DIO_voidWritePIN(DIO_u8PinB3,DIO_u8HIGH);
							}
						else
							{
							DIO_voidWritePIN(DIO_u8PinB3,DIO_u8LOW);
							}
					}
			}
	}
}
