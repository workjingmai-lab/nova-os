#!/usr/bin/env python3
# Calculate ETA to 3000 blocks

current = 2880
target = 3000
remaining = target - current

# Velocity scenarios
velocities = {
    "Conservative": 30,      # blocks/hour
    "Sustained": 44,         # blocks/hour (current avg)
    "Optimistic": 50,        # blocks/hour
}

print(f"Current block: {current}")
print(f"Target: {target}")
print(f"Remaining: {remaining} blocks")
print()

for name, velocity in velocities.items():
    hours = remaining / velocity
    minutes = hours * 60
    print(f"{name}: {velocity} blocks/hr = {hours:.1f} hours ({minutes:.0f} minutes)")

print()
print(f"If started now (22:17Z):")
for name, velocity in velocities.items():
    from datetime import datetime, timedelta
    hours = remaining / velocity
    eta = datetime.utcnow() + timedelta(hours=hours)
    print(f"  {name}: {eta.strftime('%H:%MZ')} (~{hours:.1f} hours)")
