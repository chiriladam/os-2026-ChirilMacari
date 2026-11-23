// user/uthread_switch.S - Lab 18 (Chiril-Adam Macari, FAF-243)
//
//   void thread_switch(struct context *old, struct context *new);
//
// Shaped like the kernel swtch (kernel/swtch.S): save the callee-saved
// registers of the current thread into *old (a0), load the ones of the
// next thread from *new (a1), and ret: ra now holds the next thread's
// return address, so execution continues in the next thread.

        .text
        .globl thread_switch
thread_switch:
        sd ra, 0(a0)            # save current thread registers
        sd sp, 8(a0)
        sd s0, 16(a0)
        sd s1, 24(a0)
        sd s2, 32(a0)
        sd s3, 40(a0)
        sd s4, 48(a0)
        sd s5, 56(a0)
        sd s6, 64(a0)
        sd s7, 72(a0)
        sd s8, 80(a0)
        sd s9, 88(a0)
        sd s10, 96(a0)
        sd s11, 104(a0)

        ld ra, 0(a1)            # load next thread registers
        ld sp, 8(a1)
        ld s0, 16(a1)
        ld s1, 24(a1)
        ld s2, 32(a1)
        ld s3, 40(a1)
        ld s4, 48(a1)
        ld s5, 56(a1)
        ld s6, 64(a1)
        ld s7, 72(a1)
        ld s8, 80(a1)
        ld s9, 88(a1)
        ld s10, 96(a1)
        ld s11, 104(a1)

        ret                     # return into the next thread
