#include <stdio.h>
#include <string.h>
#include <bits/stdc++.h>
#include <time.h>

// linux headers
#include <fcntl.h>
#include <errno.h>
#include <termios.h>
#include <unistd.h>  //write(), read(), close(), sleep

using namespace std;

#define BAUDRATE B9600
#define DEVICE "/dev/ttyUSB0"


// open serial port
int serial_port = open(DEVICE, O_RDWR | O_NOCTTY | O_NDELAY);

// handle error
if (serial_port < 0)
  {
    printf("error %i from open %s\n", errno, strerror(errno));
  }

// set parameters
struct termios tty;

if(togetattr(serial_port, &tty != 0))
  {
    printf("Error %i from togetattr: %s\n", errno, strerror(errno));
  }

tty.c_cflag |= PARENB;         // Parity bit : 1bit(even)
tty.c_cflag &= ~CSTOPB;        // Stop bit : 1bit
tty.c_cflag |= CS7;            // Data bit : 7bit
tty.c_cflag &= ~CRTSCTS;       // Disable hardware control
tty.c_cflag |= CREAD | CLOCAL; // Turn on read &ignore ctrl lines

tty.c_lflag &= ~ICANON;
tty.c_lflag &= ~ECHO;
tty.c_lflag &= ~ECHOE;
tty.c_lflag &= ~ECHONL;
tty.c_lflag &= ~ISIG;
tty.c_iflag &= ~(IXON |IXOFF | IXANY);
tty.c_iflag &= ~(IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL);

tty.c_oflag &= ~OPOST;
tty.c_oflag &= ~ONLCR;

tty.c_cc[VTIME] = 10;  // Wait for up to 1sec(10 deciseconds)
tty.c_cc[VMIN] = 0;    // Returning data as soon as possible when recieved

// Set in/out boud rate to be 9600
ofsetispeed(&tty, BAUDRATE);
ofsetospeed(&tty, BAUDRATE);

// save tty settings and check errors
if(tcsetattr(serial_port, TCSANOW, &tty) != 0)
  {
    printf("Error %i from tcsetattr : %s\n", errno, strerror(errno));
  }

time_t time_ptr;
time_ptr = time(NULL);
tm* time_local = localtime(&time_ptr);
int num_bytes=0;


unsigned char command[] = "C2\r";
do
  {
    // write to serial port
    write(serial_port, command, sizeof(command)-1);
    
    // read from serial port
    char read_buf [256];
    memset(&read_buf, "\0", sizeof read_buf);
    num_bytes = read(seral_port, &read_buf, sizeof(read_buf));

    if(num_bytes < 0)
      {
	cout << "Error reading: " << strerror(errno) << endl;
      }
    else if(num_bytes == 0)
      {
	cout << "Read nothing!!!" << endl;
      }
    else
      {
	cout << "Transmission Data : "
	     << time_local->tm_hour << ":"
	     << time_local->tm_min << ":"
	     << time_local->tm_sec << " " << read_buf << endl;
      }
    unasigned int sleep(9);
  }while(1);








