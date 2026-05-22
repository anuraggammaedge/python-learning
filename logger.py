log_data = [
    {
        "timestamp": "2026-05-18T10:00:01Z",
        "log_level": "INFO",
        "message": "User login successful",
        "user_id": "USR-101"
    },
    {
        "timestamp": "2026-05-18T10:05:23Z",
        "log_level": "WARNING",
        "message": "Failed login attempt from unrecognized IP address",
        "user_id": "USR-102"
    },
    {
        "timestamp": "2026-05-18T10:05:23Z",
        "log_level": "WARNING",
        "message": "Failed login attempt from unrecognized IP address",
        "user_id": "USR-101"
    },
    {
        "timestamp": "2026-05-18T22:12:45Z",
        "log_level": "ERROR",
        "message": "Database connection timeout during payment processing",
        "user_id": "USR-104"
    },
    {
        "timestamp": "2026-05-18T10:15:00Z",
        "log_level": "INFO",
        "message": "Automated database backup completed successfully",
        "user_id": None  # System level action
    },
    {
        "timestamp": "2026-05-18T10:22:11Z",
        "log_level": "DEBUG",
        "message": "API payload validation completed in 45ms",
        "user_id": "USR-101"
    },
    {
        "timestamp": "2026-05-18T10:31:59Z",
        "log_level": "ERROR",
        "message": "Unauthorized attempt to access admin settings dashboard",
        "user_id": "USR-105"
    },
    {
        "timestamp": "2026-05-18T11:45:12Z",
        "log_level": "INFO",
        "message": "Password reset email dispatched to user inbox",
        "user_id": "USR-108"
    },
    {
        "timestamp": "2026-05-18T11:45:12Z",
        "log_level": "ERROR",
        "message": "ERROR Password reset email dispatched to user inbox",
        "user_id": "USR-108"
    },
    {
        "timestamp": "2026-05-18T12:50:34Z",
        "log_level": "CRITICAL",
        "message": "Memory usage exceeded safe operating threshold of 95%",
        "user_id": None  # Infrastructure level alert
    }
]


# hour_key = log_data[0]["timestamp"][:13] + ":00"
# hour_key = log_data[1]["timestamp"][:13] + ":00"
# hour_key = log_data[7]["timestamp"][11:13] + ":00"


# print(hour_key)

error_data ={}




for log in log_data:
    log_hour_key = log["timestamp"][11:13] + ":00"
    if log["log_level"] == "ERROR":
        if log_hour_key in error_data:
            error_data[log_hour_key].append(log)
        else:
            for hour in range(24):
                hour_key = f"{hour:02d}:00"
                if hour_key not in error_data:
                    error_data[hour_key] = []
            error_data[log_hour_key] = [log]
# print(error_data)


ll = list(filter(lambda log: log["log_level"] == "ERROR", log_data))

ll2 = [log for log in log_data if log["log_level"] == "ERROR"]

# print(ll)
# print(ll2)

from functools import reduce

user_freq = reduce(
    lambda acc, log: (
        acc.update(
            {
                log['user_id']: acc.get(log['user_id'], 0) + 1
            }
        ) or acc
        ),
    log_data,
    {}
)
print(user_freq)


def count_freq(acc, log):
    user_id = log['user_id']
    acc[user_id] = acc.get(user_id, 0) + 1 
    return acc

result = reduce(count_freq, log_data, {})
print(result)