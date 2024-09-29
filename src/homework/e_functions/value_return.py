def get_hour(epoch_seconds):
    return (epoch_seconds // 3600) % 24

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60
