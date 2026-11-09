#include "kernel/types.h"
#include "user/user.h"

// a chain of processes: each one reads numbers from "in",
// prints the first one (a prime p) and sends the numbers
// that are not divisible by p to its child, the next stage
void
sieve(int in)
{
    for(;;){
        int p, n;
        if(read(in, &p, sizeof(p)) != sizeof(p)){
            close(in);
            exit(0);                   // no more numbers: the chain ends
        }
        printf("prime %d\n", p);

        int fd[2];
        pipe(fd);
        if(fork() == 0){
            // the child becomes the next stage and reads from fd[0]
            close(fd[1]);
            close(in);
            in = fd[0];
            continue;
        }
        close(fd[0]);
        while(read(in, &n, sizeof(n)) == sizeof(n)){
            if(n % p != 0)
                write(fd[1], &n, sizeof(n));
        }
        close(in);
        close(fd[1]);                  // the next stage sees end of input
        wait(0);
        exit(0);
    }
}

int
main(int argc, char *argv[])
{
    int fd[2];
    pipe(fd);
    if(fork() == 0){
        close(fd[1]);
        sieve(fd[0]);
    }
    close(fd[0]);
    for(int i = 2; i <= 35; i++)
        write(fd[1], &i, sizeof(i));
    close(fd[1]);
    wait(0);
    exit(0);
}
