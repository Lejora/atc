N = int(input())
card_box = map(int, input().split(" "))

sorted_card_box = sorted(card_box, reverse=True)

point_alice = 0
point_bob = 0

for i in range(len(sorted_card_box)):
  selected_card = sorted_card_box[i]

  if i % 2 == 0:
    point_alice += selected_card
  else:
    point_bob += selected_card

result = point_alice - point_bob

print(result)