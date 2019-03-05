import sys
from .text_swapper import TextSwapperInMark

def swapInputLines():
	swapper = TextSwapperInMark()

	for line in sys.stdin:
		sys.stdout.write(swapper.swap(line))
