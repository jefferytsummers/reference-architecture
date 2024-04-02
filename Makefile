SHELL := /bin/zsh

PYTHON_SERVICES := python-service-one
DOTNET_SERVICES := dotnet-service-one
NODE_SERVICES := node-service-one

.PHONY: npm-install all python dotnet node contracts clean-contracts $(PYTHON_SERVICES) $(DOTNET_SERVICES) $(NODE_SERVICES)

python: $(PYTHON_SERVICES)

dotnet: $(DOTNET_SERVICES)

node: $(NODE_SERVICES)

contracts: python dotnet node

$(PYTHON_SERVICES):
	@echo "Generating Python code for $@..."
	protoc --proto_path=contracts/ --python_out=services/$@/contracts contracts/*.proto
	@echo "Python code generated successfully for $@."

$(DOTNET_SERVICES):
	@echo "Generating C# code for $@..."
	protoc --proto_path=contracts/ --csharp_out=services/$@/contracts contracts/*.proto
	@echo "C# code generated successfully for $@."

$(NODE_SERVICES):
	@echo "Generating TypeScript code for $@..."
	protoc --proto_path=contracts/ --ts_out=services/$@/src/contracts --ts_opt=generate_package_definition contracts/*.proto
	@echo "TypeScript code generated successfully for $@."
	@echo "Compiling TypeScript code for $@..."
	cd services/$@; npm run build
	@echo "TypeScript code compiled successfully for $@."

clean-contracts:
	@echo "Cleaning generated files..."
	find $(addsuffix /contracts/, $(addprefix services/, $(PYTHON_SERVICES) $(DOTNET_SERVICES))) -type f -delete
	find $(addsuffix /src/contracts/, $(addprefix services/, $(NODE_SERVICES))) -type f -delete
	@echo "Cleanup completed."

npm-install:
	source ~/.nvm/nvm.sh && nvm use && npm install