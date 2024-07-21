def is_possible_channel(channel, broken_buttons):
    for ch in str(channel):
        if ch in broken_buttons:
            return False
    return True

def find_min_presses(target_channel, broken_buttons):
    min_presses = abs(target_channel - 100)  # + or - only
    for channel in range(1000000):  # Consider larger range to include edge cases
        if is_possible_channel(channel, broken_buttons):
            presses = len(str(channel)) + abs(channel - target_channel)
            min_presses = min(min_presses, presses)
    return min_presses

# Input
N = int(input())
M = int(input())
if M > 0:
    broken_buttons = set(input().split())
else:
    broken_buttons = set()

# Output the minimum number of button presses
print(find_min_presses(N, broken_buttons))
