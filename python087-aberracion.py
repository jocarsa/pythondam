import os
import time

programaenc = '#include <stdio.h>\n int main(int argc, char *argv[]) {printf("Soy una aberracioooooon");return 0;}'


archivo = open("aberracion.c",'w')
archivo.write(programaenc)
archivo.close()

os.system('gcc aberracion.c -o aberracion')

os.system('./aberracion')
