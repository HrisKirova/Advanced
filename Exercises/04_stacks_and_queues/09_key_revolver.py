from collections import deque
from itertools import count

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())
shoots = 0
while locks and bullets_stack:

    current_bullet = bullets_stack.pop()
    current_lock = locks.popleft()
    intelligence_value -= bullet_price
    shoots += 1
    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)
    if shoots == barrel_size and bullets_stack:
        print("Reloading!")
        shoots = 0

if not locks:
    print(f"{len(bullets_stack)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
    # compare the bullet and the lock -> Bang or Ping (+ return the lock)
    # deduct the bullet price from the intelligence value
    # when the barrel is empty -> reload if there are bullets
