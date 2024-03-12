import tkinter as tk
from tkinter import filedialog, messagebox
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

class Lexer:
  def __init__(self, text):
    self.text = text
    self.pos = 0
    self.current_char = self.text[self.pos]
    self.keywords = ["if", "else", "while", "for", "return"]

  def advance(self):
    self.pos += 1
    if self.pos < len(self.text):
      self.current_char = self.text[self.pos]
    else:
      self.current_char = None

  def skip_whitespace(self):
    while self.current_char is not None and self.current_char.isspace():
      self.advance()

  def get_identifier(self):
    result = ''
    while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit()):
      result += self.current_char
      self.advance()

    if result in self.keywords:
      return Token(result.upper(), result)
    else:
      return Token("IDENTIFIER", result)

  def get_real(self):
    integer_part = ''
    decimal_part = ''
     
    while self.current_char is not None and self.current_char.isdigit():
      integer_part += self.current_char
      self.advance()
     
    if self.current_char == '.':
      self.advance()
       
      while self.current_char is not None and self.current_char.isdigit():
        decimal_part += self.current_char
        self.advance()

    if integer_part or decimal_part:
      return float(f"{integer_part}.{decimal_part}")
    else:
      raise ValueError("Invalid real number format")

  def get_string(self):
    result = ''
    if self.current_char == '"':
      self.advance()
      while self.current_char is not None and self.current_char != '"':
        result += self.current_char
        self.advance()
      if self.current_char == '"':
        self.advance()
        return Token("STRING", result)
    raise ValueError("Invalid string format")
     
  def get_next_token(self):
    while self.current_char is not None:
      if self.current_char.isspace():
        self.skip_whitespace()
        continue

      if self.current_char.isalpha():
        return self.get_identifier()

      if self.current_char.isdigit():
        return Token("REAL", self.get_real())
       
      if self.current_char == '"':
        return self.get_string()
       
      if self.current_char in "+-*/<>=!&|(){};":
        token_type = self.current_char
        self.advance()
        return Token(token_type, token_type)
       
      raise ValueError(f"Invalid character: {self.current_char}")

    return Token("EOF", None)

def analyze_file(filename):
  try:
    with open(filename, 'r') as file:
      text = file.read()
  except FileNotFoundError:
    raise FileNotFoundError("File not found!")

  lexer = Lexer(text)
  tokens = []
  while True:
    try:
      token = lexer.get_next_token()
      tokens.append(token)
      if token.type == "EOF":
        break
    except ValueError as e:
      messagebox.showerror("Error", str(e))
      return []

  return tokens

def browse_file():
  filename = filedialog.askopenfilename()
  if filename:
    try:
      tokens = analyze_file(filename)
      token_list.delete(1.0, tk.END)
      for token in tokens:
        token_list.insert(tk.END, f"{token.type}: {token.value}\n")
    except Exception as e:
      messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Token Analyzer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

token_list = tk.Text(frame, width=50, height=20)
token_list.pack(side=tk.RIGHT)

root.mainloop()
