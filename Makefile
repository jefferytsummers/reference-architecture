SHELL := /bin/zsh

.PHONY: npm-install
npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install
