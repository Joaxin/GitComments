@echo off
5:          
echo 1 Open Wifi
echo 2 Kill Wifi
echo 3 Bulid Wifi
echo 4 Look at Wifi
set /p k=Plz input£º
if /i %k%==1 goto 1
if /i %k%==2 goto 2
if /i %k%==3 goto 3
if /i %k%==4 goto 4
echo illeagal input must in 1,2,3,4
pause
cls
goto 5

:1
cls
rem Ìí¼ÓÐéÄâÎÞÏßÍøÂç 
netsh wlan set hostednetwork mode=allow ssid="Quizas Quizas Quizas" key=123456788 keyUsage=persistent 
rem Æô¶¯ÐéÄâÎÞÏßÍøÂç 
netsh wlan start hostednetwork 
rem "Í£Áô3ÃëÖÓ" 
ping -n 3 127.1>nul 
rem "³ÌÐòÍË³ö" 
exit

:2
netsh wlan stop hostednetwork
netsh wlan set hostednetwork mode=disallow
exit

:3
cls
set /p name=plz input your wifi's name£º
cls
set /p secrect=£ºAnd its password(Length 8~16)
netsh wlan set hostednetwork mode=allow ssid=%name% key=%secrect%
netsh wlan start hostednetwork
echo.
exit

:4
cls
netsh wlan show hostednetwork
pause
exit

