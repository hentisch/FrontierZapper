Note: Much of this description of the file format was mostly derived from it's [XentaxWiki entry](http://wiki.xentax.com/index.php/Frontier_Developments_ZAP) 

# Header Bytes
Bytes [0x0-0x3] - "ZAP" + null, this is a constnat between all ZAP archives
Bytes [0x04-0x07] - The size of each file. This is a constant - though different files will occupy different amounts of this space.
Bytes [0x08-0x0F] - The function of these bytes isn't currently understood, though they seemingly don't have anything to do with the file structure

# Bytes Per File
Note that for this description, I will use 0x0 as the "start" of the file description, even though no file description could exist in this position

Bytes [0x0-0x3]: A Hash / Checksum (Maybe)
> When the file is a directory, this is 2573

[0x04-0x05]: A File Type ID
> When this is a directory, this is 0
> Some files (so far only documentation) also have 0 file type ids

[0x06-0x07]: The Length of the name of the file/directory
> This includes a null terminator
> Let this length be $n$

[0x07-0x$n+7-1$]: The directory name

Next 1 byte: A null terminator 

# Directory Structure
As noted earlier, zap files can contain directory structures.

To create a directory, simply create a file entry, as described above, with the relavent file id, and a / at the end of the file name

Every file after the creation of a directory will be considered as belonging in that directory. The only way to make subsequent files not a part of that directory is to use the following sequence of bytes: "0D 0A 00 00 00 00 03 00 2E 2E 00". This can be thought of similarly to using "cd ../" on *nix systems.

# Reading File Bytes
TODO