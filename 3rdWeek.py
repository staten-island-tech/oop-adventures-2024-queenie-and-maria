import datetime

day=datetime.date(year=1842, month=7, day=26)

events = [
    {"event": "Start Project", "date": day},
    {"event": "First Milestone", "date": day + datetime.timedelta(days=5)},
    {"event": "Second Milestone", "date": day + datetime.timedelta(days=10)},
    {"event": "Finish Project", "date": day + datetime.timedelta(days=15)},
]

# Print the timeline
print("Project Timeline:")
for event in events:
    print(f"{event['date']} - {event['event']}")
