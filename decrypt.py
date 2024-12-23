from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hmac
import sys

# input and output paths
in_path = sys.argv[1]
out_path = in_path + ".out"

# values from "backup_config_new.db" SQLite database
random = "rnayE49mE5XjHKvWeiFrm3gESTS2fDOe"
iv = "7087977048519264718"

# the 'BackupRestoreFile' asset in the APK contains a very long base64 string,
# which is indexed by a list of 16 hardcoded integers (x4.a.f10038b),
# and then concatenated with the 'BackupRestoreFile_salt' asset containing 16 characters,
# to form the following 32 character (256 bit) "secret" string:
secret = "rTMVTmZYZVMTTEGt-Backup_Restore-"

# the final key and IV are derived as follows:
digest = hmac.digest(random.encode(), secret.encode(), "sha256")
key = "".join(hex(b >> 4)[2] for b in digest).encode()
iv = iv[:16].encode()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = cipher.decryptor()
with open(out_path, "wb") as out:
	for chunk in open(in_path, "rb"):
		out.write(decryptor.update(chunk))
	out.write(decryptor.finalize())
