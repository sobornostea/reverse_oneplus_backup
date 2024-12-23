# OnePlus Backup Decrypt tool

The OnePlus backup app allows you to backup your contacts, SMS history, call logs...
to transfer it to a new device. Unfortunately, if you manually copied the files, 
you cannot make use of the backup as it is encrypted you should've done the transfer
with their proprietary backup app x)

Fortunately for us, the OnePlus app keeps the IV and a random string from which the 
key is generated. The derivation process is obfuscated, but we can reverse the app
and get the key that will allow us to decrypt our backups

# How to use ?

Make sure to extract the iv and randomness from the `backup_config_new.db` file
and pass a path to your file as the first argument of `decrypt.py`.  

I've added a sample (anonymized) database and a `speeddial_backup.xml` file to test it

# Security comments

The encryption process is pretty bad as they reuse the IV for
every file and lose more than half of the entropy in the derivation process.

This choice of obfuscation certainly says something.

This was disclosed to OnePlus and they did not care.

# Credit

Most if not all of the reverse work was done by a friend of
mine, all credit goes to her
