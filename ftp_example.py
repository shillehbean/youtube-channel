from ftplib import FTP

print('Testing')
ftp = FTP('ftp.dlptest.com', 21, 'dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
ftp.pwd()
ftp.retrlines('LIST')
print('Done Connecting')
