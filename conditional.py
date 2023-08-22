#  > >= < <= != not or and
x_position = 1
end_position = 10
# suppose youhave two position, startingand ending, then test the logi below

is_at_end = x_position == end_position
print(is_at_end)

#  check if at halfway
is_at_half_way = x_position >= end_position / 2
print(is_at_half_way)

# logical operators

# not reverses a boolean

print(not is_at_end)
# or can also be written as 

not_is_at_end = not is_at_end
print(not_is_at_end)

# the and operators &&

score = 10
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# or return true if comparison is valid
score = 9
is_game_over = score >= 10 or is_at_end
print(is_game_over) 