import math

sodukoGrid = [
	[7,0,0,0,3,4,8,0,0],
	[8,0,4,6,0,0,0,0,0],
	[0,3,9,0,5,0,0,0,0],
	[1,0,0,5,0,0,6,0,0],
	[0,4,0,7,0,9,0,3,0],
	[0,0,3,0,0,8,0,0,9],
	[0,0,0,0,7,0,3,2,0],
	[0,2,6,0,0,1,9,0,5],
	[0,0,7,9,2,0,0,0,4]
]

Size = len(sodukoGrid)
print("The Sudoku Grid Is", Size, "By", Size, "\n")

for Row in range(Size):
	print(sodukoGrid[Row])
print()

Area = int(math.sqrt(Size))
print("The Size Of The Area Is", Area, "By", Area, "\n")

gridUpdated = True
while(gridUpdated):
	gridUpdated =False
	for Target in range(1, Size + 1):
		Row = 0
		while (Row < Size):	
			Column = 0
			while(Column < Size):
				print("Checking The Following Value For A Target:", Target)
				print("Start Row:", Row)
				print("End Row:", Row + Area - 1)
				print("Start Column:", Column)
				print("End Column:", Column + Area - 1, "\n")

				foundTarget = False
				for R in range(Row, Row + Area):
					for C in range(Column, Column + Area):
						if(sodukoGrid[R][C] == Target):
							foundTarget = True
							break

				print("The Target Value", Target, end="")
				if not foundTarget:
					print(" Was Not In The Area\n")
					PlaceTargetAt = []
					for R in range(Row, Row + Area):
						for C in range(Column, Column + Area):
							print("Checking: Row", R, "Column", C)
							if(sodukoGrid[R][C] == 0):
								print("Square Availible")
								currentRowValues = sodukoGrid[R]
								currentColumnValues = [Item[C] for Item in sodukoGrid]
								print("Row Contains ", currentRowValues)
								print("Column Contains", currentColumnValues)
								if Target not in currentRowValues and Target not in currentColumnValues:
									print("Could Place",Target,"At [",R,",",C,"]\n")
									PlaceTargetAt.append([R,C])
					if(len(PlaceTargetAt) == 1):
						print("Placed", Target, "At", PlaceTargetAt[0][0], "x", PlaceTargetAt[0][1])
						sodukoGrid[PlaceTargetAt[0][0]][PlaceTargetAt[0][1]] = Target
						gridUpdated = True
				else:
					print(" Was Found In The Area\n")

				Column += Area
			Row += Area
	for Row in range(0,Size):
		if 0 in sodukoGrid[Row]:
			for Column in range(0, Size):
				if sodukoGrid[Row][Column] == 0:
					currentRowValues = sodukoGrid[Row]
					currentColumnValues = [Item[Column] for Item in sodukoGrid]
					validChoices = []
					for N in range(1, Size + 1):
						if N not in currentRowValues and N not in currentColumnValues:
							validChoices.append([Row,Column,N])
					if len(validChoices) == 1:
						X = validChoices[0][0]
						Y = validChoices[0][1]
						N = validChoices[0][2]
						sodukoGrid[X][Y] = N
						gridUpdated = True

for Row in range(Size):
	print(sodukoGrid[Row])
