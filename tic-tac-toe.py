import tkinter as tk
import random


BG = "black"
FG = "white"
FONT = ('Helvetica', 20, 'bold')


class myApp:
	def __init__ (self, master):

		self.createGame(master)



	def createGame(self, master):

		self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		self.game_over = False
		self.winner = "NONE"


		self.top_frame = tk.Frame(master, bg=BG)
		self.top_frame.pack()

		self.container = tk.Frame(self.top_frame, bg=BG)
		self.container.pack()

		self.welcome_message = tk.Label(self.container, text="WELCOME TO TIC-TAC-TOE", bg=BG, fg=FG, font=FONT)
		self.welcome_message.grid(row=0, column=0, columnspan=2)

		self.hint_message = tk.Label(self.container, text="YOU PLAY FIRST!", bg=BG, fg=FG, font=FONT)
		self.hint_message.grid(row=1, column=0, columnspan=2)


		self.board_frame = tk.Frame(master)
		self.board_frame.pack()


		self.button_one = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_one.grid(row=1, column=0, padx=5, pady=5)
		self.button_one.config(command = lambda: self.clicked(0,0, self.button_one))

		self.button_two = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_two.grid(row=1, column=1, padx=5, pady=5)
		self.button_two.config(command = lambda: self.clicked(0,1, self.button_two))

		self.button_three = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_three.grid(row=1, column=2, padx=5, pady=5)
		self.button_three.config(command = lambda: self.clicked(0,2, self.button_three))

		self.button_four = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_four.grid(row=2, column=0, padx=5, pady=5)
		self.button_four.config(command = lambda: self.clicked(1,0, self.button_four))

		self.button_five = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_five.grid(row=2, column=1, padx=5, pady=5)
		self.button_five.config(command = lambda: self.clicked(1,1, self.button_five))

		self.button_six = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_six.grid(row=2, column=2, padx=5, pady=5)
		self.button_six.config(command = lambda: self.clicked(1,2, self.button_six))

		self.button_seven = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_seven.grid(row=3, column=0, padx=5, pady=5)
		self.button_seven.config(command = lambda: self.clicked(2,0, self.button_seven))

		self.button_eight = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_eight.grid(row=3, column=1, padx=5, pady=5)
		self.button_eight.config(command = lambda: self.clicked(2,1, self.button_eight))

		self.button_nine = tk.Button(self.board_frame, text=" ", width=10, height=5, bg=BG, fg=FG, font=FONT)
		self.button_nine.grid(row=3, column=2, padx=5, pady=5)
		self.button_nine.config(command = lambda: self.clicked(2,2, self.button_nine))


		self.reset_frame = tk.Frame(master)
		self.reset_frame.pack()

		self.reset_button  = tk.Button(self.reset_frame, text="RESET", command=lambda:self.reset(master), bg=BG, fg=FG, font=FONT)
		self.reset_button.grid(row=0, column=0, columnspan=2)


	def clicked(self, x, y, button):

		if not self.game_over:

			button.config(text="X", state="disabled")
			self.updateBoard(x, y)
			self.checkWin()


			if not self.isBoardFull():
				self.moveAI()

			else:
				self.update_frame()
				# print("BOARD FULL!")


	def updateBoard(self, x, y):

		self.board[x][y] = 1

		# print("******************HUMAN********************")
		# print(self.board)


	def moveAI(self): 

		if not self.game_over:

			random.seed()
			move_x = random.randrange(0, 3)
			move_y = random.randrange(0, 3)

			if(self.board[move_x][move_y] == 0):
				self.board[move_x][move_y] = 2
				self.updateButton(move_x, move_y)
				
				# print("******************AI********************")
				# print(self.board)

				self.checkWin()

			else:
				self.moveAI()


	def updateButton(self, x, y):

		if x==0 and y==0:
			self.button_one.config(text="O", state="disabled")

		elif x==0 and y==1:
			self.button_two.config(text="O", state="disabled")

		elif x==0 and y==2:
			self.button_three.config(text="O", state="disabled")

		elif x==1 and y==0:
			self.button_four.config(text="O", state="disabled")

		elif x==1 and y==1:
			self.button_five.config(text="O", state="disabled")

		elif x==1 and y==2:
			self.button_six.config(text="O", state="disabled")

		elif x==2 and y==0:
			self.button_seven.config(text="O", state="disabled")

		elif x==2 and y==1:
			self.button_eight.config(text="O", state="disabled")

		elif x==2 and y==2:
			self.button_nine.config(text="O", state="disabled")


	def isBoardFull(self):

		for i in range(0,3):
			for j in range(0,3):
				if self.board[i][j] == 0:
					return False

		return True


	def checkWin(self):

		# for rows
		for i in range(0,3):
			if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != 0:
					
				if self.board[i][0] == 1:
					self.winner = "X"
				else:
					self.winner = "O"

				# print("%s WINS" %(self.winner))
				self.updateButtonColor("row", i)
				self.game_over = True
				self.update_frame()
				break


		# for columns
		for i in range(0,3):
			if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != 0:
					
				if self.board[0][i] == 1:
					self.winner = "X"
				else:
					self.winner = "O"

				# print("%s WINS" %(self.winner))
				self.updateButtonColor("column", i)
				self.game_over = True
				self.update_frame()
				break


		# for diagonals
		if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] !=0:
			if self.board[0][0] == 1:
				self.winner = "X"
			else:
				self.winner = "O"

			# print("%s WINS" %(self.winner))
			self.updateButtonColor("diagonal", 0)
			self.game_over = True
			self.update_frame()


		if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] !=0:
			if self.board[0][2] == 1:
				self.winner = "X"
			else:
				self.winner = "O"

			# print("%s WINS" %(self.winner))
			self.updateButtonColor("diagonal", 1)
			self.game_over = True
			self.update_frame()


	def updateButtonColor(self, win_type, value):

		if win_type == "row":
			if value == 0:
				self.button_one.config(bg="green", fg="white")
				self.button_two.config(bg="green", fg="white")
				self.button_three.config(bg="green", fg="white")

			elif value == 1:
				self.button_four.config(bg="green", fg="white")
				self.button_five.config(bg="green", fg="white")
				self.button_six.config(bg="green", fg="white")

			elif value == 2:
				self.button_seven.config(bg="green", fg="white")
				self.button_eight.config(bg="green", fg="white")
				self.button_nine.config(bg="green", fg="white")


		if win_type == "column":
			if value == 0:
				self.button_one.config(bg="green", fg="white")
				self.button_four.config(bg="green", fg="white")
				self.button_seven.config(bg="green", fg="white")

			elif value == 1:
				self.button_two.config(bg="green", fg="white")
				self.button_five.config(bg="green", fg="white")
				self.button_eight.config(bg="green", fg="white")

			elif value == 2:
				self.button_three.config(bg="green", fg="white")
				self.button_six.config(bg="green", fg="white")
				self.button_nine.config(bg="green", fg="white")
			


		if win_type == "diagonal":
			if value == 0:
				self.button_one.config(bg="green", fg="white")
				self.button_five.config(bg="green", fg="white")
				self.button_nine.config(bg="green", fg="white")

			elif value == 1:
				self.button_three.config(bg="green", fg="white")
				self.button_five.config(bg="green", fg="white")
				self.button_seven.config(bg="green", fg="white")


	def update_frame(self):

		self.container.destroy()


		if self.winner != "NONE":

			if self.winner == "X":
				display_text = "YOU WIN!"
			else:
				display_text = "COMPUTER WINS!"

			win_label = tk.Label(self.top_frame, text=display_text, bg=BG, fg=FG, font=FONT)
			win_label.grid(row=0, column=0, columnspan=2)

		if self.isBoardFull() and self.winner == "NONE":
			draw_label = tk.Label(self.top_frame, text="DRAW MATCH!", bg=BG, fg=FG, font=FONT)
			draw_label.grid(row=0, column=0, columnspan=2) 


	def reset(self, master):
		
		self.top_frame.destroy()
		self.board_frame.destroy()
		self.reset_frame.destroy()

		self.createGame(master)



root = tk.Tk()
root.title("TIC-TAC-TOE")
root.config(bg=BG)
root.resizable(False, False)

app = myApp(root)

root.mainloop()
