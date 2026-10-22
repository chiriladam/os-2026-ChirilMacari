#include "kernel/types.h"
#include "user/user.h"

int
main(int argc, char *argv[])
{
  if(argc != 2){
    fprintf(2, "usage: sleep <ticks>\n");
    exit(1);
  }
  // In current xv6 the sleep system call is named pause()
  // (renamed from sleep() in Aug 2025).
  pause(atoi(argv[1]));   // system call into the kernel
  exit(0);
}
