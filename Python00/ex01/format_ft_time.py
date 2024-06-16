from datetime import datetime

epoch = datetime.fromisoformat("1970-01-01")
now = datetime.now()
secs = (now - epoch).total_seconds()
date = epoch.strftime("%B %-d, %Y")

print(f"Seconds since {date}: {secs:,.4f} or {secs:.3} in scientific notation")
print(now.strftime("%b %d %Y"))
