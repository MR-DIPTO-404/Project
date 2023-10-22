# WRITTEN BY MR.DIPTO
# FOLLOW MY GITHUB : https://github.com/MR-DIPTO-404
#------------- IMPORT ------------#
from os import system as c
import marshal
import base64
import zlib
try:
    from Cython.Build.BuildExecutable import build as execute
except:
    c('pip install cython >/dev/null')
#---------------- LOGO -----------#
logo='''
`7MM"""YMM  `7MN.   `7MF' .g8"""bgd 
  MM    `7    MMN.    M .dP'     `M 
  MM   d      M YMb   M dM'       ` 
  MMmmMM      M  `MN. M MM          
  MM   Y  ,   M   `MM.M MM.         
  MM     ,M   M     YMM `Mb.     ,' 
.JMMmmmmMMM .JML.    YM   `"bmmmd'
'''
#--------------- CLEAR FUNCTION -------------#
def clear():
    c('clear')
    print(logo)
    print(40*'-')
    print(' FB PAGE : PING WORLD ')
    print(' GITHUB  : MR-DIPTO-404')
    print(40*'-')
#----------- MAIN FUNCTION ------------#
def main():
    clear()
    print(' [A] MARSHAL ENCRYPTION ')
    print(' [B] BASE64  ENCRYPTION ')
    print(' [C] ZLIB    ENCRYPTION ')
    print(' [D] CYTHON  EXECUTABLE ')
    print(' [E] EXIT TERMINAL ')
    print(40*'-')
    option=input(' [?] CHOICE MENU : ')
    if option in ['a','A']:
        marshal_enc()
    elif option in ['b','B']:
        base64_enc()
    elif option in ['c','C']:
        zlib_enc()
    elif option in ['d','D']:
        cython_executable()
    else:
        exit(' TOOL EXITED :/')
#----------- MARSHAL ENCRYPTION --------------#
def marshal_enc():
    clear()
    file=input(' ENTER SOURCE FILE NAME : ')
    filex=input(' ENTER OUTPUT FILE NAME : ')
    try:
        file_open=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write(run_code)
    out_put.close()
    print(40*'-')
    print(' [✓✓] ENCRYPTION COMPLETE :/ ')
    print(' [✓✓] OUTPUT FILE SAVE AS : '+filex)
#---------- BASE64 ENCRYPTION ------------#
def base64_enc():
    clear()
    input_file=input(' ENTER SOURCE FILE PATH : ')
    output_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        file_open=open(input_file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR !!')
    compile=base64.b64encode(file_open.encode())
    run_code=f'import base64\nexec(base64.b64decode({compile}))'
    out_put=open(output_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+output_file)
#---------------- ZLIB ENCRYPTION -----------------#
def zlib_enc():
    clear()
    src=input(' ENTER SOURCE FILE PATH : ')
    save_file=input(' ENTER OUTPUT FILE PATH : ')
    try:
        src_file=open(src,'r').read()
    except:
        exit(' FILE NOT FOUND !!')
    compile_zlib=zlib.compress(src_file.encode())
    run_code=f'import zlib\nexec(zlib.decompress({compile_zlib}).decode())'
    out_put=open(save_file,'w')
    out_put.write(run_code)
    out_put.close()
    print(' [✓✓] ENCRYPTION COMPLETE :/')
    print(' [✓✓] ENC FILE SAVE AS : '+save_file)
#--------------- CYTHON EXECUTABLE -----------------#
def cython_executable():
    clear()
    file=input(' ENTER SOURCE FILE PATH : ')
    try:
        filex=open(file,'r').read()
    except:
        exit(' FILE NOT FOUND ERROR :/')
    error=filex.replace('	','    ')
    solve=open(file,'w').write(error)
    execute(file)
    clear()
    print(' [✓✓] CYTHON EXECUTABLE COMPLETE :")')
    save=file[:-3]
    print(' [✓✓] EXECUTABLE FILE SAVE AS : '+save)
#----------------- END --------------#
main()