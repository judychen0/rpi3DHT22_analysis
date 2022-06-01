====================================================
Code for sending serial commands to HITACHI via ssh
====================================================

>> serial_write_*.py
   set the program you wan to run on HITACHI
   1. Using "onestep()" function to modify the steps' goal temperature and arrival time
   2. Using "returnstep()" function to modify the repeating cycles and the cycled steps

>> serial_close.py
   stop the HITACHI and clean the current program setting

>> serial_pause.py
   stop the HITACHI and do not clean program setting
   