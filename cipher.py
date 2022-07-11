alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(new_text, new_shift): 
  cipher = ""
  for letter in new_text:
    position = alphabet.index(letter)
    new_position = position + new_shift
    new_letter = alphabet[new_position]
    cipher += new_letter
  print(f"The encoded text is {cipher}")


encrypt(new_text=text, new_shift=shift)
