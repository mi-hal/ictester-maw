#define F_CPU	16000000UL

#include <math.h>
#include <inttypes.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdint.h>
#include <avr/cpufunc.h>
#include "serial.h"

#define MAX_TEST_SIZE 1024

enum cmd {
	CMD_SETUP	= 0,
	CMD_UPLOAD	= 1,
	CMD_RUN		= 2,
};

enum result {
	RES_OK		= 0,
	RES_ERR		= 1,
	RES_PASS	= 2,
	RES_FAIL	= 3,
};

enum type {
	TYPE_COMB	= 0,
	TYPE_SEQ	= 1,
	TYPE_MEM	= 2,
	TYPE_MAX	= TYPE_MEM,
};

struct port {
	volatile uint8_t *port;
	volatile uint8_t *pin;
	uint8_t dut_used;
	uint8_t dut_input;
	uint8_t dut_pullup;
} port[3];

uint8_t test_type;
uint16_t test_len;
uint8_t test[MAX_TEST_SIZE][3];

// -----------------------------------------------------------------------
void reply(uint8_t res)
{
	serial_tx_char(res);
}

// -----------------------------------------------------------------------
void deconfigure(void)
{
	DDRA = 0;
	DDRB = 0;
	DDRC = 0;
	PORTA = 0;
	PORTB = 0;
	PORTC = 0;
}

// -----------------------------------------------------------------------
void setup(void)
{
	DDRA = port[0].dut_input & port[0].dut_used;
	DDRB = port[1].dut_input & port[1].dut_used;
	DDRC = port[2].dut_input & port[2].dut_used;
}

// -----------------------------------------------------------------------
void read_setup(uint8_t cmd)
{
	for (int i=0 ; i<3 ; i++) {
		port[i].dut_used = serial_rx_char();
		port[i].dut_input = serial_rx_char();
		port[i].dut_pullup = serial_rx_char();
	}

	reply(RES_OK);
}

// -----------------------------------------------------------------------
void upload(uint8_t cmd)
{
	test_type = serial_rx_char();
	test_len = (uint16_t) serial_rx_char() << 8;
	test_len += serial_rx_char();

	for (int pos=0 ; pos<test_len ; pos++) {
		for (int i=0 ; i<3 ; i++) {
			test[pos][i] = serial_rx_char();
		}
	}

	reply(RES_OK);
}

// -----------------------------------------------------------------------
uint8_t run_single(void)
{
	uint8_t i;
	uint8_t data;
	uint8_t pullup;
	uint8_t expected;

	uint8_t res = RES_PASS;
	for (int pos=0 ; pos<test_len ; pos++) {
		for (i=0 ; i<3 ; i++) {
			data = test[pos][i] & port[i].dut_input;
			pullup = port[i].dut_pullup & ~port[i].dut_input;
			*port[i].port = port[i].dut_used & (data | pullup);
		}
		_NOP();
		if ((test_type == TYPE_COMB) || ((test_type == TYPE_SEQ) && (pos%2))) {
			for (i=0 ; i<3 ; i++) {
				data = *port[i].pin & ~port[i].dut_input & port[i].dut_used;
				expected = test[pos][i] & ~port[i].dut_input & port[i].dut_used;
				if (data != expected) {
					res = RES_FAIL;
					break;
				}
			}
		}
	}
	return res;
}

//    pin:  7   6   5   4    3  2  1    0
// port A:  -  NC Din ~WE ~RAS A0 A2   A1
// port C: NC  a7  a5  a4   a3 a6 Do ~CAS 

#define PORT_RAS PORTA
#define PORT_WE  PORTA
#define PORT_DIN PORTA
#define PORT_CAS PORTC
#define IN_DOUT  PINC
#define PORT_AL  PORTA
#define PORT_AH  PORTC

// -----------------------------------------------------------------------
void mem_setup(void)
{
	DDRA  = 0b11111111;
	PORTA = 0b00011000;

	DDRC  = 0b11111101;
	PORTC = 0b00000001;

	// wait 100us after initialization
	_delay_us(100);
	// blink RAS 8 times before using the chip
	for (uint8_t i=0 ; i<8 ; i++) {
		PORTA = 0b00010000;
		PORTA = 0b00010000; // repeated twice, because 120ns min pulse
		PORTA = 0b00011000;
	}
}

#define ADDR_LOW(addr) (((addr) & 0b111))
#define ADDR_HIGH(addr) (((addr) & 0b11111000) >> 1)
#define DATA(data) (((data) & 1) << 5)
#define WE_OFF (1 << 4)
#define WE_ON 0
#define RAS_OFF (1 << 3)
#define RAS_ON
#define CAS_OFF (1 << 0)
#define CAS_ON 0

