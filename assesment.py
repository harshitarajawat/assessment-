import psutil
import speedtest
import platform
import ctypes
import socket
import os
from pygetwindow import getWindowsWithTitle

def get_installed_software():
    software_list = []
    for p in psutil.process_iter(['pid', 'name']):
        software_list.append(p.info['name'])
    return list(set(software_list))

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / (1024 * 1024)  # Convert to Mbps
    upload_speed = st.upload() / (1024 * 1024)  # Convert to Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def get_screen_size():
    window_title = getWindowsWithTitle(os.path.basename(__file__))[0]
    return window_title.width, window_title.height

def get_cpu_info():
    return platform.processor(), psutil.cpu_count(logical=False), psutil.cpu_count()

def get_gpu_info():
    try:
        import GPUtil
        gpu = GPUtil.getGPUs()[0]
        return gpu.name
    except ImportError:
        return "GPUtil library not installed. Install using: pip install gputil"

def get_ram_size():
    return round(psutil.virtual_memory().total / (1024 ** 3), 2)

def get_screen_size():
    window_title = getWindowsWithTitle(os.path.basename(__file__))[0]
    return window_title.width, window_title.height

def get_network_info():
    try:
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2, 7)][::-1])
    except NameError:
        mac = "UUID library not installed. Install using: pip install uuid"

    ip = socket.gethostbyname(socket.gethostname())
    return mac, ip

def get_public_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        return "No internet connection"

def get_windows_version():
    return platform.version()

if __name__ == "__main__":
    print("Installed Software: ", get_installed_software())
    download_speed, upload_speed = get_internet_speed()
    print(f"Internet Speed: Download = {download_speed:.2f} Mbps, Upload = {upload_speed:.2f} Mbps")
    print("Screen Resolution: ", get_screen_resolution())
    print("Screen Size: ", get_screen_size())
    cpu_model, num_cores, num_threads = get_cpu_info()
    print(f"CPU Model: {cpu_model}, Cores: {num_cores}, Threads: {num_threads}")
    print("GPU Model: ", get_gpu_info())
    print("RAM Size: ", get_ram_size(), "GB")
    mac_address, ip_address = get_network_info()
    print("Network Information: MAC Address =", mac_address, ", IP Address =", ip_address)
    print("Public IP Address: ", get_public_ip())
    print("Windows Version: ", get_windows_version())
