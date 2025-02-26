# SPDX-FileCopyrightText: 2023 DroZDi
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Orange Pi 5 Plus"""

from adafruit_blinka.microcontroller.rockchip.rk3588 import pin

# D pin number is ordered by physical pin sequence

# D1 = +3.3V
# D2 = +5V
D3 = pin.GPIO0_C0
# D4 = +5V
D5 = pin.GPIO0_B7
# D6 = GND
D7 = pin.GPIO1_D6
D8 = pin.GPIO1_A1
# D9 = GND
D10 = pin.GPIO1_A0
D11 = pin.GPIO1_A4
D12 = pin.GPIO3_A1
D13 = pin.GPIO1_A7
# D14 = GND
D15 = pin.GPIO1_B0
D16 = pin.GPIO3_B5
# D17 = +3.3V
D18 = pin.GPIO3_B6
D19 = pin.GPIO1_B2
# D20 = GND
D21 = pin.GPIO1_B1
D22 = pin.GPIO1_A2
D23 = pin.GPIO1_B3
D24 = pin.GPIO1_B4
# D25 = GND
D26 = pin.GPIO1_B5
D27 = pin.GPIO1_B7
D28 = pin.GPIO1_B6
D29 = pin.GPIO1_D7
# D30 = GND
D31 = pin.GPIO3_A0
D32 = pin.GPIO1_A3
D33 = pin.GPIO3_C2
# D34 = GND
D35 = pin.GPIO3_A2
D36 = pin.GPIO3_A5
D37 = pin.GPIO3_C1
D38 = pin.GPIO3_A4
# D39 = GND
D40 = pin.GPIO3_A3

# UART
UART1_TX_M1 = pin.GPIO1_B6
UART1_RX_M1 = pin.GPIO1_B7
UART3_TX_M1 = pin.GPIO3_B5
UART3_RX_M1 = pin.GPIO3_B6
UART4_TX_M2 = pin.GPIO1_B3
UART4_RX_M2 = pin.GPIO1_B2
UART6_TX_M1 = pin.GPIO1_A1
UART6_RX_M1 = pin.GPIO1_A0
UART7_TX_M2 = pin.GPIO1_B5
UART7_RX_M2 = pin.GPIO1_B4
UART8_TX_M1 = pin.GPIO3_A2
UART8_RX_M1 = pin.GPIO3_A3

# Default UART
TX = UART6_TX_M1
RX = UART6_RX_M1
TXD = UART6_TX_M1
RXD = UART6_RX_M1

# I2C
I2C2_SCL_M0 = pin.GPIO0_B7
I2C2_SDA_M0 = pin.GPIO0_C0
I2C2_SCL_M4 = pin.GPIO1_A1
I2C2_SDA_M4 = pin.GPIO1_A0
I2C4_SCL_M3 = pin.GPIO1_A3
I2C4_SDA_M3 = pin.GPIO1_A2
I2C5_SCL_M3 = pin.GPIO1_B6
I2C5_SDA_M3 = pin.GPIO1_B7
I2C8_SCL_M2 = pin.GPIO1_D6
I2C8_SDA_M2 = pin.GPIO1_D7

# Default I2C
SCL = I2C2_SCL_M0
SDA = I2C2_SDA_M0

# SPI
SPI0_MISO_M2 = pin.GPIO1_B1
SPI0_MOSI_M2 = pin.GPIO1_B2
SPI0_CLK_M2 = pin.GPIO1_B3
SPI0_CS1_M2 = pin.GPIO1_B5
SPI0_CS0_M2 = pin.GPIO1_B4
SPI4_MISO_M1 = pin.GPIO3_A0
SPI4_MOSI_M1 = pin.GPIO3_A1
SPI4_CLK_M1 = pin.GPIO3_A2
SPI4_CS1_M1 = pin.GPIO3_A4
SPI4_CS0_M1 = pin.GPIO3_A3
SPI4_MISO_M2 = pin.GPIO1_A0
SPI4_MOSI_M2 = pin.GPIO1_A1
SPI4_CLK_M2 = pin.GPIO1_A2
SPI4_CS0_M2 = pin.GPIO1_A3

# Default SPI
MOSI = SPI0_MOSI_M2
MISO = SPI0_MISO_M2
SCLK = SPI0_CLK_M2
CS1 = SPI0_CS1_M2
CS0 = SPI0_CS0_M2

# CAN

CAN0_RX_M0 = pin.GPIO0_C0
CAN0_TX_M0 = pin.GPIO0_B7
CAN1_RX_M0 = pin.GPIO3_B5
CAN1_TX_M0 = pin.GPIO3_B6