// -----------------------------------------------------------------------
uint8_t mem_test_bit(uint16_t addr, uint8_t data)
{
	uint8_t addr_col = addr & 0xff;
	uint8_t addr_row = addr >> 8;
	uint8_t dout;

	// write:

	// set row addr
	PORT_AL = ADDR_LOW(addr_row) | WE_OFF | RAS_OFF;
	PORT_AH = ADDR_HIGH(addr_row) | CAS_OFF;
	// RAS low
	PORT_AL &= ~RAS_OFF;
	// WE low
	PORT_AL &= ~WE_OFF;
	// data
	PORT_AL = (data & 1) << 5;
	// set column addr
	PORT_AL |= ADDR_LOW(addr_col);
	PORT_AH = ADDR_HIGH(addr_col) | CAS_OFF;
	// CAS low
	PORT_AH &= ~CAS_OFF;
	// WE high
	PORT_AL |= WE_OFF;
	// CAS high
	PORT_AH |= CAS_OFF;
	// RAS high
	PORT_AL |= RAS_OFF;
	// data 0
	PORT_AL &= ~0b00100000;

	// read:

	// set row addr
	PORT_AL = ADDR_LOW(addr_row) | WE_OFF | RAS_OFF;
	PORT_AH = ADDR_HIGH(addr_row) | CAS_OFF;
	// RAS low
	PORT_AL &= ~RAS_OFF;
	// set column addr
	PORT_AL = ADDR_LOW(addr_col) | WE_OFF;
	PORT_AH = ADDR_HIGH(addr_col) | CAS_OFF;
	// CAS low
	PORT_AH &= ~CAS_OFF;
	__asm__ __volatile__ ("nop");
	__asm__ __volatile__ ("nop");
	// wait for valid data
	dout = (IN_DOUT >> 1) & 1;
	// CAS high
	PORT_AH |= CAS_OFF;
	// RAS high
	PORT_AL |= RAS_OFF;

	if (dout == data) return RES_PASS;

	return RES_FAIL;
}

// -----------------------------------------------------------------------
uint8_t mem_test_page(uint16_t addr, uint8_t data)
{
	uint8_t res = RES_PASS;
	uint16_t addr_col;
	uint8_t addr_row = addr;
	uint8_t dout;

	// write:

	// set row addr
	PORT_AL = ADDR_LOW(addr_row) | WE_OFF | RAS_OFF;
	PORT_AH = ADDR_HIGH(addr_row) | CAS_OFF;
	// RAS low
	PORT_AL &= ~RAS_OFF;
	for (addr_col=0 ; addr_col<256 ; addr_col++) {
		// WE low
		PORT_AL &= ~WE_OFF;
		// data
		PORT_AL = (data & 1) << 5;
		// set column addr
		PORT_AL |= ADDR_LOW(addr_col);
		PORT_AH = ADDR_HIGH(addr_col) | CAS_OFF;
		// CAS low
		PORT_AH &= ~CAS_OFF;
		// WE high
		PORT_AL |= WE_OFF;
		// CAS high
		PORT_AH |= CAS_OFF;
	}
	// RAS high
	PORT_AL |= RAS_OFF;
	// data 0
	PORT_AL &= ~0b00100000;

	// read:

	// set row addr
	PORT_AL = ADDR_LOW(addr_row) | WE_OFF | RAS_OFF;
	PORT_AH = ADDR_HIGH(addr_row) | CAS_OFF;
	// RAS low
	PORT_AL &= ~RAS_OFF;
	for (addr_col=0 ; addr_col<256 ; addr_col++) {
		// set column addr
		PORT_AL = ADDR_LOW(addr_col) | WE_OFF;
		PORT_AH = ADDR_HIGH(addr_col) | CAS_OFF;
		// CAS low
		PORT_AH &= ~CAS_OFF;
		__asm__ __volatile__ ("nop");
		__asm__ __volatile__ ("nop");
		// wait for valid data
		dout = (IN_DOUT >> 1) & 1;
		// CAS high
		PORT_AH |= CAS_OFF;
		if (dout != data) {
			res = RES_FAIL;
			break;
		}
	}
	// RAS high
	PORT_AL |= RAS_OFF;

	return res;
}

// -----------------------------------------------------------------------
uint8_t run_mem(void)
{
	uint8_t res = RES_PASS;

	mem_setup();

	for (uint32_t addr=0 ; addr<256; addr++) {
		res = mem_test_page(addr, 0);
		if (res != RES_PASS) break;
		res = mem_test_page(addr, 1);
		if (res != RES_PASS) break;
	}

	return res;
}

// -----------------------------------------------------------------------
void run(uint8_t cmd)
{
	uint8_t res;

	uint8_t test_pow = serial_rx_char();
	int test_loops = pow(2, test_pow);

	for (int rep=0 ; rep<test_loops ; rep++) {
		if (test_type == TYPE_MEM) {
			res = run_mem();
		} else {
			res = run_single();
		}
		if (res != RES_PASS) {
			reply(RES_FAIL);
			return;
		}
	}

	reply(RES_PASS);
}

// -----------------------------------------------------------------------
int main(void)
{
	deconfigure();
	serial_init(500000);

	port[0].port = &PORTA;
	port[1].port = &PORTB;
	port[2].port = &PORTC;
	port[0].pin = &PINA;
	port[1].pin = &PINB;
	port[2].pin = &PINC;

	while (1) {
		int cmd = serial_rx_char();
		switch (cmd >> 5) {
			case CMD_SETUP:
				read_setup(cmd);
				break;
			case CMD_UPLOAD:
				upload(cmd);
				break;
			case CMD_RUN:
				setup();
				run(cmd);
				deconfigure();
				break;
			default:
				reply(RES_ERR);
		}
	}

	return 0;
}

// vim: tabstop=4 shiftwidth=4 autoindent
