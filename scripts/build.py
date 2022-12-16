#!/usr/bin/python3

import os


if __name__ == '__main__':
    # Todo: создание floppy образа
    '''
    os.system("dd if=/dev/zero of=floppy.img bs=512 count=2880")
    os.system("losetup /dev/loop0 floppy.img")
    os.system("mkdosfs -F 12 /dev/loop0")
    os.system("mount -t ext2 /dev/loop0 /mnt/beluga_os_floppy")
    os.system("mkdir /mnt/beluga_os_floppy/grub")
    '''
    
    os.system("i686-elf-gcc -finput-charset=UTF-8 -fextended-identifiers -ffreestanding  -march=i486 -ggdb -Wall -Wextra -O0 -g -I include// -c kernel.c -o bin/kernel.o")
    os.system("i686-elf-gcc -finput-charset=UTF-8 -fextended-identifiers -ffreestanding  -march=i486 -ggdb -Wall -Wextra -O0 -g -I include// -c start.s -o bin/start.o")
    os.system("i686-elf-gcc -ffreestanding -nostdlib -g -T linker.ld bin/start.o bin/kernel.o -o isodir/kernel.elf")
    os.system("i686-elf-strip  -s -K mmio -K fb -K bootboot -K environment -K initstack isodir/kernel.elf")
    os.system("i686-elf-readelf -hls isodir/kernel.elf>kernel.elf.txt")

    os.system("wsl grub-mkrescue isodir -o BelugaOS.iso")
    
