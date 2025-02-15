from collections import deque
from math import remainder

def division_elements(grater_el, smaller_el):
    if smaller_el == 0:
        return 0
    remainder_from_division = grater_el % smaller_el
    return remainder_from_division

suggested_links = deque([int(el) for el in input().split()])
featured_articles = deque([int(el) for el in input().split()])
target_engagement_value = int(input())
final_feed_collection = []

while suggested_links and featured_articles:
    current_link = suggested_links.popleft()
    current_article = featured_articles.pop()
    if current_article == current_link:
        final_feed_collection.append(0)
    elif current_link < current_article:
        grater = current_article
        smaller = current_link
        current_remainder = division_elements(grater, smaller)
        final_feed_collection.append(abs(current_remainder))

        if current_remainder == 0:
            continue
        else:
            doubled_result = current_remainder * 2
            featured_articles.append(doubled_result)
    elif current_article < current_link:
        grater = current_link
        smaller = current_article
        current_remainder = division_elements(grater, smaller)
        final_feed_collection.append(-current_remainder)

        if current_remainder == 0:
            continue
        else:
            doubled_result = current_remainder * 2
            suggested_links.append(doubled_result)

total_engagement = sum(final_feed_collection)
print(f'Final Feed: {", ".join(map(str, final_feed_collection))}')
if total_engagement >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement}")



