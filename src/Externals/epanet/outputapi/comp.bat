set PATH=C:\MinGW\bin;C:\Users\Mark\Anaconda2;C:\Users\Mark\Anaconda2\Scripts;C:\Users\Mark\Anaconda2\Library\bin;C:\ProgramData\Oracle\Java\javapath;C:\Program Files\Common Files\Microsoft Shared\Windows Live;C:\Program Files (x86)\Common Files\Microsoft Shared\Windows Live;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files\TortoiseSVN\bin;C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;C:\Program Files (x86)\Microsoft SDKs\TypeScript\1.0\;C:\Program Files (x86)\Windows Live\Shared;C:\Program Files(x86)\GtkSharp\2.12\bin;C:\Program Files (x86)\Git\cmd;C:\Program Files (x86)\Git\bin;C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;C:\Program Files (x86)\Skype\Phone\;C:\Users\Mark\.dnx\bin;C:\Program Files\MicrosoftDNX\Dnvm\;C:\Program Files\doxygen\bin;C:\Program Files\TortoiseGit\bin
gcc -m64 outputapi.c -c
gcc -m64 -shared -o outputapi.dll *.o
rem gcc test.c -c
rem gcc -o test.exe test.o -L. -l outputapi -lm