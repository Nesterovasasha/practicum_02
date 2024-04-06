wives = 7
bags_per_wife = 7
cats_per_bag = 7
kittens_per_cat = 7

total_people_and_animals = 1 + wives + wives * bags_per_wife * cats_per_bag + wives * bags_per_wife * cats_per_bag * kittens_per_cat

print("Общее количество людей и животных, направляющихся в Сент-Айвс: ", total_people_and_animals)
