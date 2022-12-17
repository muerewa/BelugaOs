#!/usr/bin/python3

from sys import platform
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
    os.system("mkdir bin/")
    
    os.system("i686-elf-gcc -finput-charset=UTF-8 -fextended-identifiers -ffreestanding  -march=i486 -ggdb -Wall -Wextra -O0 -g -I include// -c kernel.c -o bin/kernel.o")
    os.system("i686-elf-gcc -finput-charset=UTF-8 -fextended-identifiers -ffreestanding  -march=i486 -ggdb -Wall -Wextra -O0 -g -I include// -c start.s -o bin/start.o")
    os.system("i686-elf-gcc -ffreestanding -nostdlib -g -T linker.ld bin/start.o bin/kernel.o -o isodir/kernel.elf")
    os.system("i686-elf-strip  -s -K mmio -K fb -K bootboot -K environment -K initstack isodir/kernel.elf")
    os.system("i686-elf-readelf -hls isodir/kernel.elf>kernel.elf.txt")

    #os.system("grub-mkrescue isodir -o BelugaOS.iso")
    
    LIMINE_XORRISO = "-b limine-cd.bin -no-emul-boot -boot-load-size 4 -boot-info-table --efi-boot limine-cd-efi.bin -efi-boot-part --efi-boot-image "
    os.system(f"xorriso -as mkisofs {LIMINE_XORRISO} --protective-msdos-label isodir -o BelugaOS-limine.iso")


    if platform == "linux" or platform == "linux2":
        os.system("./limine/limine-deploy BelugaOS-limine.iso")
    elif platform == "win32":
        os.system("cd limine/ && limine-deploy.exe ../BelugaOS-limine.iso && cd ..")

    
    #qemu-system-i386 -cdrom belugaos.iso -nographic
