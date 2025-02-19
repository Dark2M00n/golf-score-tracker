def main():
  name = ''
  golf_score = 0
  num_player = 0

  num_players = int(input("Enter the number of players in the tournament: "))

  outfile = open('golf.txt', 'w')

  for i in range(num_players):
    name = input("Enter the name of the player:")
    golf_score = int(input("Enter the golf score: "))

    outfile.write(name + '\n')
    outfile.write(str(golf_score) + '\n')

  outfile.close()
main()


def main():
  line = ''
  name = ''
  golf_score = 0
  num_players = 0

  infile = open('golf.txt', 'r')

  name = infile.readline()

  while name != '':
    golf_score = int(infile.readline())

    name = name.rstrip('\n')

    print('Name:', name)
    print('Golf Score:', golf_score)

    name = infile.readline()

  infile.close()
main()
