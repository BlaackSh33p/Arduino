import os
import machine

# Firmware + platform info
print("uname:", os.uname())

# CPU frequency
print("CPU freq:", machine.freq(), "Hz")

# Unique chip ID (ESP32 MAC address)
chip_id = machine.unique_id()
print("Unique ID:", chip_id, " → hex:", "".join("{:02x}".format(b) for b in chip_id))

# Reset cause
causes = {
    machine.PWRON_RESET: "Power on",
    machine.HARD_RESET: "Hard reset",
    machine.WDT_RESET: "Watchdog reset",
    machine.DEEPSLEEP_RESET: "Woke from deep sleep",
    machine.SOFT_RESET: "Soft reset"
}
print("Reset cause:", causes.get(machine.reset_cause(), machine.reset_cause()))

# Flash size (ESP32 specific)
try:
    import esp
    print("Flash size:", esp.flash_size() // (1024 * 1024), "MB")
except ImportError:
    print("esp module not available")
