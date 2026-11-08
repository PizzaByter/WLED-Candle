# scripts/upload_littlefs.py
import subprocess, pathlib
Import("env")
DATA = pathlib.Path(env["PROJECT_DIR"]) / "littlefs-builder" / "data-E1"
IMG  = pathlib.Path(env["PROJECT_DIR"]) / "littlefs-builder" / "E1-littlefs.bin"
IMG.parent.mkdir(exist_ok=True)
subprocess.check_call([
    "mklittlefs", "-c", str(DATA),
    "-p", "256", "-b", "4096", "-s", "0xF0000", str(IMG)
])
#subprocess.check_call([
#    "esptool.py", "--chip", "esp32c3",
    #"--port", env["UPLOAD_PORT"], "--baud", "921600",
#    "--port", "COM7", "--baud", "921600",
#    "write_flash", "0x310000", str(IMG)
#])