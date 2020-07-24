# 'Local IP': ('Server Type', 'Server Name'),
# Name and type are optional.
# 'Local IP': ('',''),
# Should work fine ^
SERVER_NAMES = {
    '192.168.1.2':('Production','Ubuntu Server'),
    '192.168.1.7':('Backup','Raspberry Pi'),
    '192.168.1.9':('Staging',"Bobs-PC")
}

# Port Number:'Description',
# Desciption is optional too.
# Port Number:'',
# Should work fine ^
PORTS = {
    25:'SMTP',
    21:'FTP',
    22:'SSH',
    993:'IMAP',
    143:'IMAP',
    587:'SMTP',
    443:'HTTPS',
    80:'HTTP'
}