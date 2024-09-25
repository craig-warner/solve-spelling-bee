setup: requirements.txt
	pip3 install --user -r requirements.txt --break-system-packages

run:
	python3 ssb.py --center_letter a --letter1 e --letter2 i --letter3 v --letter4 l --letter5 n --letter6 j

clean:
	rm -rf __pycache__
