SHELL := /bin/zsh

PYTHON_SERVICES := python-service-one
DOTNET_SERVICES := dotnet-service-one
GENERATED_DIRECTORIES := PYTHON_SERVICES DOTNET_SERVICES
.PHONY: npm-install all clean-contracts $(PYTHON_SERVICES) $(DOTNET_SERVICES) 

python: $(PYTHON_SERVICES)
dotnet: $(DOTNET_SERVICES)
contracts: python dotnet

$(PYTHON_SERVICES):
	@echo "Generating Python code for $@..."
	protoc --proto_path=contracts/ --python_out=service/$@/contracts contracts/*.proto
	@echo "Python code generated successfully for $@."
$(DOTNET_SERVICES):
	@echo "Generating C# code for $@..."
	protoc --proto_path=contracts/ --csharp_out=service/$@/ contracts/*.proto
	@echo "C# code generated successfully for $@."




clean-contracts:
	@echo "Cleaning generated files..."
	rm -rf $(OUT_DIR)/*.*
	@echo "Cleanup completed."
npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install
