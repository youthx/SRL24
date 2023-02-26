####################################################################################
# DONT RUN THIS, IT DOESNT WORK, IT WAS FOR SOME DEBUGGING AND IS NOT NEEDED ANYMORE
####################################################################################

if [[ "$OSTYPE" != "win32" ]]; then
    echo WARNING: OS ENVIRONMENT MAY NOT BE COMPATIBLE WITH WIN32API
fi

echo PACKAGES > package.pack
pip install pywin32 && echo [pywin32] 1 > package.pack
pip install requests && echo [requests] 1 > package.pack
pip install tkinter  && echo [tkinter] 1 > package.pack
echo DONE > package.pack 
echo installed pywin32, requests, tkinter
python3 srl24.py 

