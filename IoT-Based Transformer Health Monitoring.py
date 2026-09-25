# IoT-Based Transformer Health Monitoring System
# Python Simulation

print("===== IoT TRANSFORMER HEALTH MONITORING =====")

temperature = float(input("Enter Temperature (°C): "))
voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
oil_level = float(input("Enter Oil Level (%): "))

fault = False
warnings = []

# Temperature check
if temperature > 90:
    fault = True
    warnings.append("High Temperature")
elif temperature > 70:
    warnings.append("Temperature High")

# Voltage check
if voltage < 210:
    fault = True
    warnings.append("Under Voltage")
elif voltage > 250:
    fault = True
    warnings.append("Over Voltage")

# Current check
if current > 10:
    fault = True
    warnings.append("Over Current")

# Oil level check
if oil_level < 40:
    fault = True
    warnings.append("Low Oil Level")
elif oil_level < 60:
    warnings.append("Oil Level Low")

print("\n===== TRANSFORMER DATA =====")
print("Temperature :", temperature, "°C")
print("Voltage     :", voltage, "V")
print("Current     :", current, "A")
print("Oil Level   :", oil_level, "%")

print("\n===== HEALTH STATUS =====")

if fault:
    print("STATUS: CRITICAL")
    print("Action: Maintenance Required")

elif len(warnings) > 0:
    print("STATUS: WARNING")
    print("Check:")
    for warning in warnings:
        print("-", warning)

else:
    print("STATUS: HEALTHY")

# Simulated IoT message
print("\n===== IoT CLOUD MESSAGE =====")
print("Transformer data uploaded successfully.")
